import uuid
from datetime import datetime, timedelta
from enum import Enum
from sys import maxsize

from dateutil import rrule

from Progetto.Component.ComponentBilancio import ComponentBilancio
from Progetto.listaprodotti.model.ProdottoConQuantità import ProdottoConQuantità

GIORNI_IN_ANNO = 365  # Numero minimo di giorni in un anno
GIORNI_IN_MESE = 28  # Numero minimo di giorni in un mese


class Periodicita(Enum):
    """
    Indica il tipo di periodicità assegnabile ad una voce di bilancio
    """
    NESSUNA = 0
    GIORNALIERA = 1
    SETTIMANALE = 2
    MENSILE = 3
    ANNUALE = 4

    def __str__(self):
        """
        Stringa che descrive la periodicità
        """
        match self:
            case Periodicita.NESSUNA:
                return 'Non periodico'
            case Periodicita.GIORNALIERA:
                return 'Giorni'
            case Periodicita.SETTIMANALE:
                return 'Settimane'
            case Periodicita.MENSILE:
                return 'Mesi'
            case Periodicita.ANNUALE:
                return 'Anni'


MESI_IN_UN_ANNO = 12


class ComponenteGenerica(ComponentBilancio):
    """
    Le istanze diuesta classe rappresentano una componente generica di bilancio che può essere passata al costruttore di VoceDiBilancio
    """

    def __init__(self, valore, nome: str):
        """
        :param valore: valore associato alla componente(espresso in centesimi di euro)
        :param nome: stringa che descrive la coponente
        """
        super(ComponenteGenerica, self).__init__()
        self.valore = None
        self.set_valore(valore)
        self.nome = nome
        self.id = uuid.uuid4()

    def get_valore(self):
        return self.valore

    def get_nome(self):
        return self.nome

    def set_valore(self, nuovo):
        self.valore = nuovo

    def __str__(self):
        """
        :return: stringa che descrive la componente indicando il valore in euro e centesimi
        """
        euro_cent = self.get_valore_euro()
        return '({nome}, {euro}.{cent} €)'.format(nome=self.get_nome(), euro=euro_cent[0], cent=euro_cent[1])


def prova_occorrenze():
    v1 = VoceDiBilancio(ComponenteGenerica(5000, 'Pepe'), False, Periodicita.SETTIMANALE, arg_periodicita=1,
                        iterazioni=15)
    v2 = VoceDiBilancio(ComponenteGenerica(150000, 'Comodato d\'uso'), True, Periodicita.ANNUALE, arg_periodicita=1,
                        iterazioni=16)
    v3 = VoceDiBilancio(ComponenteGenerica(30000, 'Cozze'), True, Periodicita.NESSUNA,
                        data=datetime.today().replace(day=28))
    d1 = datetime(2022, 1, 27, 0, 0)
    d2 = datetime(2022, 3, 11, 0, 0)
    d3 = datetime(2022, 4, 23)
    d4 = datetime(2022, 5, 26)
    d5 = datetime(2024, 1, 1)
    l1 = v1.occorrenze_in(d1, d4)
    l2 = v1.occorrenze_in(d1, d2)
    l3 = v1.occorrenze_in(d2, d5)
    l4 = v2.occorrenze_in(d2, d5)
    l5 = v3.occorrenze_in(d3, d4)
    l6 = v3.occorrenze_in(d4, d5)
    print('l1: ' + l1.__str__())
    print('l2: ' + l2.__str__())  # Deve essere vuoto
    print('l3: ' + l3.__str__())
    print('Dimensione l3: ' + v1.occorre_in(d2, d5).__str__() + ' == ' + v1.get_iterazioni().__str__())
    print('l4: ' + l4.__str__())  # Dovrebbe avere due date
    print('l5: ' + l5.__str__())  # Data di oggi
    print('l6: ' + l6.__str__())  # Vuoto


class VoceDiBilancio:
    """
    Classe che descrive un oggetto che andrà utilizzato per comporre i vari bilanci (mensili e settimanali): un istanza di tale classe
    può esprimere sia un'entrata che un'uscita, ricorrente o non ricorrente
    """

    # La ricorrenza deve essere utilizzata con una risoluzione massima di un giorno e deve essere non negativa, altrimenti viene lanciata un ValueError
    # La ricorrenzaa uguale al tempo nullo indica che la voce non è ricorrente
    # 'iterazioni' indica il numero di volte in cui la voce sarà aggiunta al bilancio
    def __init__(self, component: ComponentBilancio, entrata: bool, periodicita: Periodicita, arg_periodicita=1,
                 iterazioni=maxsize,
                 data=datetime.today()):
        """

        Esempio di init: VoceDiBilancio(affitto, false, Periodicita.Mensile, arg_periodicita=1, iterazioni=62, datetime=datetime.datetime(2020, 3, 12)) (dove affitto è
        un componentBilancio) restituisce un oggetto che descrive un pagamento (l'affitto) che deve essere effettuato ogni mese per 62 mesi a partire dalla data 12 Marzo 2020
        :param component: Componente di bilancio associata
        :param entrata: booleano che se impostato a vero indica che l'oggetto instanziato si riferisce ad un'entrata, se falso si riferisce ad un'usicta
        :param periodicita: indica il tipo di periodicità: se uguale a Periodicita.NESSUNA la voce descrive un entrata/uscita non ricorrente
        :param arg_periodicita: intero che indica ogni quanti giorni/settimane/mesi/anni la voce deve entrare in bilancio
        :param iterazioni: intero che indica quante volte la voce deve entrare in bilancio
        :param data: datetime che indica la data della prima volta in cui la voce deve entrare a bilancio
        """

        self.component = component
        self.prodotto = None
        if isinstance(component, ProdottoConQuantità):
            self.prodotto = component
        self.entrata = entrata
        self.periodicita = periodicita
        self.iterazioni = None
        if periodicita == Periodicita.NESSUNA:
            self.periodico = False
            self.arg_periodicita = 0
            self.set_iterazioni(iterazioni)
        else:
            self.periodico = True
            if arg_periodicita <= 0:
                raise ValueError('L\'argomento deve essere positivo se la voce è periodica')
            self.arg_periodicita = arg_periodicita
            self.set_iterazioni(iterazioni)
        self.valore = component.get_valore()
        self.data = data
        self.id = uuid.uuid4()
        self.storico_valori = []
        if self.is_periodico():
            self.storico_valori.append((data, component.get_valore()))
        self.eterno = None
        if self.get_periodicita() != Periodicita.NESSUNA and iterazioni >= 10000:
            self.eterno = True
        else:
            self.eterno = False

    def get_prodotto(self):
        """
        Da chiamare solo se il compoentne è di tipo Prodotto altrimenti viene restituito un RunTimeError (usare is_product() per il controllo)
        :return: prodotto associato alla voce, se esiste
        """
        if self.is_product():
            return self.prodotto
        else:
            raise RuntimeError('Non è definito nessun prodotto per questa voce di bilancio')

    def is_periodico(self):
        """
        :return: vero se la voce è periodica, falso altrimenti
        """
        if self.periodico:
            return True
        return False

    def get_periodicita(self):
        return self.periodicita

    def get_valore(self):
        """
        :return: il valore del componente associato alla voce
        """
        return self.component.get_valore()

    def aggiorna_valore(self, nuovo_valore: int):
        """
        Metodo per aggiornare il valore all'interno della componente associata alla voce.
        Nota: per una voce periodica se si cambia il valore esso descriverà il valore per tutto il periodo della voce: se si desidera cambiare
        il valore della voce a partire da una data ridurre il numero delle iterazioni in modo che la voce scada in quella data attraverso set_iterazioni() e creare una nuova voce con il nuovo valore
        :param nuovo_valore: nuovo valore da assegnare
        """
        if isinstance(self.component, ComponenteGenerica):
            if nuovo_valore < 0:
                raise ValueError('Inserire un valore non negativo')
            self.component.set_valore(nuovo_valore)
        self.component.aggiorna_valore()
        if self.is_periodico():
            self.valore = self.component.get_valore()

    def is_product(self):
        """
        :return: vero se il componente associato alla voce è un'istanza di Prodotto, falso altrimenti
        """
        if self.prodotto is None:
            return False
        else:
            return True

    def is_entrata(self):
        if self.entrata:
            return True
        return False

    def get_data(self):
        """
        :return: la data della priam occorrenza della voce
        """
        return self.data

    def get_id(self):
        return self.id

    def is_eterno(self):
        if self.eterno:
            return True
        return False

    def get_iterazioni(self):
        return self.iterazioni

    def set_iterazioni(self, nuovo_numero: int):
        if nuovo_numero < 0:
            raise ValueError('Il numero delle iterazioni deve essere non negativo')
        self.iterazioni = nuovo_numero

    def get_timedelta(self):
        """
        :return: timedelta ottenuto come datetime che descrive la scadenza - datetime che descrive la prima occorrenza
        """
        match self.get_periodicita():
            case Periodicita.NESSUNA:
                raise RuntimeError('Il timedelta non è definito su una voce non periodica')
            case Periodicita.GIORNALIERA:
                return timedelta(days=1) * self.arg_periodicita * self.get_iterazioni() - timedelta(seconds=1)
            case Periodicita.SETTIMANALE:
                return timedelta(weeks=1) * self.arg_periodicita * self.get_iterazioni() - timedelta(seconds=1)
            case Periodicita.MENSILE:
                data_iniziale = self.get_data()
                mesi_totali = self.arg_periodicita * self.get_iterazioni()
                anno_finale = data_iniziale.year + mesi_totali // MESI_IN_UN_ANNO
                mesi_totali -= mesi_totali // MESI_IN_UN_ANNO
                mese_finale = data_iniziale.month + mesi_totali
                data_finale = datetime(anno_finale, mese_finale, data_iniziale.day, data_iniziale.hour,
                                       data_iniziale.minute, data_iniziale.second)
                return data_finale - data_iniziale - timedelta(seconds=1)
            case Periodicita.ANNUALE:
                data_iniziale = self.get_data()
                anni_finali = data_iniziale.year + self.arg_periodicita * self.get_iterazioni()
                data_finale = datetime(anni_finali, data_iniziale.month, data_iniziale.day, data_iniziale.hour,
                                       data_iniziale.minute, data_iniziale.second)
                return data_finale - data_iniziale - timedelta(seconds=1)

    def get_ultima_data(self) -> datetime:
        """
        :return: datetime che descrive la scadenza (datetime molto lontano nel fututro se la voce è eterna)
        """
        if self.is_eterno():
            return datetime.max  # giorno molto lontano futuro
        data = self.get_data()
        match self.get_periodicita():
            case Periodicita.NESSUNA:
                pass
            case Periodicita.GIORNALIERA:
                data += self.get_timedelta()
            case Periodicita.SETTIMANALE:
                data += self.get_timedelta()
            case Periodicita.MENSILE:
                data_iniziale = self.get_data()
                mesi_totali = self.arg_periodicita * self.get_iterazioni()
                anno_finale = data_iniziale.year + mesi_totali // MESI_IN_UN_ANNO
                mesi_totali -= mesi_totali // MESI_IN_UN_ANNO
                mese_finale = data_iniziale.month + mesi_totali
                if mese_finale > 12:
                    anno_finale += 1
                    mese_finale -= 12
                data = datetime(anno_finale, mese_finale, data_iniziale.day, data_iniziale.hour, data_iniziale.minute,
                                data_iniziale.second)
            case Periodicita.ANNUALE:
                data_iniziale = self.get_data()
                anni_finali = data_iniziale.year + self.arg_periodicita * self.get_iterazioni()
                data = datetime(anni_finali, data_iniziale.month, data_iniziale.day, data_iniziale.hour,
                                data_iniziale.minute, data_iniziale.second)
            case _:
                raise NotImplementedError
        return data

    def occorre_in(self, data_iniziale: datetime, data_finale: datetime):
        """
        Funzione per verificare se la VoceDiBilancio ha un'occorrenza in un periodo
        :param data_iniziale:
        :param data_finale:
        :return: il numero di volte in cui la voce occorre nella data specificata
        """
        return len(self.occorrenze_in(data_iniziale, data_finale))

    def occorrenze_in(self, data_iniziale: datetime, data_finale: datetime):
        """
        Funzione per ottenere le occorrenze in un certo range di tempo
        :param data_iniziale: data iniziale del range
        :param data_finale: data finale del range
        :return: lista delle date relative alle occorrenze della VoceDiBilancio
        """
        data_finale -= timedelta(seconds=1)
        start = max(self.get_data(), data_iniziale)
        if not self.is_eterno():
            until = min(self.get_ultima_data(), data_finale)
        else:
            until = data_finale
        lista_occorrenze = []
        match self.get_periodicita():
            # Per le voci non periodiche basta guardare la data iniziale
            case Periodicita.NESSUNA:
                if data_iniziale <= self.get_data() <= data_finale:
                    lista_occorrenze.append(self.get_data())
            case Periodicita.GIORNALIERA:
                for dt in rrule.rrule(rrule.DAILY, dtstart=start, until=until):
                    lista_occorrenze.append(dt)
            case Periodicita.SETTIMANALE:
                for dt in rrule.rrule(rrule.WEEKLY, byweekday=self.get_data().weekday(), dtstart=start, until=until):
                    lista_occorrenze.append(dt)
            case Periodicita.MENSILE:
                for dt in rrule.rrule(rrule.MONTHLY, bymonthday=self.get_data().timetuple().tm_mday, dtstart=start,
                                      until=until):
                    lista_occorrenze.append(dt)
            case Periodicita.ANNUALE:
                for dt in rrule.rrule(rrule.YEARLY, byyearday=self.get_data().timetuple().tm_yday, dtstart=start,
                                      until=until):
                    lista_occorrenze.append(dt)
            case _:
                raise NotImplementedError
        return lista_occorrenze

    def generator_date(self) -> datetime:
        i = 0
        while i <= self.arg_periodicita:
            yield self.get_data() + self.get_timedelta() * i

    def __hash__(self):
        return hash((self.component, self.entrata, self.periodicita, self.arg_periodicita, self.iterazioni, self.data))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id

    def __str__(self):
        if self.is_entrata():
            stringa_entrata = 'ENTRATA'
        else:
            stringa_entrata = 'USCITA'
        if self.is_eterno():
            stringa_periodicita = 'RICORRENZA: per sempre'
        elif self.is_periodico():
            stringa_periodicita = 'RICORRENZA: ogni ' + self.arg_periodicita.__str__() + ' ' + self.get_periodicita().__str__() + '  per ' + self.get_iterazioni().__str__() + ' volte'
        else:
            stringa_periodicita = 'NON PERIODICO'
        return '(COMPONENTE: ' + self.component.__str__() + '; ' + stringa_entrata + '; ' + stringa_periodicita + '; ' + 'PRIMA OCCORRENZA: ' + self.get_data().strftime(
            '%Y-%m-%d') + ' [anno-mese-giorno])'

    # def occorre_in(self, data_iniziale: datetime, data_finale: datetime):
    #     """
    #     Funzione per verificare se la VoceDiBilancio ha un'occorrenza in un periodo
    #     :param data_iniziale:
    #     :param data_finale:
    #     :return: il numero di volte in cui la voce occorre nella data specificata
    #     """

    #
    #
    #     def is_in_range(data: datetime):
    #         """
    #         :param data:
    #         :return: vero se la data appartiene al range nel quale la VoceDiBilancio è definita, falso altrimenti
    #         """
    #         return self.get_data() <= data <= self.get_ultima_data()
    #
    #     # In base al tipo di periodicità dobbiamo effettuare operazioni diverse
    #     match self.get_periodicita():
    #         # Per le voci non periodiche basta guardare la data iniziale
    #         case Periodicita.NESSUNA:
    #             if self.get_data() == data_iniziale:
    #                 return 1
    #             else:
    #                 return 0
    #         case Periodicita.GIORNALIERA:
    #             # Il numero massimo di occorrenze può essere:
    #             num_max = data_finale.day - data_iniziale.day + 1
    #             giorni = self.get_ultima_data() - data_iniziale + 1
    #             if giorni.days >= 0:
    #                 if giorni.days > num_max:
    #                     return num_max
    #                 else:
    #                     return giorni.days
    #             else:
    #                 return 0
    #         case Periodicita.SETTIMANALE:
    #             start = max(self.get_data(), data_iniziale)
    #             until = min(self.get_ultima_data(), data_finale)
    #             lista_occorrenze = rrule.rrule(rrule.MONTHLY, bymonthday=self.get_data().day, dtstart=start, until=until)
    #             return len(lista_occorrenze)
    #             # giorno_settimanale_occorrenza = self.get_data().weekday()
    #             # # I giorni che ci interessano sono quelli tra le date passate alla funzione se sono nello stesso giorno
    #             # # della settimana della VoceDiBilancio e se
    #             # occorrenze = [day for day in
    #             #               (data_iniziale + timedelta(days=n) for n in range(data_finale.day - data_iniziale.day)) if
    #             #               day.weekday() == giorno_settimanale_occorrenza and is_in_range(day)]
    #             # return len(occorrenze)
    #         case Periodicita.MENSILE:
    #             start = max(self.get_data(), data_iniziale)
    #             until = min(self.get_ultima_data(), data_finale)
    #             lista_occorrenze = rrule.rrule(rrule.MONTHLY, bymonthday=self.get_data().day, dtstart=start, until=until)
    #             return len(lista_occorrenze)
    #         case Periodicita.ANNUALE:
    #             start = max(self.get_data(), data_iniziale)
    #             until = min(self.get_ultima_data(), data_finale)
    #             lista_occorrenze = rrule.rrule(rrule.YEARLY, bymonthday=self.get_data().day, dtstart=start, until=until)
    #             return len(lista_occorrenze)


if __name__ == "__main__":
    prova_occorrenze()
