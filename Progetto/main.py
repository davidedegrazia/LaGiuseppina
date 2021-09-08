import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Progetto.dipendenti.view.main_interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.stackedWidget.setCurrentIndex(5)

        self.ui.push_dipendenti.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dipendenti))
        self.ui.push_dipendenti.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_empty))
        self.ui.push_visualizza.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_visualizza_dipendente))
        self.ui.push_creanuovodipendente.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_crea_nuovo_dipendente))

        self.ui.push_pianodilavoro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pianodilavoro))

        self.ui.push_magazzino.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.magazzino))

        self.ui.push_contabilita.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.contabilita))

        self.ui.push_statistiche.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.statistiche))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
