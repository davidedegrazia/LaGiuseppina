from datetime import datetime

import parse
from PyQt5 import QtCore, QtGui, QtWidgets
from  parse import compile

import Progetto.contabilit√†.utils
from Progetto.contabilit√†.model.Bilancio import Bilancio
from Progetto.contabilit√†.model.VoceDiBilancio import Periodicita, VoceDiBilancio, ComponenteGenerica


class VistaVociDiBilancio(object):
    def __init__(self, bilancio):
        self.bilancio = bilancio
        self.periodicita_dict = {
            'Nessuna': Periodicita.NESSUNA,
            'Giornaliera': Periodicita.GIORNALIERA,
            'Settimanale': Periodicita.SETTIMANALE,
            'Mensile': Periodicita.MENSILE,
            'Annuale': Periodicita.ANNUALE
        }

    def setupUi(self, MainWindow, bilancio):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 616)
        MainWindow.setMaximumSize(QtCore.QSize(709, 670))
        MainWindow.setStyleSheet("border:none;"
                                 "background-color: rgb(235, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 40, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(12, 0, 50, 0)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_vocidibilancio = QtWidgets.QListWidget(self.frame_4)
        self.listWidget_vocidibilancio.setStyleSheet("background-color: rgb(255, 255, 255);"
                                                     "color: rgb(0, 0, 0);")
        self.listWidget_vocidibilancio.setObjectName("listWidget_vocidibilancio")
        self.horizontalLayout_2.addWidget(self.listWidget_vocidibilancio)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 12)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.push_visualizza = QtWidgets.QPushButton(self.frame_3)
        self.push_visualizza.setMinimumSize(QtCore.QSize(0, 25))
        self.push_visualizza.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                           "border-top-color: rgb(255, 0, 26);\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "border-radius: 12px;"
                                           "color: rgb(0, 0, 0);")
        self.push_visualizza.setObjectName("push_visualizza")
        self.verticalLayout_2.addWidget(self.push_visualizza)
        self.push_elimina = QtWidgets.QPushButton(self.frame_3)
        self.push_elimina.setMinimumSize(QtCore.QSize(0, 25))
        self.push_elimina.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                        "border-top-color: rgb(255, 0, 26);\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 12px;"
                                        "color: rgb(0, 0, 0);")
        self.push_elimina.setObjectName("push_elimina")
        self.verticalLayout_2.addWidget(self.push_elimina)
        self.push_creanuovavoce = QtWidgets.QPushButton(self.frame_3)
        self.push_creanuovavoce.setMinimumSize(QtCore.QSize(100, 0))
        self.push_creanuovavoce.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                              "border-top-color: rgb(255, 0, 26);\n"
                                              "background-color: rgb(0, 122, 254);\n"
                                              "border-radius: 17px;\n"
                                              "color: rgb(255, 255, 255);")
        self.push_creanuovavoce.setObjectName("push_creanuovavoce")
        self.verticalLayout_2.addWidget(self.push_creanuovavoce)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_vuota = QtWidgets.QWidget()
        self.page_vuota.setObjectName("page_vuota")
        self.stackedWidget.addWidget(self.page_vuota)
        self.page_visualizza_voce = QtWidgets.QWidget()
        self.page_visualizza_voce.setObjectName("page_visualizza_voce")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_visualizza_voce)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_nome_voce = QtWidgets.QLabel(self.page_visualizza_voce)
        self.label_nome_voce.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label_nome_voce.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                           "color: rgb(0,0,0);")
        self.label_nome_voce.setObjectName("label_nome_voce")
        self.verticalLayout_3.addWidget(self.label_nome_voce)
        self.label_prezzo_voce = QtWidgets.QLabel(self.page_visualizza_voce)
        self.label_prezzo_voce.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label_prezzo_voce.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                             "color: rgb(0,0,0);")
        self.label_prezzo_voce.setObjectName("label_prezzo_voce")
        self.verticalLayout_3.addWidget(self.label_prezzo_voce)
        self.label_entrata_voce = QtWidgets.QLabel(self.page_visualizza_voce)
        self.label_entrata_voce.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label_entrata_voce.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                              "color: rgb(0,0,0);")
        self.label_entrata_voce.setObjectName("label_entrata_voce")
        self.verticalLayout_3.addWidget(self.label_entrata_voce)
        self.label_periodicita_voce = QtWidgets.QLabel(self.page_visualizza_voce)
        self.label_periodicita_voce.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                                  "color: rgb(0,0,0);")
        self.label_periodicita_voce.setObjectName("label_periodicita_voce")
        self.verticalLayout_3.addWidget(self.label_periodicita_voce)
        self.label_num_iterazioni_voce = QtWidgets.QLabel(self.page_visualizza_voce)
        self.label_num_iterazioni_voce.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                                     "color: rgb(0,0,0);")
        self.label_num_iterazioni_voce.setObjectName("label_num_iterazioni_voce")
        self.verticalLayout_3.addWidget(self.label_num_iterazioni_voce)
        self.label_prima_iterazione_voce = QtWidgets.QLabel(self.page_visualizza_voce)
        self.label_prima_iterazione_voce.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                                       "color: rgb(0,0,0);")
        self.label_prima_iterazione_voce.setObjectName("label_prima_iterazione_voce")
        self.verticalLayout_3.addWidget(self.label_prima_iterazione_voce)
        self.stackedWidget.addWidget(self.page_visualizza_voce)
        self.page_crea_nuova_voce = QtWidgets.QWidget()
        self.page_crea_nuova_voce.setObjectName("page_crea_nuova_voce")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_crea_nuova_voce)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.page_crea_nuova_voce)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_7.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                   "color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.frame_bianco = QtWidgets.QFrame(self.page_crea_nuova_voce)
        self.frame_bianco.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 16px;\n"
                                        "")
        self.frame_bianco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bianco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bianco.setObjectName("frame_bianco")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_bianco)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_bianco)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(-1, 12, 200, 12)
        self.horizontalLayout_4.setSpacing(25)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                   "color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEdit_nome_voce = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_nome_voce.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_nome_voce.setStyleSheet("border-radius: 10px;\n"
                                              "background-color: rgb(235, 235, 235);"
                                              "color: rgb(0, 0, 0);")
        self.lineEdit_nome_voce.setObjectName("lineEdit_nome_voce")
        self.horizontalLayout_4.addWidget(self.lineEdit_nome_voce)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame_bianco)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(12, -1, 400, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_11.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.doubleSpinBox_prezzo_voce = QtWidgets.QDoubleSpinBox(self.frame_5)
        self.doubleSpinBox_prezzo_voce.setMinimumSize(QtCore.QSize(0, 25))
        self.doubleSpinBox_prezzo_voce.setMaximumSize(QtCore.QSize(100, 16777215))
        self.doubleSpinBox_prezzo_voce.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(235, 235, 235);"
                                                     "color: rgb(0, 0, 0);")
        self.doubleSpinBox_prezzo_voce.setObjectName("doubleSpinBox_prezzo_voce")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_prezzo_voce)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_bianco)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_entrata = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_entrata.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                            "color: rgb(0, 0, 0);")
        self.checkBox_entrata.setObjectName("checkBox_entrata")
        self.horizontalLayout_10.addWidget(self.checkBox_entrata)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.frame_bianco)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(-1, 8, 350, 8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        self.label_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_9.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                   "color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.comboBox_periodicita = QtWidgets.QComboBox(self.frame_9)
        self.comboBox_periodicita.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_periodicita.setStyleSheet("border-radius: 10px;\n"
                                                "background-color: rgb(235, 235, 235);"
                                                "color: rgb(0, 0, 0);")
        self.comboBox_periodicita.setObjectName("comboBox_periodicita")
        self.comboBox_periodicita.addItem("")
        self.comboBox_periodicita.addItem("")
        self.comboBox_periodicita.addItem("")
        self.comboBox_periodicita.addItem("")
        self.comboBox_periodicita.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_periodicita)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_bianco)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setContentsMargins(-1, -1, 350, -1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        self.label_10.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.label_10.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.spinBox_numero_iterazioni = QtWidgets.QSpinBox(self.frame_10)
        self.spinBox_numero_iterazioni.setMinimumSize(QtCore.QSize(0, 25))
        self.spinBox_numero_iterazioni.setMaximumSize(QtCore.QSize(80, 16777215))
        self.spinBox_numero_iterazioni.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(235, 235, 235);"
                                                     "color: rgb(0, 0, 0);")
        self.spinBox_numero_iterazioni.setObjectName("spinBox_numero_iterazioni")
        self.horizontalLayout_6.addWidget(self.spinBox_numero_iterazioni)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.frame_8 = QtWidgets.QFrame(self.frame_bianco)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setContentsMargins(-1, -1, 350, -1)
        self.horizontalLayout_9.setSpacing(40)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setMaximumSize(QtCore.QSize(350, 16777215))
        self.label_2.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                   "color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.dateEdit_prima_iterazione = QtWidgets.QDateEdit(self.frame_8)
        self.dateEdit_prima_iterazione.setMinimumSize(QtCore.QSize(0, 25))
        self.dateEdit_prima_iterazione.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(235, 235, 235);"
                                                     "color: rgb(0, 0, 0);")
        self.dateEdit_prima_iterazione.setDate(QtCore.QDate(2022, 6, 1))
        self.dateEdit_prima_iterazione.setObjectName("dateEdit_prima_iterazione")
        self.horizontalLayout_9.addWidget(self.dateEdit_prima_iterazione)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.frame_11 = QtWidgets.QFrame(self.frame_bianco)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setContentsMargins(400, 0, 110, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_salva_voce = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_salva_voce.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_salva_voce.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                                 "border-top-color: rgb(255, 0, 26);\n"
                                                 "background-color: rgb(0, 122, 254);\n"
                                                 "border-radius: 17px;\n"
                                                 "color: rgb(255, 255, 255);")
        self.pushButton_salva_voce.setObjectName("pushButton_salva_voce")
        self.horizontalLayout_8.addWidget(self.pushButton_salva_voce)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.verticalLayout_6.addWidget(self.frame_bianco)
        self.stackedWidget.addWidget(self.page_crea_nuova_voce)
        self.page_vuota_2 = QtWidgets.QWidget()
        self.page_vuota_2.setObjectName("page_vuota_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_vuota_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget.addWidget(self.page_vuota_2)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.caricaLista()
        try:
            self.visualizza(self.bilancio.get_voci('po')[0])
        except IndexError:
            self.clearLabels()
            pass
        except Exception as e:
            pass
        self.pushButton_salva_voce.clicked.connect(lambda: self.salva())
        self.push_visualizza.clicked.connect(lambda: self.visualizzaSelezionato())
        self.push_creanuovavoce.clicked.connect(lambda: self.creaNuovaVoce())
        self.push_elimina.clicked.connect(lambda: self.eliminaSelezionato())
        # bilancio = Bilancio()
        # # #oggi = datetime.datetime.today
        # # v1 = VoceDiBilancio(ComponenteGenerica(5000, 'Pepe'), False, Periodicita.SETTIMANALE, arg_periodicita=1,
        # #                     iterazioni=15)
        # # v2 = VoceDiBilancio(ComponenteGenerica(150000, 'Comodato d\'uso'), True, Periodicita.ANNUALE, arg_periodicita=1,
        # #                     iterazioni=16)
        # # v3 = VoceDiBilancio(ComponenteGenerica(30000, 'Cozze'), True, Periodicita.NESSUNA, arg_periodicita=1,
        # #                     data=oggi.replace(day=28))
        # # try:
        # #     v4 = VoceDiBilancio(ComponenteGenerica(500, 'Software vari'), False, Periodicita.GIORNALIERA,
        # #                         arg_periodicita=1,
        # #                         data=oggi.replace(day=datetime.datetime.today().day + 1))
        # # except Exception:
        # #     try:
        # #         v4 = VoceDiBilancio(ComponenteGenerica(500, 'Software vari'), False, Periodicita.GIORNALIERA,
        # #                             arg_periodicita=1,
        # #                             data=oggi.replace(day=1, month=datetime.datetime.today().month + 1))
        # #     except Exception:
        # #         v4 = VoceDiBilancio(ComponenteGenerica(500, 'Software vari'), False, Periodicita.GIORNALIERA,
        # #                             arg_periodicita=1,
        # #                             data=oggi.replace(day=1, month=1, year=datetime.datetime.today().year + 1))
        # # vettore = [v1, v2, v3, v4]
        # # for v in vettore:
        # #     bilancio.aggiungi_elemento(v)
        # for voce in bilancio.get_voci('po'):
        #     self.listWidget_vocidibilancio.addItem(voce.component.get_nome())

        #self.salva()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_visualizza.setText(_translate("MainWindow", "Visualizza"))
        self.push_elimina.setText(_translate("MainWindow", "Elimina"))
        self.push_creanuovavoce.setText(_translate("MainWindow", "Crea nuova \n"
                                                                 " voce"))
        self.label_nome_voce.setText(_translate("MainWindow", "Nome:"))
        self.label_prezzo_voce.setText(_translate("MainWindow", "Prezzo:"))
        self.label_entrata_voce.setText(_translate("MainWindow", "Entrata?: "))
        self.label_periodicita_voce.setText(_translate("MainWindow", "Periodicit√†: "))
        self.label_num_iterazioni_voce.setText(_translate("MainWindow", "Numero iterazioni: "))
        self.label_prima_iterazione_voce.setText(_translate("MainWindow", "Data prima iterazione:"))
        self.label_7.setText(_translate("MainWindow", "Crea una nuova voce di bilancio!"))
        self.label_8.setText(_translate("MainWindow", "Nome: "))
        self.label_11.setText(_translate("MainWindow", "Prezzo:"))
        self.checkBox_entrata.setText(_translate("MainWindow", "Entrata"))
        self.label_9.setText(_translate("MainWindow", "Periodicit√†:"))
        self.comboBox_periodicita.setItemText(0, _translate("MainWindow", "Nessuna"))
        self.comboBox_periodicita.setItemText(1, _translate("MainWindow", "Giornaliera"))
        self.comboBox_periodicita.setItemText(2, _translate("MainWindow", "Settimanale"))
        self.comboBox_periodicita.setItemText(3, _translate("MainWindow", "Mensile"))
        self.comboBox_periodicita.setItemText(4, _translate("MainWindow", "Annuale"))
        self.label_10.setText(_translate("MainWindow", "Numero iterazioni:"))
        self.label_2.setText(_translate("MainWindow", "Data prima iterazione:"))
        self.pushButton_salva_voce.setText(_translate("MainWindow", "Salva voce"))

    def salva(self):
        nome = self.lineEdit_nome_voce.text()
        prezzo_cent = int(self.doubleSpinBox_prezzo_voce.value()) * 100
        entrata = self.checkBox_entrata.isChecked()
        periodicita_txt = self.comboBox_periodicita.currentText()
        periodicita = self.periodicita_dict[periodicita_txt]
        numero_iterazioni = self.spinBox_numero_iterazioni.value()
        data = self.dateEdit_prima_iterazione.date().toPyDate()
        dt = datetime(data.year, data.month, data.day)
        try:
            voce = VoceDiBilancio(ComponenteGenerica(prezzo_cent, nome), entrata, periodicita, iterazioni=numero_iterazioni, data = dt)
            self.bilancio.aggiungi_elemento(voce)
            self.caricaLista()
            self.visualizza(voce)
        except ValueError as ve:
            print(ve)

    def caricaLista(self):
        voci = self.bilancio.get_voci('po')
        self.listWidget_vocidibilancio.clear()
        for voce in voci:
            self.listWidget_vocidibilancio.addItem(voce.component.get_nome() + ' ' + str(voce.data.strftime("%Y/%m/%d")))

    def trovaSelezionato(self)->VoceDiBilancio:
        indice = self.listWidget_vocidibilancio.selectedIndexes()[0].row()
        voce = self.bilancio.get_voci('po')[indice]
        return voce

    def visualizzaSelezionato(self):
        try:
            voce = self.trovaSelezionato()
            self.visualizza(voce)
        except IndexError:
            pass

    def visualizza(self, voce):
        self.stackedWidget.setCurrentIndex(1)
        self.label_nome_voce.setText('Nome: ' + voce.component.get_nome())
        self.label_prezzo_voce.setText('Prezzo: ' +Progetto.contabilit√†.utils.centToEuroString(voce.get_valore()))
        if voce.is_entrata():
            entrata_str = 'S√¨'
        else:
            entrata_str = 'No'
        self.label_entrata_voce.setText('Entrata?: ' + entrata_str)
        self.label_periodicita_voce.setText('Periodicit√†: ' + str(voce.get_periodicita()))
        if voce.is_eterno():
            self.label_num_iterazioni_voce.setText('Voce eterna')
        else:
            self.label_num_iterazioni_voce.setText('Numero iterazioni: ' + str(voce.get_iterazioni()))
        self.label_prima_iterazione_voce.setText('Data prima occorrenza: ' + voce.get_data().strftime('%d/%m/%Y'))

    def clearLabels(self):
        self.label_nome_voce.setText('Nessuna voce presente')
        self.label_prezzo_voce.setText('Cliccare \'Crea ')
        self.label_entrata_voce.setText('')
        self.label_periodicita_voce.setText('')
        self.label_num_iterazioni_voce.setText('')
        self.label_prima_iterazione_voce.setText('')

    def creaNuovaVoce(self):
        self.stackedWidget.setCurrentIndex(2)

    def salvaVoce(self, voce):
        self.bilancio.aggiungi_elemento(voce)
        self.caricaLista()
        self.visualizza(voce)

    def eliminaSelezionato(self):
        try:
            indice =  self.listWidget_vocidibilancio.selectedIndexes()[0].row()
            voci = self.bilancio.get_voci('po')
            voce = voci[indice]
            self.bilancio.rimuovi_elemento(voce)
            self.caricaLista()
        except IndexError as e:
            print(e)
