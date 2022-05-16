import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Progetto.home.view.main_interface import main_interface


class MainWindow(QMainWindow):
    def __init__(self, dipendente):
        QMainWindow.__init__(self)
        self.ui = main_interface()
        self.ui.setupUi(self, dipendente)
        self.show()

        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)

        self.ui.push_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homepage))
        self.ui.push_dipendenti.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dipendenti))
        self.ui.push_dipendenti.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_empty))

        self.ui.push_creanuovodipendente.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_crea_nuovo_dipendente))

        self.ui.push_pianodilavoro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pianodilavoro))

        self.ui.push_magazzino.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.magazzino))

        self.ui.push_clienti.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clienti))

        self.ui.push_contabilita.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.contabilita))

        self.ui.push_statistiche.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.statistiche))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(dipendente= None)
    sys.exit(app.exec())

