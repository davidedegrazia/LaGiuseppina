import json
from calendar import monthrange
from datetime import datetime, timedelta

from Progetto.contabilità.model.VoceDiBilancio import VoceDiBilancio, ComponenteGenerica, Periodicita

pth_voci = 'contabilità/data/voci_di_bilancio.json'


def __ProvaBilancioSettimanale():
    oggi = datetime.today()
    v1 = VoceDiBilancio(ComponenteGenerica(5000, 'Pepe'), False, Periodicita.SETTIMANALE, arg_periodicita=1,
                        iterazioni=15)
    v2 = VoceDiBilancio(ComponenteGenerica(150000, 'Comodato d\'uso'), True, Periodicita.ANNUALE, arg_periodicita=1,
                        iterazioni=16)
    v3 = VoceDiBilancio(ComponenteGenerica(30000, 'Cozze'), True, Periodicita.NESSUNA, arg_periodicita=1,
                        data=oggi.replace(day=28))
    try:
        v4 = VoceDiBilancio(ComponenteGenerica(500, 'Software vari'), False, Periodicita.GIORNALIERA, arg_periodicita=1,
                            data=oggi.replace(day=datetime.today().day + 1))
    except Exception:
        try:
            v4 = VoceDiBilancio(ComponenteGenerica(500, 'Software vari'), False, Periodicita.GIORNALIERA,
                                arg_periodicita=1,
                                data=oggi.replace(day=1, month=datetime.today().month + 1))
        except Exception:
            v4 = VoceDiBilancio(ComponenteGenerica(500, 'Software vari'), False, Periodicita.GIORNALIERA,
                                arg_periodicita=1,
                                data=oggi.replace(day=1, month=1, year=datetime.today().year + 1))
    vettore = [v1, v2, v3, v4]
    b1 = BilancioSettimanale(vettore, oggi.year, oggi.isocalendar().week)
    # print(v4.occorrenze_in(datetime.today(), datetime.today() + timedelta(weeks=1)))
    v_settimana = b1.get_voci_settimanali()
    e_settimana = b1.get_entrate_settimanali()
    u_settimana = b1.get_uscite_settimanali()
    print('Voci per la settimana numero ' + b1.get_settimana().__str__() + ' dell\'anno ' + b1.get_anno().__str__())
    for v in v_settimana:
        print(v[0])
    print('Solo entrate:')
    for e in e_settimana:
        print(e[0])
    print('Solo uscite:')
    for u in u_settimana:
        print(u[0])
    print(b1.get_utile().__str__() + ' == ' + b1.get_ricavo().__str__() + '-' + b1.get_costi().__str__() + '(=' + (
            b1.get_ricavo() - b1.get_costi()).__str__() + ')')


def __ProvaBilancioMensile():
    oggi = datetime.today()
    v1 = VoceDiBilancio(ComponenteGenerica(5000, 'Pepe'), False, Periodicita.SETTIMANALE, arg_periodicita=1,
                        iterazioni=15)
    v2 = VoceDiBilancio(ComponenteGenerica(150000, 'Comodato d\'uso'), True, Periodicita.ANNUALE, arg_periodicita=1,
                        iterazioni=16)
    v3 = VoceDiBilancio(ComponenteGenerica(30000, 'Cozze'), True, Periodicita.NESSUNA, arg_periodicita=1,
                        data=oggi.replace(day=28))
    try:
        v4 = VoceDiBilancio(ComponenteGenerica(500, 'Software vari'), False, Periodicita.GIORNALIERA, arg_periodicita=1,
                            data=oggi.replace(day=datetime.today().day + 1))
    except Exception:
        try:
            v4 = VoceDiBilancio(ComponenteGenerica(500, 'Software vari'), False, Periodicita.GIORNALIERA,
                                arg_periodicita=1,
                                data=oggi.replace(day=1, month=datetime.today().month + 1))
        except Exception:
            v4 = VoceDiBilancio(ComponenteGenerica(500, 'Software vari'), False, Periodicita.GIORNALIERA,
                                arg_periodicita=1,
                                data=oggi.replace(day=1, month=1, year=datetime.today().year + 1))
    vettore = [v1, v2, v3, v4]
    b1 = BilancioMensile(vettore, 2022, datetime.today().month)
    v_settimana = b1.get_voci_mensili()
    e_settimana = b1.get_voci_mensili()
    u_settimana = b1.get_voci_mensili()
    print('Voci per il mese numero ' + b1.get_mese().__str__() + ' dell\'anno ' + b1.get_anno().__str__())
    for v in v_settimana:
        print(v[0])
    print('Solo entrate:')
    for e in e_settimana:
        print(e[0])
    print('Solo uscite:')
    for u in u_settimana:
        print(u[0])
    print(b1.get_utile().__str__() + ' == ' + b1.get_ricavo().__str__() + '-' + b1.get_costi().__str__() + '(=' + (
            b1.get_ricavo() - b1.get_costi()).__str__() + ')')


class BilancioSettimanale:
    """
    Classe da utilizzare per descrivere un bilancio settimanale
    Attualmente funziona solo con VoceDiBilancio con arg_periodicita = 1 o VoceDiBilancio non periodica
    """

    def __init__(self, voci: list[VoceDiBilancio], anno=datetime.today().isocalendar().year,
                 settiamna_iso=datetime.today().isocalendar().week):
        """
        :param anno:
        :param settiamna_iso: settimana dell'anno a cui il bilancio si riferisce (secondo la convenzione ISO)
        :param voci: array contenente un set di voci ordinate per scadenza crescente nel quale sono presenti le voci che devono essere inserite nel bilancio settimanale
        """
        self.costi = None
        self.ricavo = None
        self.utile = None
        self.anno = anno
        self.settimana_iso = settiamna_iso
        self.tutte_le_voci = voci
        self.voci_settimana = self.__trova_voci_settimanali()
        self.costi = self.get_costi()
        self.ricavo = self.get_ricavo()
        self.utile = self.get_utile()

    def __trova_voci_settimanali(self):
        """
        funzione da utilizzare solo per l'inizializzazione del BilancioSettimanale
        :return:array di tuple del tipo (ComponentBilancio, datetime, bool)
        """
        # troviamo prima e ultima data della settimana
        first_day = datetime.fromisocalendar(self.get_anno(), self.get_settimana(), 1)
        delta = timedelta(days=7) - timedelta(microseconds=1)
        last_day = first_day + delta

        # vettore delle voci a cui siamo interessati
        voci_date = []
        for voce in self.tutte_le_voci:
            occorrenze = voce.occorrenze_in(first_day, last_day)
            for data in occorrenze:
                voci_date += [(voce.component, data, voce.is_entrata())]
            # voci_date += [(voce.component, data) for data in occorrenze if len(occorrenze) > 0]
        # voci_settimanali = [voce for voce in self.tutte_le_voci if
        #                     is_in_range(voce)]
        return sorted(voci_date, key=lambda v: v[1])

    def get_anno(self):
        """
        :return: anno al quale si riferisce il bilancio
        """
        return self.anno

    def get_settimana(self):
        """
        :return: settimana alla quale si riferisce il bilancio
        """
        return self.settimana_iso

    def get_data_iniziale(self):
        return datetime.fromisocalendar(self.anno, self.settimana_iso, 1)

    def get_data_finale(self):
        return datetime.fromisocalendar(self.anno, self.settimana_iso, 7)

    def get_voci_settimanali(self):
        """
        :return: array composto da elementi del tipo (ComponentBilancio, data, bool) ordinato per data crescente in cui il booleano di ogni elemento è vero se il ComponentBilancio si riferisce a un'entrata, falso altrimenit
        """
        return self.voci_settimana

    def get_utile(self):
        """
        :return: utile
        """
        self.utile = 0

        def aggiungi_a_utile(
                x: tuple):
            if x[2]:
                self.utile += x[0].get_valore()
            else:
                self.utile -= x[0].get_valore()

        voci = self.get_voci_settimanali()

        for voce in voci:
            aggiungi_a_utile(voce)
        return self.utile

    def get_entrate_settimanali(self):
        return [(voce[0], voce[1]) for voce in self.get_voci_settimanali() if voce[2]]

    def get_uscite_settimanali(self):
        return [(voce[0], voce[1]) for voce in self.get_voci_settimanali() if not voce[2]]

    def get_ricavo(self):
        self.ricavo = 0
        for entrata in self.get_entrate_settimanali():
            self.ricavo += entrata[0].get_valore()
        return self.ricavo

    def get_costi(self):
        self.costi = 0
        for uscita in self.get_uscite_settimanali():
            self.costi += uscita[0].get_valore()
        return self.costi

    def add(self, voce: VoceDiBilancio):
        self.tutte_le_voci.add(voce)
        self.__init__(self.tutte_le_voci, self.anno, self.settimana_iso)

    def remove(self, voce: VoceDiBilancio):
        self.tutte_le_voci.remove(voce)
        self.__init__(self.tutte_le_voci, self.anno, self.settimana_iso)

    def next(self):
        nuova_data = datetime.fromisocalendar(self.get_anno(), self.get_settimana(), 1) + timedelta(weeks=1)
        self.__init__(self.tutte_le_voci, nuova_data.isocalendar().year, nuova_data.isocalendar().week)

    def previous(self):
        nuova_data = datetime.fromisocalendar(self.get_anno(), self.get_settimana(), 1) - timedelta(weeks=1)
        self.__init__(self.tutte_le_voci, nuova_data.isocalendar().year, nuova_data.isocalendar().week)


class BilancioMensile:
    def __init__(self, voci: list[VoceDiBilancio], anno=datetime.today().year,
                 mese=datetime.today().month):
        self.costi = None
        self.ricavo = None
        self.utile = None
        self.anno = anno
        self.mese = mese
        self.tutte_le_voci = voci
        self.voci_mensili = self.__trova_voci_mensili()
        self.costi = self.get_costi()
        self.ricavo = self.get_ricavo()
        self.utile = self.get_utile()

    def __trova_voci_mensili(self):
        anno = self.get_anno()
        mese = self.get_mese()

        voci_date = []
        for voce in self.tutte_le_voci:
            primo_giorno = datetime(anno, mese, 1)
            ultimo_giorno = datetime(anno, mese, monthrange(anno, mese)[1])
            occorrenze = voce.occorrenze_in(primo_giorno, ultimo_giorno)
            for data in occorrenze:
                voci_date += [(voce.component, data, voce.is_entrata())]
        return voci_date

    def get_anno(self):
        return self.anno

    def get_mese(self):
        return self.mese

    def get_data_iniziale(self):
        return datetime(self.anno, self.mese, monthrange(self.anno, self.mese)[0])

    def get_data_finale(self):
        return datetime(self.anno, self.mese, monthrange(self.anno, self.mese)[1])

    def get_voci_mensili(self):
        return self.voci_mensili

    def get_utile(self):
        self.utile = 0

        def aggiungi_a_utile(
                x: tuple):
            if x[2]:
                self.utile += x[0].get_valore()
            else:
                self.utile -= x[0].get_valore()

        voci = self.get_voci_mensili()

        for voce in voci:
            aggiungi_a_utile(voce)
        return self.utile

    def get_entrate_mensili(self):
        return [(voce[0], voce[1]) for voce in self.get_voci_mensili() if voce[2]]

    def get_uscite_mensili(self):
        return [(voce[0], voce[1]) for voce in self.get_voci_mensili() if not voce[2]]

    def get_ricavo(self):
        self.ricavo = 0
        for entrata in self.get_entrate_mensili():
            self.ricavo += entrata[0].get_valore()
        return self.ricavo

    def get_costi(self):
        self.costi = 0
        for uscita in self.get_uscite_mensili():
            self.costi += uscita[0].get_valore()
        return self.costi

    def add(self, voce: VoceDiBilancio):
        self.tutte_le_voci.add(voce)
        self.__init__(self.tutte_le_voci, self.anno, self.mese)

    def remove(self, voce: VoceDiBilancio):
        self.tutte_le_voci.remove(voce)
        self.__init__(self.tutte_le_voci, self.anno, self.settimana_iso)

    def next(self):
        anno = self.get_anno()
        mese = self.get_mese()
        nuova_data = datetime(year=anno, month=mese, day=1) + timedelta(days=31)
        self.__init__(self.tutte_le_voci, nuova_data.year, nuova_data.month)

    def previous(self):
        anno = self.get_anno()
        mese = self.get_mese()
        nuova_data = datetime(year=anno, month=self.mese, day=1) - timedelta(days=1)
        self.__init__(self.tutte_le_voci, nuova_data.year, nuova_data.month)


def __ProvaInit():
    affitto = ComponenteGenerica(450, 'Affitto')
    trattore = ComponenteGenerica(2100, 'Trattore')
    semi = ComponenteGenerica(30, 'Semi')

    vdb = VoceDiBilancio(affitto, True, Periodicita.MENSILE, arg_periodicita=1, iterazioni=10,
                         data=datetime.today().replace(day=datetime.today().day - 1))
    vdb2 = VoceDiBilancio(affitto, True, Periodicita.MENSILE, arg_periodicita=2, iterazioni=10)
    vdb3 = VoceDiBilancio(trattore, False, Periodicita.NESSUNA,
                          data=datetime.today().replace(month=datetime.today().month - 1))
    vdb4 = VoceDiBilancio(semi, False, Periodicita.NESSUNA, data=datetime.today().replace(year=2100))
    vdb5 = VoceDiBilancio(semi, False, Periodicita.NESSUNA, data=datetime.today().replace(year=2000))
    bilancio = Bilancio()
    bilancio.aggiungi_elemento(vdb)
    bilancio.aggiungi_elemento(vdb2)
    bilancio.aggiungi_elemento(vdb3)
    bilancio.aggiungi_elemento(vdb4)
    bilancio.aggiungi_elemento(vdb5)
    for elemento in bilancio.get_voci():
        print(elemento)
    print('Voci ordinate prima occorrenza:')
    print('------------------------------------------')
    for elemento in bilancio.get_voci('po'):
        print(elemento)
    print('Voci ordinate ultima occorrenza:')
    print('------------------------------------------')
    for elemento in bilancio.get_voci('uo'):
        print(elemento)
        print('ultima occorrenza = ' + elemento.get_ultima_data().strftime("%Y-%m-%d"))


class Bilancio:
    def __init__(self):
        super(Bilancio, self).__init__()
        self.voci_di_bilancio = set()
        self.__caricaVoci()
        self.__modified = True
        self.voci_ordinate_data_iniziale = self.get_voci(ordine='po')
        self.voci_ordinate_data_finale = self.get_voci(ordine='uo')
        self.bilancio_corrente_sett = BilancioSettimanale(self.get_voci())
        self.bilancio_corrente_mens = BilancioMensile(self.get_voci())
        self.__modified = False

    def __caricaVoci(self):

        with open(pth_voci) as f:
            voci = json.load(f)
        for voce_jsn in voci:
            nome = voce_jsn['component']['nome']
            valore = voce_jsn['component']['valore']
            entrata = voce_jsn['entrata'] == 'True'
            periodicita = Periodicita(voce_jsn['periodicita'])
            arg_periodicita = voce_jsn['arg_periodicita']
            iterazioni = voce_jsn['iterazioni']
            data_date = datetime.strptime(voce_jsn['data'], '%Y/%m/%d')
            data_datetime = datetime(data_date.year, data_date.month, data_date.day)
            voce = VoceDiBilancio(ComponenteGenerica(valore, nome), entrata, periodicita, arg_periodicita, iterazioni,
                                  data_date)
            self.voci_di_bilancio.add(voce)

    def aggiungi_elemento(self, voce: VoceDiBilancio):
        if self.is_present_by_id(voce.get_id()):
            raise ValueError('Elemento già presente all\'interno del bilancio')
        self.voci_di_bilancio.add(voce)
        self.bilancio_corrente_sett.add(voce)
        self.bilancio_corrente_mens.add(voce)
        self.save_data(voce)
        self.__modified = True


    def rimuovi_elemento(self, voce: VoceDiBilancio):
        if self.is_present_by_id(voce.get_id()):
            self.voci_di_bilancio.remove(voce)
            self.__modified = True
            self.rimuoviDaJson(voce)
        else:
            raise ValueError('L\'elemento non è presente all\'interno del bilancio')

    def is_present_by_id(self, _id):
        voci = self.get_voci()
        for voce in voci:
            if voce.get_id() == _id:
                return True
        return False

    def get_voce_by_id(self, _id):
        voci = self.get_voci()
        for voce in voci:
            if voce.get_id() == _id:
                return voce
        raise ValueError('Non è stata trovata nessuna voce corrispondente all\'id indicato')

    @staticmethod
    def key_function_get_data(element):
        return element.get_data()

    @staticmethod
    def key_function_get_ultima_data(element):
        return element.get_ultima_data()

    def get_voci(self, ordine='nessun ordine'):
        """
        :param ordine: stringa che descrive come ordinare le voci: usare 'po' per prima occorrenza e 'uo' per ultima occorrenza
        :return: vettore di voci ordinate
        """
        if self.__modified and not ordine == 'nessun ordine':
            self.voci_ordinate_data_iniziale = sorted(self.voci_di_bilancio, key=lambda e: e.get_data())
            self.voci_ordinate_data_finale = sorted(self.voci_di_bilancio, key=lambda e: e.get_ultima_data())
            self.__modified = False
        match ordine:
            case 'po':
                return self.voci_ordinate_data_iniziale
            case 'uo':
                return self.voci_ordinate_data_finale
            case 'nessun ordine':
                return self.voci_di_bilancio
            case _:
                raise ValueError

    def get_bilancio_settimanale(self, anno=datetime.today().year, settimana_iso=datetime.today().isocalendar().week):
        self.bilancio_corrente_sett = BilancioSettimanale(self.get_voci(), anno, settimana_iso)
        return self.bilancio_corrente_sett

    def get_bilancio_mensile(self, anno=datetime.today().year, mese=datetime.today().month):
        self.bilancio_corrente_mens = BilancioMensile(self.get_voci(), anno, mese)
        return self.bilancio_corrente_mens

    def next_sett(self):
        self.bilancio_corrente_sett.next()

    def previous_sett(self):
        self.bilancio_corrente_sett.previous()

    def next_mens(self):
        self.bilancio_corrente_mens.next()

    def previous_mens(self):
        self.bilancio_corrente_mens.previous()

    def trova(self, nome_componente: str, data_iniziale_g_m_a: datetime, indice: int):
        voce = None
        indice += 1
        for i in range(indice):
            voce = next(v for v in self.get_voci('po') if
                        v.get_component.get_nome() is nome_componente and data_iniziale_g_m_a.date() is v.get_data())
        return voce

    def save_data(self, voce):
        with open(pth_voci) as f:
            voci = json.load(f)
            periodicita = voce.get_periodicita()
            nuovo = {
                "component": {
                     "nome": voce.component.get_nome(),
                     "valore": voce.get_valore()
                },
                "entrata": str(voce.is_entrata()),
                "periodicita": voce.get_periodicita().value,
                "arg_periodicita": voce.arg_periodicita,
                "iterazioni": voce.get_iterazioni(),
                "data": voce.get_data().date().strftime('%Y/%m/%d')
            }
            voci.append(nuovo)
        with open(pth_voci, 'w') as file:
            json.dump(voci, file, indent=4)

    def rimuoviDaJson(self, voce: VoceDiBilancio):
        with open(pth_voci) as f:
            data = json.load(f)
            cercato = {
                "component": {
                     "nome": voce.component.get_nome(),
                     "valore": voce.get_valore()
                },
                "entrata": str(voce.is_entrata()),
                "periodicita": voce.get_periodicita().value,
                "arg_periodicita": voce.arg_periodicita,
                "iterazioni": voce.get_iterazioni(),
                "data": voce.get_data().date().strftime('%Y/%m/%d')
            }
            if len(data) > 0:
                for i in range(len(data)):
                    if data[i] == cercato:
                        del data[i]
                        break
                # try:
                #     index = next(i for i in range(len(data)-1) if data[i] == cercato)
                #     del data[index]
                # except Exception as e:
                #     print(e)
            else:
                raise ValueError('Voce non trovata!')
        with open(pth_voci, 'w') as file:
                    json.dump(data, file, indent=4)

if __name__ == '__main__':
    # __ProvaInit()
    # __ProvaBilancioSettimanale()
    # __ProvaBilancioMensile()
    pass
