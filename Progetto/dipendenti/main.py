import sys
from PyQt5.QtWidgets import QApplication
from pyqt5_plugins.examplebutton import QtWidgets

from Progetto.dipendenti.view.Crea_nuovo_dipendente import Ui_Form
from Progetto.dipendenti.view.VistaDipendente import VistaDipendente


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())