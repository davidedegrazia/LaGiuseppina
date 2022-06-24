import datetime
import json

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QListView, QMessageBox, QWidget, QVBoxLayout, QFrame, QLabel, QPushButton

from Progetto.dipendenti.controller.ControlloreDipendente import ControlloreDipendente
from Progetto.dipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti
from Progetto.listaprodotti.controller.ControlloreListaProdottiSalvati import ControlloreListaProdottiSalvati
from Progetto.listaprodotti.view.VistaProdottiMagazzino import VistaProdottiMagazzino
from Progetto.pianodilavoro.controller.ControllorePianoLavoro import ControllorePianoLavoro
from Progetto.pianodilavoro.view.VistaPianoLavoro import VistaPianoLavoro
from Progetto.clienti.controller.ControlloreListaOrdinazioni import ControlloreListaOrdinazioni
from Progetto.contabilità.view.VistaVociDiBilancio import VistaVociDiBilancio
from Progetto.contabilità.model.VoceDiBilancio import VoceDiBilancio, ComponenteGenerica, Periodicita
from Progetto.contabilità.model.Bilancio import Bilancio
from Progetto.contabilità.utils import centToEuroString


class main_interface(object):
    def __init__(self):
        self.vista_pianolavoro = VistaPianoLavoro()
        self.vista_listaprodotti = VistaProdottiMagazzino()
        self.bilancio = Bilancio()
        self.vista_vocidibilancio = VistaVociDiBilancio(self.bilancio)


    def vista_lista_prodotti(self):
        self.window = QtWidgets.QMainWindow()
        self.vista_listaprodotti.setupUi(self.window)
        self.window.show()

    def vista_piano_lavoro(self):
        self.window = QtWidgets.QMainWindow()
        self.vista_pianolavoro.setupUi(self.window)
        self.window.show()

    def vista_voci_di_bilancio(self):
        self.window = QtWidgets.QMainWindow()
        self.vista_vocidibilancio.setupUi(self.window, self.bilancio)
        self.window.show()

    def setupUi(self, MainWindow, dipendente):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1203, 527)
        MainWindow.setStyleSheet("border: none\n"
                                 "rgb(0, 0, 0)\n"
                                 "\n"
                                 "")
        MainWindow.setStyleSheet("background-color: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, -1, 12)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.banda_arancione = QtWidgets.QFrame(self.centralwidget)
        self.banda_arancione.setMaximumSize(QtCore.QSize(16777215, 55))
        self.banda_arancione.setSizeIncrement(QtCore.QSize(8, 0))
        self.banda_arancione.setStyleSheet("background-color: rgb(245, 148, 1);\n"
                                           "border-radius: 16px;\n"
                                           "")
        self.banda_arancione.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.banda_arancione.setFrameShadow(QtWidgets.QFrame.Plain)
        self.banda_arancione.setLineWidth(0)
        self.banda_arancione.setMidLineWidth(0)
        self.banda_arancione.setObjectName("banda_arancione")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.banda_arancione)
        self.horizontalLayout.setContentsMargins(-1, 8, -1, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.push_home = QPushButton(self.banda_arancione)
        self.push_home.setObjectName(u"push_home")
        self.push_home.setMaximumSize(QSize(60, 16777215))
        self.push_home.setStyleSheet(u"COLOR: rgb(255, 255, 255);\n"
                                     "font: 600 18pt \"SF Pro\";")

        self.horizontalLayout.addWidget(self.push_home)
        #self.home = QtWidgets.QLabel(self.banda_arancione)
        #self.home.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
        #                        "font: 600 18pt \"SF Pro\";")
        #self.home.setObjectName("home")
        #self.horizontalLayout.addWidget(self.home, 0, QtCore.Qt.AlignLeft)
        self.la_giuseppina = QtWidgets.QLabel(self.banda_arancione)
        self.la_giuseppina.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                         "font: 650 35pt \"SF Pro\";")
        self.la_giuseppina.setObjectName("la_giuseppina")
        self.horizontalLayout.addWidget(self.la_giuseppina, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.banda_arancione)
        self.central_frame = QtWidgets.QFrame(self.centralwidget)
        self.central_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central_frame.setLineWidth(0)
        self.central_frame.setObjectName("central_frame")
        self.central_frame.setStyleSheet("border: none")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(13)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu_e_data = QtWidgets.QFrame(self.central_frame)
        self.menu_e_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_e_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_e_data.setLineWidth(0)
        self.menu_e_data.setObjectName("menu_e_data")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_e_data)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_blu = QtWidgets.QFrame(self.menu_e_data)
        self.frame_blu.setStyleSheet("background-color: rgb(0, 143, 248);\n"
                                     "border-radius:18px;")
        self.frame_blu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_blu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_blu.setLineWidth(0)
        self.frame_blu.setObjectName("frame_blu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_blu)
        self.verticalLayout_3.setContentsMargins(14, 20, -1, 20)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.push_dipendenti = QtWidgets.QPushButton(self.frame_blu)
        self.push_dipendenti.setMinimumSize(QtCore.QSize(0, 40))
        self.push_dipendenti.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                           "font: 600 18pt \"SF Pro\";")
        self.push_dipendenti.setObjectName("push_dipendenti")
        self.verticalLayout_3.addWidget(self.push_dipendenti, 0, QtCore.Qt.AlignLeft)
        self.push_pianodilavoro = QtWidgets.QPushButton(self.frame_blu)
        self.push_pianodilavoro.setMinimumSize(QtCore.QSize(0, 40))
        self.push_pianodilavoro.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                              "font: 600 18pt \"SF Pro\";")
        self.push_pianodilavoro.setObjectName("push_pianodilavoro")
        self.verticalLayout_3.addWidget(self.push_pianodilavoro, 0, QtCore.Qt.AlignLeft)
        self.push_magazzino = QtWidgets.QPushButton(self.frame_blu)
        self.push_magazzino.setMinimumSize(QtCore.QSize(0, 40))
        self.push_magazzino.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                          "font: 600 18pt \"SF Pro\";")
        self.push_magazzino.setObjectName("push_magazzino")
        self.verticalLayout_3.addWidget(self.push_magazzino, 0, QtCore.Qt.AlignLeft)
        self.push_clienti = QtWidgets.QPushButton(self.frame_blu)
        self.push_clienti.setMinimumSize(QtCore.QSize(0, 40))
        self.push_clienti.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                        "font: 600 18pt \"SF Pro\";")
        self.push_clienti.setObjectName("push_clienti")
        self.verticalLayout_3.addWidget(self.push_clienti, 0, QtCore.Qt.AlignLeft)
        self.push_contabilita = QtWidgets.QPushButton(self.frame_blu)
        self.push_contabilita.setMinimumSize(QtCore.QSize(0, 40))
        self.push_contabilita.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                            "font: 600 18pt \"SF Pro\";")
        self.push_contabilita.setObjectName("push_contabilita")
        self.verticalLayout_3.addWidget(self.push_contabilita, 0, QtCore.Qt.AlignLeft)
        self.push_statistiche = QtWidgets.QPushButton(self.frame_blu)
        self.push_statistiche.setMinimumSize(QtCore.QSize(0, 40))
        self.push_statistiche.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                            "font: 600 18pt \"SF Pro\";")
        self.push_statistiche.setObjectName("push_statistiche")
        self.verticalLayout_3.addWidget(self.push_statistiche, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.frame_blu, 0, QtCore.Qt.AlignLeft)
        self.frame_celeste = QtWidgets.QFrame(self.menu_e_data)
        self.frame_celeste.setMinimumSize(QtCore.QSize(183, 0))
        self.frame_celeste.setMaximumSize(QtCore.QSize(180, 146))
        self.frame_celeste.setStyleSheet("\n"
                                         "background-color: rgb(126, 221, 255);\n"
                                         "border-radius: 17px;")
        self.frame_celeste.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_celeste.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_celeste.setObjectName("frame_celeste")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_celeste)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.giorno = QtWidgets.QLabel("Giri", self.frame_celeste)
        self.giorno.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                  "font: 600 55pt \"SF Pro\";")
        self.giorno.setObjectName("giorno")

        self.verticalLayout_4.addWidget(self.giorno, 0, QtCore.Qt.AlignHCenter)
        self.mese = QtWidgets.QLabel(self.frame_celeste)
        self.mese.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                "font: 600 30pt \"SF Pro\";")
        self.mese.setObjectName("mese")
        self.verticalLayout_4.addWidget(self.mese, 0, QtCore.Qt.AlignHCenter)
        self.anno = QtWidgets.QLabel(self.frame_celeste)
        self.anno.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
                                "font: 600 38pt \"SF Pro\";")
        self.anno.setObjectName("anno")
        self.verticalLayout_4.addWidget(self.anno, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_celeste)
        self.horizontalLayout_2.addWidget(self.menu_e_data, 0, QtCore.Qt.AlignLeft)
        self.main_frame = QtWidgets.QFrame(self.central_frame)
        self.main_frame.setStyleSheet("border-radius: 18px;\n"
                                      "background-color: rgb(235, 235, 235);\n"
                                      "")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setLineWidth(0)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_frame)
        self.stackedWidget.setStyleSheet("color: rgb(0, 0, 0);"
                                         "border-radius: 18px;"
                                         "background-color: rgb(235, 235, 235);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.verticalLayout_54 = QVBoxLayout(self.homepage)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(25, 30, 25, 700)
        self.verticalLayout_54.setSpacing(35)
        self.label_tit_homepage = QLabel(self.homepage)
        self.label_tit_homepage.setObjectName(u"label_tit_homepage")
        self.label_tit_homepage.setMaximumSize(QSize(16777215, 80))
        self.label_tit_homepage.setStyleSheet(u"\n"
                                              "font: 600 36pt \"SF Pro\";\n"
                                              "color: rgb(0, 0, 0);\n"
                                              "")

        self.verticalLayout_54.addWidget(self.label_tit_homepage)

        self.label_descrizione_sito = QLabel(self.homepage)
        self.label_descrizione_sito.setObjectName(u"label_descrizione_sito")
        self.label_descrizione_sito.setStyleSheet(u"font: 300 22pt \"SF Pro\";\n"
                                                  "color: rgb(0, 0, 0);\n"
                                                  "")

        self.verticalLayout_54.addWidget(self.label_descrizione_sito)

        self.stackedWidget.addWidget(self.homepage)
        self.dipendenti = QtWidgets.QWidget()
        self.dipendenti.setStyleSheet("")
        self.dipendenti.setObjectName("dipendenti")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dipendenti)
        self.verticalLayout_6.setContentsMargins(15, 10, 0, 0)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_listadeidipendenti = QtWidgets.QFrame(self.dipendenti)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_listadeidipendenti.sizePolicy().hasHeightForWidth())
        self.frame_listadeidipendenti.setSizePolicy(sizePolicy)
        self.frame_listadeidipendenti.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_listadeidipendenti.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_listadeidipendenti.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_listadeidipendenti.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_listadeidipendenti.setLineWidth(-1)
        self.frame_listadeidipendenti.setObjectName("frame_listadeidipendenti")
        self.frame_listadeidipendenti_2 = QtWidgets.QLabel(self.frame_listadeidipendenti)
        self.frame_listadeidipendenti_2.setGeometry(QtCore.QRect(0, 0, 391, 31))
        self.frame_listadeidipendenti_2.setMaximumSize(QtCore.QSize(391, 31))
        self.frame_listadeidipendenti_2.setStyleSheet("\n"
                                                      "font: 600 36pt \"SF Pro\";")
        self.frame_listadeidipendenti_2.setObjectName("frame_listadeidipendenti_2")
        self.verticalLayout_6.addWidget(self.frame_listadeidipendenti)
        self.frame_4 = QtWidgets.QFrame(self.dipendenti)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_list_and_buttons = QtWidgets.QFrame(self.frame_4)
        self.frame_list_and_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_list_and_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_list_and_buttons.setObjectName("frame_list_and_buttons")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_list_and_buttons)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_list = QtWidgets.QFrame(self.frame_list_and_buttons)
        self.frame_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_list.setObjectName("frame_list")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_list)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_13 = QtWidgets.QFrame(self.frame_list)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.listWidget_dipendenti = QListView(self.frame_13)
        self.listWidget_dipendenti.setGeometry(QtCore.QRect(10, 10, 771, 411))
        self.listWidget_dipendenti.setMaximumSize(QtCore.QSize(831, 411))
        self.listWidget_dipendenti.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "border-radius:0px;")
        self.listWidget_dipendenti.setObjectName("listWidget_dipendenti")

        self.verticalLayout_8.addWidget(self.frame_13)
        self.horizontalLayout_4.addWidget(self.frame_list)
        self.frame_15 = QtWidgets.QFrame(self.frame_list_and_buttons)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.push_visualizza = QtWidgets.QPushButton(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_visualizza.sizePolicy().hasHeightForWidth())
        self.push_visualizza.setSizePolicy(sizePolicy)
        self.push_visualizza.setMinimumSize(QtCore.QSize(120, 41))
        self.push_visualizza.setMaximumSize(QtCore.QSize(120, 16777215))
        self.push_visualizza.setBaseSize(QtCore.QSize(0, 12))
        self.push_visualizza.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                           "border-top-color: rgb(255, 0, 26);\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "border-radius: 17px;")
        self.push_visualizza.setIconSize(QtCore.QSize(0, 0))
        self.push_visualizza.setObjectName("push_visualizza")
        self.verticalLayout_9.addWidget(self.push_visualizza, 0, QtCore.Qt.AlignHCenter)
        self.push_modifica = QtWidgets.QPushButton(self.frame_15)
        self.push_modifica.setMinimumSize(QtCore.QSize(120, 41))
        self.push_modifica.setMaximumSize(QtCore.QSize(120, 16777215))
        self.push_modifica.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 17px;")
        self.push_modifica.setObjectName("push_modifica")
        self.verticalLayout_9.addWidget(self.push_modifica, 0, QtCore.Qt.AlignHCenter)
        self.push_elimina = QtWidgets.QPushButton(self.frame_15)
        self.push_elimina.setMinimumSize(QtCore.QSize(120, 41))
        self.push_elimina.setMaximumSize(QtCore.QSize(120, 16777215))
        self.push_elimina.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 17px;")
        self.push_elimina.setObjectName("push_elimina")
        self.verticalLayout_9.addWidget(self.push_elimina, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.frame_15)
        self.frame_new_dipendente = QtWidgets.QFrame(self.frame_list_and_buttons)
        self.frame_new_dipendente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_new_dipendente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_new_dipendente.setObjectName("frame_new_dipendente")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_new_dipendente)
        self.verticalLayout_7.setContentsMargins(0, 0, 26, 0)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.push_creanuovodipendente = QtWidgets.QPushButton(self.frame_new_dipendente)
        self.push_creanuovodipendente.setMinimumSize(QtCore.QSize(155, 60))
        self.push_creanuovodipendente.setMaximumSize(QtCore.QSize(155, 16777215))
        self.push_creanuovodipendente.setStyleSheet("font: 700 17pt \"Apple SD Gothic Neo\";\n"
                                                    "background-color: rgb(255, 255, 255);\n"
                                                    "border-radius: 17px;\n"
                                                    "background-color: rgba(0, 122, 255, 204);\n"
                                                    "color: rgb(255, 255, 255);")
        self.push_creanuovodipendente.setObjectName("push_creanuovodipendente")
        self.verticalLayout_7.addWidget(self.push_creanuovodipendente, 0,
                                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_4.addWidget(self.frame_new_dipendente)
        self.horizontalLayout_3.addWidget(self.frame_list_and_buttons)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.widget = QtWidgets.QWidget(self.dipendenti)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_empty = QtWidgets.QWidget()
        self.page_empty.setObjectName("page_empty")
        self.stackedWidget_2.addWidget(self.page_empty)
        self.page_crea_nuovo_dipendente = QtWidgets.QWidget()
        self.page_crea_nuovo_dipendente.setObjectName("page_crea_nuovo_dipendente")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_crea_nuovo_dipendente)
        self.verticalLayout_10.setContentsMargins(7, 2, 20, 16)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_scritta = QtWidgets.QFrame(self.page_crea_nuovo_dipendente)
        self.frame_scritta.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_scritta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_scritta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_scritta.setObjectName("frame_scritta")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_scritta)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_scritta = QtWidgets.QLabel(self.frame_scritta)
        self.label_scritta.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_scritta.setStyleSheet("font: 800 22pt \"Apple SD Gothic Neo\";")
        self.label_scritta.setObjectName("label_scritta")
        self.verticalLayout_11.addWidget(self.label_scritta)
        self.verticalLayout_10.addWidget(self.frame_scritta)
        self.frame_white = QtWidgets.QFrame(self.page_crea_nuovo_dipendente)
        self.frame_white.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 16px;\n"
                                       "")
        self.frame_white.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white.setObjectName("frame_white")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_white)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_nome = QtWidgets.QFrame(self.frame_white)
        self.frame_nome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_nome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_nome.setObjectName("frame_nome")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_nome)
        self.horizontalLayout_6.setContentsMargins(-1, 0, 200, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_nome = QtWidgets.QLabel(self.frame_nome)
        self.label_nome.setStyleSheet("\n"
                                      "font: 400 17pt \"SF Pro\";")
        self.label_nome.setObjectName("label_nome")
        self.horizontalLayout_6.addWidget(self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.frame_nome)
        self.lineEdit_nome.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_nome.setStyleSheet("border-radius: 10px;\n"
                                         "background-color: rgb(235, 235, 235);")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.horizontalLayout_6.addWidget(self.lineEdit_nome)
        self.verticalLayout_12.addWidget(self.frame_nome)
        self.frame_ore_settimanali = QtWidgets.QFrame(self.frame_white)
        self.frame_ore_settimanali.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ore_settimanali.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ore_settimanali.setObjectName("frame_ore_settimanali")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_ore_settimanali)
        self.horizontalLayout_10.setContentsMargins(-1, -1, 472, -1)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_oresettimanali = QtWidgets.QLabel(self.frame_ore_settimanali)
        self.label_oresettimanali.setStyleSheet("\n"
                                                "font: 400 17pt \"SF Pro\";")
        self.label_oresettimanali.setObjectName("label_oresettimanali")
        self.horizontalLayout_10.addWidget(self.label_oresettimanali)
        self.spinBox_oresettimanali = QtWidgets.QSpinBox(self.frame_ore_settimanali)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_oresettimanali.sizePolicy().hasHeightForWidth())
        self.spinBox_oresettimanali.setSizePolicy(sizePolicy)
        self.spinBox_oresettimanali.setMinimumSize(QtCore.QSize(60, 30))
        self.spinBox_oresettimanali.setStyleSheet("border-radius: 10px;\n"
                                                  "background-color: rgb(235, 235, 235);")
        self.spinBox_oresettimanali.setObjectName("spinBox_oresettimanali")
        self.horizontalLayout_10.addWidget(self.spinBox_oresettimanali)
        self.verticalLayout_12.addWidget(self.frame_ore_settimanali)
        self.frame_paga_ad_ora = QtWidgets.QFrame(self.frame_white)
        self.frame_paga_ad_ora.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_paga_ad_ora.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_paga_ad_ora.setObjectName("frame_paga_ad_ora")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_paga_ad_ora)
        self.horizontalLayout_9.setContentsMargins(-1, -1, 472, -1)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_pagaadora = QtWidgets.QLabel(self.frame_paga_ad_ora)
        self.label_pagaadora.setStyleSheet("\n"
                                           "font: 400 17pt \"SF Pro\";")
        self.label_pagaadora.setObjectName("label_pagaadora")
        self.horizontalLayout_9.addWidget(self.label_pagaadora)
        self.spinBox_pagaadora = QtWidgets.QSpinBox(self.frame_paga_ad_ora)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_pagaadora.sizePolicy().hasHeightForWidth())
        self.spinBox_pagaadora.setSizePolicy(sizePolicy)
        self.spinBox_pagaadora.setMinimumSize(QtCore.QSize(60, 30))
        self.spinBox_pagaadora.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(235, 235, 235);")
        self.spinBox_pagaadora.setObjectName("spinBox_pagaadora")
        self.horizontalLayout_9.addWidget(self.spinBox_pagaadora)
        self.verticalLayout_12.addWidget(self.frame_paga_ad_ora)
        self.frame_tipodicontratto = QtWidgets.QFrame(self.frame_white)
        self.frame_tipodicontratto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tipodicontratto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tipodicontratto.setObjectName("frame_tipodicontratto")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_tipodicontratto)
        self.horizontalLayout_8.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_tipodicontratto = QtWidgets.QLabel(self.frame_tipodicontratto)
        self.label_tipodicontratto.setStyleSheet("\n"
                                                 "font: 400 17pt \"SF Pro\";")
        self.label_tipodicontratto.setObjectName("label_tipodicontratto")
        self.horizontalLayout_8.addWidget(self.label_tipodicontratto)
        self.lineEdit_tipodicontratto = QtWidgets.QLineEdit(self.frame_tipodicontratto)
        self.lineEdit_tipodicontratto.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_tipodicontratto.setStyleSheet("border-radius: 10px;\n"
                                                    "background-color: rgb(235, 235, 235);")
        self.lineEdit_tipodicontratto.setObjectName("lineEdit_tipodicontratto")
        self.horizontalLayout_8.addWidget(self.lineEdit_tipodicontratto)
        self.verticalLayout_12.addWidget(self.frame_tipodicontratto)
        self.frame_email = QtWidgets.QFrame(self.frame_white)
        self.frame_email.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_email.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_email.setObjectName("frame_email")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_email)
        self.horizontalLayout_7.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_email = QtWidgets.QLabel(self.frame_email)
        self.label_email.setStyleSheet("\n"
                                       "font: 400 17pt \"SF Pro\";")
        self.label_email.setObjectName("label_email")
        self.horizontalLayout_7.addWidget(self.label_email)
        self.lineEdit_email = QtWidgets.QLineEdit(self.frame_email)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_email.setStyleSheet("border-radius: 10px;\n"
                                          "background-color: rgb(235, 235, 235);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_7.addWidget(self.lineEdit_email)
        self.verticalLayout_12.addWidget(self.frame_email)
        self.frame_telefono = QtWidgets.QFrame(self.frame_white)
        self.frame_telefono.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_telefono.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_telefono.setObjectName("frame_telefono")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_telefono)
        self.horizontalLayout_11.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_telefono = QtWidgets.QLabel(self.frame_telefono)
        self.label_telefono.setStyleSheet("\n"
                                          "font: 400 17pt \"SF Pro\";")
        self.label_telefono.setObjectName("label_telefono")
        self.horizontalLayout_11.addWidget(self.label_telefono)
        self.lineEdit_telefono = QtWidgets.QLineEdit(self.frame_telefono)
        self.lineEdit_telefono.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_telefono.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(235, 235, 235);")
        self.lineEdit_telefono.setObjectName("lineEdit_telefono")
        self.horizontalLayout_11.addWidget(self.lineEdit_telefono)
        self.verticalLayout_12.addWidget(self.frame_telefono)
        self.frame_salva_dipendenti = QtWidgets.QFrame(self.frame_white)
        self.frame_salva_dipendenti.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salva_dipendenti.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salva_dipendenti.setObjectName("frame_salva_dipendenti")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_salva_dipendenti)
        self.horizontalLayout_12.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_salva_dipendenti = QtWidgets.QPushButton(self.frame_salva_dipendenti)
        self.pushButton_salva_dipendenti.setMinimumSize(QtCore.QSize(0, 36))
        self.pushButton_salva_dipendenti.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_salva_dipendenti.setStyleSheet("font: 700 14pt \"Apple SD Gothic Neo\";\n"
                                                       "background-color: rgb(255, 255, 255);\n"
                                                       "border-radius: 11px;\n"
                                                       "background-color: rgba(0, 122, 255, 204);\n"
                                                       "color: rgb(255, 255, 255);")
        self.pushButton_salva_dipendenti.setObjectName("pushButton_salva_dipendenti")
        self.horizontalLayout_12.addWidget(self.pushButton_salva_dipendenti)
        self.verticalLayout_12.addWidget(self.frame_salva_dipendenti)
        self.verticalLayout_10.addWidget(self.frame_white)
        self.stackedWidget_2.addWidget(self.page_crea_nuovo_dipendente)
        self.page_visualizza_dipendente = QtWidgets.QWidget()
        self.page_visualizza_dipendente.setObjectName("page_visualizza_dipendente")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.page_visualizza_dipendente)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.frame_visualizza_nuovo_dipendente = QtWidgets.QFrame(self.page_visualizza_dipendente)
        self.frame_visualizza_nuovo_dipendente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_visualizza_nuovo_dipendente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_visualizza_nuovo_dipendente.setObjectName("frame_visualizza_nuovo_dipendente")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_visualizza_nuovo_dipendente)
        self.verticalLayout_30.setContentsMargins(0, 0, 13, 6)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_scritta_dipendente = QtWidgets.QFrame(self.frame_visualizza_nuovo_dipendente)
        self.frame_scritta_dipendente.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frame_scritta_dipendente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_scritta_dipendente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_scritta_dipendente.setObjectName("frame_scritta_dipendente")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_scritta_dipendente)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_scrittvisualizzadipendente = QtWidgets.QLabel(self.frame_scritta_dipendente)
        self.label_scrittvisualizzadipendente.setMaximumSize(QtCore.QSize(16777215, 167))
        self.label_scrittvisualizzadipendente.setStyleSheet("font: 800 22pt \"Apple SD Gothic Neo\";")
        self.label_scrittvisualizzadipendente.setObjectName("label_scrittvisualizzadipendente")
        self.verticalLayout_31.addWidget(self.label_scrittvisualizzadipendente)
        self.verticalLayout_30.addWidget(self.frame_scritta_dipendente)
        self.frame_50 = QtWidgets.QFrame(self.frame_visualizza_nuovo_dipendente)
        self.frame_50.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 16px;\n"
                                    "")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_50)
        self.verticalLayout_32.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_visualizza_nome = QtWidgets.QLabel(self.frame_50)
        self.label_visualizza_nome.setStyleSheet("\n"
                                                 "font: 400 17pt \"SF Pro\";")
        self.label_visualizza_nome.setObjectName("label_visualizza_nome")
        self.verticalLayout_32.addWidget(self.label_visualizza_nome)
        self.label_visualizza_oresettimanali = QtWidgets.QLabel(self.frame_50)
        self.label_visualizza_oresettimanali.setStyleSheet("\n"
                                                           "font: 400 17pt \"SF Pro\";")
        self.label_visualizza_oresettimanali.setObjectName("label_visualizza_oresettimanali")
        self.verticalLayout_32.addWidget(self.label_visualizza_oresettimanali)
        self.label__visualizza_pagaadora = QtWidgets.QLabel(self.frame_50)
        self.label__visualizza_pagaadora.setStyleSheet("\n"
                                                       "font: 400 17pt \"SF Pro\";")
        self.label__visualizza_pagaadora.setObjectName("label__visualizza_pagaadora")
        self.verticalLayout_32.addWidget(self.label__visualizza_pagaadora)
        self.label_visualizza_tipodicontratto = QtWidgets.QLabel(self.frame_50)
        self.label_visualizza_tipodicontratto.setStyleSheet("\n"
                                                            "font: 400 17pt \"SF Pro\";")
        self.label_visualizza_tipodicontratto.setObjectName("label_visualizza_tipodicontratto")
        self.verticalLayout_32.addWidget(self.label_visualizza_tipodicontratto)
        self.label_visualizza_email_ = QtWidgets.QLabel(self.frame_50)
        self.label_visualizza_email_.setStyleSheet("\n"
                                                   "font: 400 17pt \"SF Pro\";")
        self.label_visualizza_email_.setObjectName("label_visualizza_email_")
        self.verticalLayout_32.addWidget(self.label_visualizza_email_)
        self.label_telefono_2 = QtWidgets.QLabel(self.frame_50)
        self.label_telefono_2.setStyleSheet("\n"
                                            "font: 400 17pt \"SF Pro\";")
        self.label_telefono_2.setObjectName("label_telefono_2")
        self.verticalLayout_32.addWidget(self.label_telefono_2)
        self.verticalLayout_30.addWidget(self.frame_50)
        self.verticalLayout_28.addWidget(self.frame_visualizza_nuovo_dipendente)
        self.stackedWidget_2.addWidget(self.page_visualizza_dipendente)
        self.horizontalLayout_5.addWidget(self.stackedWidget_2)
        self.verticalLayout_6.addWidget(self.widget)
        self.stackedWidget.addWidget(self.dipendenti)
        self.pianodilavoro = QtWidgets.QWidget()
        self.pianodilavoro.setObjectName("pianodilavoro")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.pianodilavoro)
        self.verticalLayout_13.setContentsMargins(16, 4, 0, 7)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.pianodilavoro)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_14.setStyleSheet("\n"
                                    "font: 600 36pt \"SF Pro\";")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_13.addWidget(self.label_14)
        self.frame_centrale = QtWidgets.QFrame(self.pianodilavoro)
        self.frame_centrale.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_centrale.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_centrale.setObjectName("frame_centrale")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_centrale)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_sx = QtWidgets.QFrame(self.frame_centrale)
        self.frame_sx.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sx.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sx.setObjectName("frame_sx")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_sx)
        self.verticalLayout_14.setContentsMargins(0, 5, 100, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_27 = QtWidgets.QFrame(self.frame_sx)
        self.frame_27.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_27.setStyleSheet("\n"
                                    "font:600 18pt \"SF Pro\";")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_15.setContentsMargins(10, -1, 0, -1)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_oggi = QtWidgets.QLabel(self.frame_27)
        self.label_oggi.setObjectName("label_oggi")
        self.verticalLayout_15.addWidget(self.label_oggi)
        self.verticalLayout_14.addWidget(self.frame_27)
        self.frame_33 = QtWidgets.QFrame(self.frame_sx)
        self.frame_33.setMaximumSize(QtCore.QSize(2000, 167))
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_33)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_33)
        self.listWidget_2.setMinimumSize(QtCore.QSize(373, 0))
        self.listWidget_2.setMaximumSize(QtCore.QSize(16777215, 167))
        self.listWidget_2.setStyleSheet("border-radius: 14px;\n"
                                        "background-color: rgb(255, 255, 255);")
        self.listWidget_2.setObjectName("listWidget_2")

        self.horizontalLayout_14.addWidget(self.listWidget_2)
        self.verticalLayout_14.addWidget(self.frame_33)
        self.frame_29 = QtWidgets.QFrame(self.frame_sx)
        self.frame_29.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.frame_29)
        self.label_16.setStyleSheet("\n"
                                    "font:600 18pt \"SF Pro\";")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_16.addWidget(self.label_16)
        self.verticalLayout_14.addWidget(self.frame_29)
        self.frame_32 = QtWidgets.QFrame(self.frame_sx)
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 167))
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.listWidget_3 = QtWidgets.QListWidget(self.frame_32)
        self.listWidget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_3.setObjectName("listWidget_3")

        self.verticalLayout_17.addWidget(self.listWidget_3)
        self.verticalLayout_14.addWidget(self.frame_32)
        self.frame_30 = QtWidgets.QFrame(self.frame_sx)
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frame_30.setStyleSheet("\n"
                                    "font:600 18pt \"SF Pro\";")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_18.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.frame_30)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_18.addWidget(self.label_17)
        self.verticalLayout_14.addWidget(self.frame_30)
        self.frame_34 = QtWidgets.QFrame(self.frame_sx)
        self.frame_34.setMaximumSize(QtCore.QSize(16777215, 167))
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.listWidget_4 = QtWidgets.QListWidget(self.frame_34)
        self.listWidget_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_4.setObjectName("listWidget_4")

        self.verticalLayout_19.addWidget(self.listWidget_4)
        self.verticalLayout_14.addWidget(self.frame_34)
        self.frame_31 = QtWidgets.QFrame(self.frame_sx)
        self.frame_31.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_18 = QtWidgets.QLabel(self.frame_31)
        self.label_18.setStyleSheet("\n"
                                    "font:600 18pt \"SF Pro\";")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_20.addWidget(self.label_18)
        self.verticalLayout_14.addWidget(self.frame_31)
        self.frame_28 = QtWidgets.QFrame(self.frame_sx)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.listWidget_5 = QtWidgets.QListWidget(self.frame_28)
        self.listWidget_5.setMaximumSize(QtCore.QSize(16777215, 167))
        self.listWidget_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_5.setObjectName("listWidget_5")

        self.horizontalLayout_15.addWidget(self.listWidget_5)
        self.verticalLayout_14.addWidget(self.frame_28)
        self.horizontalLayout_13.addWidget(self.frame_sx)
        self.frame_26 = QtWidgets.QFrame(self.frame_centrale)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_21.setContentsMargins(-1, -1, 100, -1)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_35 = QtWidgets.QFrame(self.frame_26)
        self.frame_35.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_19 = QtWidgets.QLabel(self.frame_35)
        self.label_19.setStyleSheet("\n"
                                    "font:600 18pt \"SF Pro\";")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_22.addWidget(self.label_19)
        self.verticalLayout_21.addWidget(self.frame_35)
        self.frame_38 = QtWidgets.QFrame(self.frame_26)
        self.frame_38.setMaximumSize(QtCore.QSize(16777215, 167))
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.listWidget_6 = QtWidgets.QListWidget(self.frame_38)
        self.listWidget_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_6.setObjectName("listWidget_6")

        self.verticalLayout_23.addWidget(self.listWidget_6)
        self.verticalLayout_21.addWidget(self.frame_38)
        self.frame_36 = QtWidgets.QFrame(self.frame_26)
        self.frame_36.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_20 = QtWidgets.QLabel(self.frame_36)
        self.label_20.setStyleSheet("\n"
                                    "font:600 18pt \"SF Pro\";")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_24.addWidget(self.label_20)
        self.verticalLayout_21.addWidget(self.frame_36)
        self.frame_39 = QtWidgets.QFrame(self.frame_26)
        self.frame_39.setMaximumSize(QtCore.QSize(16777215, 167))
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_39)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.listWidget_7 = QtWidgets.QListWidget(self.frame_39)
        self.listWidget_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_7.setObjectName("listWidget_7")

        self.verticalLayout_25.addWidget(self.listWidget_7)
        self.verticalLayout_21.addWidget(self.frame_39)
        self.frame_40 = QtWidgets.QFrame(self.frame_26)
        self.frame_40.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_40)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_21 = QtWidgets.QLabel(self.frame_40)
        self.label_21.setStyleSheet("\n"
                                    "font:600 18pt \"SF Pro\";")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_26.addWidget(self.label_21)
        self.verticalLayout_21.addWidget(self.frame_40)
        self.frame_37 = QtWidgets.QFrame(self.frame_26)
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.listWidget_8 = QtWidgets.QListWidget(self.frame_37)
        self.listWidget_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_8.setObjectName("listWidget_8")

        self.verticalLayout_27.addWidget(self.listWidget_8)
        self.verticalLayout_21.addWidget(self.frame_37)
        self.horizontalLayout_13.addWidget(self.frame_26)
        self.verticalLayout_13.addWidget(self.frame_centrale)
        self.frame_buttons = QtWidgets.QFrame(self.pianodilavoro)
        self.frame_buttons.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_buttons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(7, 12, 12, 12)
        self.push_listadelleattivita = QtWidgets.QPushButton(self.frame_buttons)
        self.push_listadelleattivita.setMinimumSize(QtCore.QSize(209, 34))
        self.push_listadelleattivita.setMaximumSize(QtCore.QSize(179, 16777215))
        self.push_listadelleattivita.setStyleSheet("BORDER-RADIUS:13PX;\n"
                                                   "color: rgb(255, 255, 255);\n"
                                                   "\n"
                                                   "\n"
                                                   "border-color: rgb(235, 77, 3);\n"
                                                   "\n"
                                                   "background-color: rgb(0, 140, 251);\n"
                                                   "font: 600 14pt \"SF Pro\";")
        self.push_listadelleattivita.setObjectName("push_listadelleattivita")
        self.horizontalLayout_16.addWidget(self.push_listadelleattivita, 0, QtCore.Qt.AlignHCenter)
        self.push_eliminapianodilavoro = QtWidgets.QPushButton(self.frame_buttons)
        self.push_eliminapianodilavoro.setMinimumSize(QtCore.QSize(209, 34))
        self.push_eliminapianodilavoro.setMaximumSize(QtCore.QSize(209, 16777215))
        self.push_eliminapianodilavoro.setStyleSheet("BORDER-RADIUS:13PX;\n"
                                                     "color: rgb(255, 255, 255);\n"
                                                     "\n"
                                                     "\n"
                                                     "border-color: rgb(235, 77, 3);\n"
                                                     "\n"
                                                     "background-color: rgb(0, 140, 251);\n"
                                                     "font: 600 14pt \"SF Pro\";")
        self.push_eliminapianodilavoro.setObjectName("push_eliminapianodilavoro")
        self.horizontalLayout_16.addWidget(self.push_eliminapianodilavoro, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_13.addWidget(self.frame_buttons)
        self.stackedWidget.addWidget(self.pianodilavoro)
        self.magazzino = QtWidgets.QWidget()
        self.magazzino.setObjectName("magazzino")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.magazzino)
        self.verticalLayout_33.setContentsMargins(6, 0, 0, 7)
        self.verticalLayout_33.setSpacing(38)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.frame_51 = QtWidgets.QFrame(self.magazzino)
        self.frame_51.setMaximumSize(QtCore.QSize(16777215, 53))
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_35 = QtWidgets.QLabel(self.frame_51)
        self.label_35.setStyleSheet("\n"
                                    "font: 600 36pt \"SF Pro\";")
        self.label_35.setObjectName("label_35")
        self.verticalLayout_34.addWidget(self.label_35)
        self.verticalLayout_33.addWidget(self.frame_51)
        self.frame_52 = QtWidgets.QFrame(self.magazzino)
        self.frame_52.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_52)
        self.horizontalLayout_24.setContentsMargins(16, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_37 = QtWidgets.QLabel(self.frame_52)
        self.label_37.setStyleSheet("\n"
                                    "font:600 18pt \"SF Pro\";")
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_24.addWidget(self.label_37)
        self.label_36 = QtWidgets.QLabel(self.frame_52)
        self.label_36.setStyleSheet("\n"
                                    "font:600 18pt \"SF Pro\";")
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_24.addWidget(self.label_36)
        self.verticalLayout_33.addWidget(self.frame_52)
        self.frame_54 = QtWidgets.QFrame(self.magazzino)
        self.frame_54.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_54)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.tableWidget_frutta = QtWidgets.QTableWidget(self.frame_54)
        self.tableWidget_frutta.setObjectName("tableWidget_frutta")

        self.horizontalLayout_25.addWidget(self.tableWidget_frutta)
        self.tableWidget_erbe_aromatiche = QtWidgets.QTableWidget(self.frame_54)
        self.tableWidget_erbe_aromatiche.setObjectName("tableWidget_erbe_aromatiche")

        self.horizontalLayout_25.addWidget(self.tableWidget_erbe_aromatiche)
        self.verticalLayout_33.addWidget(self.frame_54)
        self.frame_55 = QtWidgets.QFrame(self.magazzino)
        self.frame_55.setMaximumSize(QtCore.QSize(16777215, 38))
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_55)
        self.horizontalLayout_26.setContentsMargins(16, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_38 = QtWidgets.QLabel(self.frame_55)
        self.label_38.setStyleSheet("font:600 18pt \"SF Pro\";")
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_26.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(self.frame_55)
        self.label_39.setStyleSheet("font:600 18pt \"SF Pro\";")
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_26.addWidget(self.label_39)
        self.verticalLayout_33.addWidget(self.frame_55)
        self.frame_56 = QtWidgets.QFrame(self.magazzino)
        self.frame_56.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_56)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.tableWidget_verdura = QtWidgets.QTableWidget(self.frame_56)
        self.tableWidget_verdura.setObjectName("tableWidget_verdura")

        self.horizontalLayout_27.addWidget(self.tableWidget_verdura)
        self.tableWidget_altro = QtWidgets.QTableWidget(self.frame_56)
        self.tableWidget_altro.setObjectName("tableWidget_altro")

        self.horizontalLayout_27.addWidget(self.tableWidget_altro)
        self.verticalLayout_33.addWidget(self.frame_56)
        self.frame_53 = QtWidgets.QFrame(self.magazzino)
        self.frame_53.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_53)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.push_mag_listaprodotti = QtWidgets.QPushButton(self.frame_53)
        self.push_mag_listaprodotti.setMinimumSize(QtCore.QSize(0, 38))
        self.push_mag_listaprodotti.setMaximumSize(QtCore.QSize(180, 16777215))
        self.push_mag_listaprodotti.setStyleSheet("BORDER-RADIUS:18PX;\n"
                                                  "color: rgb(255, 255, 255);\n"
                                                  "border-color: rgb(235, 77, 3);\n"
                                                  "background-color: rgb(255, 122, 0);\n"
                                                  "font: 700 13pt \"SF Pro\";")
        self.push_mag_listaprodotti.setObjectName("push_mag_listaprodotti")
        self.horizontalLayout_28.addWidget(self.push_mag_listaprodotti)
        self.push_mag_salva = QtWidgets.QPushButton(self.frame_53)
        self.push_mag_salva.setMinimumSize(QtCore.QSize(0, 38))
        self.push_mag_salva.setMaximumSize(QtCore.QSize(180, 16777215))
        self.push_mag_salva.setStyleSheet("BORDER-RADIUS:18PX;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-color: rgb(235, 77, 3);\n"
                                          "background-color: rgb(0, 140, 251);\n"
                                          "font: 700 13pt \"SF Pro\";")
        self.push_mag_salva.setObjectName("push_mag_salva")
        self.horizontalLayout_28.addWidget(self.push_mag_salva)
        self.verticalLayout_33.addWidget(self.frame_53)
        self.stackedWidget.addWidget(self.magazzino)
        self.clienti = QtWidgets.QWidget()
        self.clienti.setObjectName("clienti")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.clienti)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.frame_listadelleordinazioni = QtWidgets.QLabel(self.clienti)
        self.frame_listadelleordinazioni.setMaximumSize(QtCore.QSize(500, 31))
        self.frame_listadelleordinazioni.setStyleSheet("\n"
                                                       "font: 600 36pt \"SF Pro\";"
                                                       "color: rgb(0,0,0);")
        self.frame_listadelleordinazioni.setObjectName("frame_listadelleordinazioni")
        self.verticalLayout_37.addWidget(self.frame_listadelleordinazioni)
        self.frame = QtWidgets.QFrame(self.clienti)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_21.setContentsMargins(0, -1, 200, -1)
        self.horizontalLayout_21.setSpacing(80)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_40.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.listWidget_ordini = QtWidgets.QListWidget(self.frame_5)
        self.listWidget_ordini.setMaximumSize(QtCore.QSize(300, 411))
        self.listWidget_ordini.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius:0px;"
                                             "color: rgb(0,0,0);")
        self.listWidget_ordini.setObjectName("listWidget_ordini")
        self.verticalLayout_40.addWidget(self.listWidget_ordini)
        self.horizontalLayout_21.addWidget(self.frame_5)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.push_visualizza_ordine = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_visualizza_ordine.sizePolicy().hasHeightForWidth())
        self.push_visualizza_ordine.setSizePolicy(sizePolicy)
        self.push_visualizza_ordine.setMinimumSize(QtCore.QSize(120, 41))
        self.push_visualizza_ordine.setMaximumSize(QtCore.QSize(120, 16777215))
        self.push_visualizza_ordine.setBaseSize(QtCore.QSize(0, 12))
        self.push_visualizza_ordine.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                                  "background-color: rgb(255, 255, 255);\n"
                                                  "border-radius: 17px;"
                                                  "color: rgb(0,0,0);")
        self.push_visualizza_ordine.setIconSize(QtCore.QSize(0, 0))
        self.push_visualizza_ordine.setObjectName("push_visualizza_ordine")
        self.verticalLayout_38.addWidget(self.push_visualizza_ordine)
        # self.push_modifica_ordine = QtWidgets.QPushButton(self.frame_2)
        # self.push_modifica_ordine.setMinimumSize(QtCore.QSize(120, 41))
        # self.push_modifica_ordine.setMaximumSize(QtCore.QSize(120, 16777215))
        # self.push_modifica_ordine.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
        #                                        "background-color: rgb(255, 255, 255);\n"
        #                                        "border-radius: 17px;"
        #                                        "color: rgb(0,0,0);")
        # self.push_modifica_ordine.setObjectName("push_modifica_ordine")
        # self.verticalLayout_38.addWidget(self.push_modifica_ordine)
        self.push_elimina_ordine = QtWidgets.QPushButton(self.frame_2)
        self.push_elimina_ordine.setMinimumSize(QtCore.QSize(120, 41))
        self.push_elimina_ordine.setMaximumSize(QtCore.QSize(120, 16777215))
        self.push_elimina_ordine.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "border-radius: 17px;"
                                               "color: rgb(0,0,0);")
        self.push_elimina_ordine.setObjectName("push_elimina_ordine")
        self.verticalLayout_38.addWidget(self.push_elimina_ordine)
        self.horizontalLayout_21.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.push_creanuovoordine = QtWidgets.QPushButton(self.frame_3)
        self.push_creanuovoordine.setMinimumSize(QtCore.QSize(155, 60))
        self.push_creanuovoordine.setMaximumSize(QtCore.QSize(155, 16777215))
        self.push_creanuovoordine.setStyleSheet("font: 700 17pt \"Apple SD Gothic Neo\";\n"
                                                "\n"
                                                "border-radius: 17px;\n"
                                                "background-color: rgba(0, 122, 255, 204);\n"
                                                "color: rgb(255, 255, 255);")
        self.push_creanuovoordine.setObjectName("push_creanuovoordine")
        self.verticalLayout_39.addWidget(self.push_creanuovoordine)
        self.horizontalLayout_21.addWidget(self.frame_3)
        self.verticalLayout_37.addWidget(self.frame)
        self.stackedWidget_ordini = QtWidgets.QStackedWidget(self.clienti)
        self.stackedWidget_ordini.setObjectName("stackedWidget_ordini")
        self.page_crea_nuovo_ordine = QtWidgets.QWidget()
        self.page_crea_nuovo_ordine.setObjectName("page_crea_nuovo_ordine")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.page_crea_nuovo_ordine)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_scritta_crea_ordine = QtWidgets.QLabel(self.page_crea_nuovo_ordine)
        self.label_scritta_crea_ordine.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_scritta_crea_ordine.setStyleSheet("font: 800 22pt \"Apple SD Gothic Neo\";"
                                                     "color: rgb(0,0,0);")
        self.label_scritta_crea_ordine.setObjectName("label_scritta_crea_ordine")
        self.verticalLayout_42.addWidget(self.label_scritta_crea_ordine)
        self.frame_white_2 = QtWidgets.QFrame(self.page_crea_nuovo_ordine)
        self.frame_white_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 16px;\n"
                                         "")
        self.frame_white_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white_2.setObjectName("frame_white_2")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_white_2)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.frame_nome_2 = QtWidgets.QFrame(self.frame_white_2)
        self.frame_nome_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_nome_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_nome_2.setObjectName("frame_nome_2")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_nome_2)
        self.horizontalLayout_22.setContentsMargins(-1, 0, 200, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_nome_cliente = QtWidgets.QLabel(self.frame_nome_2)
        self.label_nome_cliente.setStyleSheet("\n"
                                              "font: 400 17pt \"SF Pro\";")
        self.label_nome_cliente.setObjectName("label_nome_cliente")
        self.horizontalLayout_22.addWidget(self.label_nome_cliente)
        self.lineEdit_nome_cliente = QtWidgets.QLineEdit(self.frame_nome_2)
        self.lineEdit_nome_cliente.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_nome_cliente.setStyleSheet("border-radius: 10px;\n"
                                                 "background-color: rgb(235, 235, 235);")
        self.lineEdit_nome_cliente.setObjectName("lineEdit_nome_cliente")
        self.horizontalLayout_22.addWidget(self.lineEdit_nome_cliente)
        self.verticalLayout_41.addWidget(self.frame_nome_2)
        self.frame_indirizzo = QtWidgets.QFrame(self.frame_white_2)
        self.frame_indirizzo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_indirizzo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_indirizzo.setObjectName("frame_indirizzo")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_indirizzo)
        self.horizontalLayout_23.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_indirizzo = QtWidgets.QLabel(self.frame_indirizzo)
        self.label_indirizzo.setStyleSheet("\n"
                                           "font: 400 17pt \"SF Pro\";")
        self.label_indirizzo.setObjectName("label_indirizzo")
        self.horizontalLayout_23.addWidget(self.label_indirizzo)
        self.lineEdit_indirizzo = QtWidgets.QLineEdit(self.frame_indirizzo)
        self.lineEdit_indirizzo.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_indirizzo.setStyleSheet("border-radius: 10px;\n"
                                              "background-color: rgb(235, 235, 235);")
        self.lineEdit_indirizzo.setObjectName("lineEdit_indirizzo")
        self.horizontalLayout_23.addWidget(self.lineEdit_indirizzo)
        self.verticalLayout_41.addWidget(self.frame_indirizzo)
        self.frame_consegna = QtWidgets.QFrame(self.frame_white_2)
        self.frame_consegna.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_consegna.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_consegna.setObjectName("frame_consegna")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_consegna)
        self.horizontalLayout_29.setContentsMargins(-1, -1, 472, -1)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_pagaadora_2 = QtWidgets.QLabel(self.frame_consegna)
        self.label_pagaadora_2.setStyleSheet("\n"
                                             "font: 400 17pt \"SF Pro\";")
        self.label_pagaadora_2.setObjectName("label_pagaadora_2")
        self.horizontalLayout_29.addWidget(self.label_pagaadora_2)
        self.dateEdit_consegna = QtWidgets.QDateEdit(self.frame_consegna)
        self.dateEdit_consegna.setMinimumSize(QtCore.QSize(0, 30))
        self.dateEdit_consegna.setStyleSheet("background-color: rgb(235,235,235);\n"
                                             "border-radius: 10px")
        self.dateEdit_consegna.setObjectName("dateEdit_consegna")
        self.horizontalLayout_29.addWidget(self.dateEdit_consegna)
        self.verticalLayout_41.addWidget(self.frame_consegna)
        self.frame_aggiungi_prodotti = QtWidgets.QFrame(self.frame_white_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_aggiungi_prodotti.sizePolicy().hasHeightForWidth())
        self.frame_aggiungi_prodotti.setSizePolicy(sizePolicy)
        self.frame_aggiungi_prodotti.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_aggiungi_prodotti.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_aggiungi_prodotti.setObjectName("frame_aggiungi_prodotti")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_aggiungi_prodotti)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_quantita = QtWidgets.QLabel(self.frame_aggiungi_prodotti)
        self.label_quantita.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_quantita.setStyleSheet("\n"
                                          "font: 400 17pt \"SF Pro\";")
        self.label_quantita.setObjectName("label_quantita")
        self.horizontalLayout_30.addWidget(self.label_quantita)
        self.frame_7 = QtWidgets.QFrame(self.frame_aggiungi_prodotti)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_31.setContentsMargins(0, -1, 300, -1)
        self.horizontalLayout_31.setSpacing(30)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.comboBox_prodotti = QtWidgets.QComboBox(self.frame_8)
        self.comboBox_prodotti.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_prodotti.setMaximumSize(QtCore.QSize(350, 16777215))
        self.comboBox_prodotti.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(235, 235, 235);")
        self.comboBox_prodotti.setObjectName("comboBox_prodotti")
        self.comboBox_prodotti.addItem("")
        self.horizontalLayout_31.addWidget(self.comboBox_prodotti)
        self.spinBox_quantita_prodotti = QtWidgets.QSpinBox(self.frame_8)
        self.spinBox_quantita_prodotti.setMaximumSize(QtCore.QSize(50, 25))
        self.spinBox_quantita_prodotti.setStyleSheet("background-color: rgb(235,235,235);\n"
                                                     "border-radius: 11px;")
        self.spinBox_quantita_prodotti.setObjectName("spinBox_quantita_prodotti")
        self.horizontalLayout_31.addWidget(self.spinBox_quantita_prodotti)
        self.push_aggiungi_prodotti = QtWidgets.QPushButton(self.frame_8)
        self.push_aggiungi_prodotti.setMinimumSize(QtCore.QSize(0, 25))
        self.push_aggiungi_prodotti.setMaximumSize(QtCore.QSize(30, 16777215))
        self.push_aggiungi_prodotti.setStyleSheet("font: 800 24pt \"Apple SD Gothic Neo\";\n"
                                                  "background-color: rgb(0, 189, 0);\n"
                                                  "border-radius: 11px;\n"
                                                  "\n"
                                                  "color: rgb(255, 255, 255);")
        self.push_aggiungi_prodotti.setObjectName("push_aggiungi_prodotti")
        self.horizontalLayout_31.addWidget(self.push_aggiungi_prodotti)
        self.verticalLayout_43.addWidget(self.frame_8)
        self.frame_18 = QtWidgets.QFrame(self.frame_7)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_43.setContentsMargins(-1, -1, 450, -1)
        self.horizontalLayout_43.setSpacing(10)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.listWidget_nome_prodotti = QtWidgets.QListWidget(self.frame_18)
        self.listWidget_nome_prodotti.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget_nome_prodotti.setStyleSheet("background-color: rgb(235,235, 235);"
                                                    "color: rgb(0,0,0);")
        self.listWidget_nome_prodotti.setObjectName("listWidget_nome_prodotti")
        self.horizontalLayout_43.addWidget(self.listWidget_nome_prodotti)
        self.listWidget_quantita_prodotti = QtWidgets.QListWidget(self.frame_18)
        self.listWidget_quantita_prodotti.setMaximumSize(QtCore.QSize(50, 16777215))
        self.listWidget_quantita_prodotti.setStyleSheet("background-color: rgb(235,235,235);"
                                                        "color: rgb(0,0,0);")
        self.listWidget_quantita_prodotti.setObjectName("listWidget_quantita_prodotti")
        self.horizontalLayout_43.addWidget(self.listWidget_quantita_prodotti)
        self.pushButton_rimuovi_prodotto = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_rimuovi_prodotto.setStyleSheet("font: 800 24pt \"Apple SD Gothic Neo\";\n"
                                                       "background-color: rgb(226, 0, 0);\n"
                                                       "border-radius: 11px;\n"
                                                       "color: rgb(255, 255, 255);")
        self.pushButton_rimuovi_prodotto.setObjectName("pushButton_rimuovi_prodotto")
        self.horizontalLayout_43.addWidget(self.pushButton_rimuovi_prodotto)
        self.verticalLayout_43.addWidget(self.frame_18)
        self.horizontalLayout_30.addWidget(self.frame_7)
        self.verticalLayout_41.addWidget(self.frame_aggiungi_prodotti)
        self.verticalLayout_42.addWidget(self.frame_white_2)
        self.frame_salva_ordini = QtWidgets.QFrame(self.page_crea_nuovo_ordine)
        self.frame_salva_ordini.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salva_ordini.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salva_ordini.setObjectName("frame_salva_ordini")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_salva_ordini)
        self.horizontalLayout_32.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.pushButton_salva_ordine = QtWidgets.QPushButton(self.frame_salva_ordini)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_salva_ordine.sizePolicy().hasHeightForWidth())
        self.pushButton_salva_ordine.setSizePolicy(sizePolicy)
        self.pushButton_salva_ordine.setMinimumSize(QtCore.QSize(0, 36))
        self.pushButton_salva_ordine.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_salva_ordine.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_salva_ordine.setStyleSheet("font: 700 14pt \"Apple SD Gothic Neo\";\n"
                                                   "background-color: rgb(255, 255, 255);\n"
                                                   "border-radius: 11px;\n"
                                                   "background-color: rgba(0, 122, 255, 204);\n"
                                                   "color: rgb(255, 255, 255);")
        self.pushButton_salva_ordine.setObjectName("pushButton_salva_ordine")
        self.horizontalLayout_32.addWidget(self.pushButton_salva_ordine)
        self.verticalLayout_42.addWidget(self.frame_salva_ordini)
        self.stackedWidget_ordini.addWidget(self.page_crea_nuovo_ordine)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_ordini.addWidget(self.page_2)
        self.page_visualizza_ordine = QtWidgets.QWidget()
        self.page_visualizza_ordine.setObjectName("page_visualizza_ordine")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.page_visualizza_ordine)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.label_scritta_ordine = QtWidgets.QLabel(self.page_visualizza_ordine)
        self.label_scritta_ordine.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_scritta_ordine.setStyleSheet("font: 800 22pt \"Apple SD Gothic Neo\";")
        self.label_scritta_ordine.setObjectName("label_scritta_ordine")
        self.verticalLayout_46.addWidget(self.label_scritta_ordine)
        self.frame_white_3 = QtWidgets.QFrame(self.page_visualizza_ordine)
        self.frame_white_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 16px;\n"
                                         "")
        self.frame_white_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white_3.setObjectName("frame_white_3")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_white_3)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.frame_visualizza_nome_cliente = QtWidgets.QFrame(self.frame_white_3)
        self.frame_visualizza_nome_cliente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_visualizza_nome_cliente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_visualizza_nome_cliente.setObjectName("frame_visualizza_nome_cliente")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_visualizza_nome_cliente)
        self.horizontalLayout_33.setContentsMargins(-1, 0, 200, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_visualizza_nome_cliente = QtWidgets.QLabel(self.frame_visualizza_nome_cliente)
        self.label_visualizza_nome_cliente.setStyleSheet("\n"
                                                         "font: 400 17pt \"SF Pro\";")
        self.label_visualizza_nome_cliente.setObjectName("label_visualizza_nome_cliente")
        self.horizontalLayout_33.addWidget(self.label_visualizza_nome_cliente)
        self.verticalLayout_44.addWidget(self.frame_visualizza_nome_cliente)
        self.frame_vis_indirizzo = QtWidgets.QFrame(self.frame_white_3)
        self.frame_vis_indirizzo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vis_indirizzo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vis_indirizzo.setObjectName("frame_vis_indirizzo")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_vis_indirizzo)
        self.horizontalLayout_34.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_visualizza_indirizzo = QtWidgets.QLabel(self.frame_vis_indirizzo)
        self.label_visualizza_indirizzo.setStyleSheet("\n"
                                                      "font: 400 17pt \"SF Pro\";")
        self.label_visualizza_indirizzo.setObjectName("label_visualizza_indirizzo")
        self.horizontalLayout_34.addWidget(self.label_visualizza_indirizzo)
        self.verticalLayout_44.addWidget(self.frame_vis_indirizzo)
        self.frame_vis_consegna = QtWidgets.QFrame(self.frame_white_3)
        self.frame_vis_consegna.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vis_consegna.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vis_consegna.setObjectName("frame_vis_consegna")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_vis_consegna)
        self.horizontalLayout_35.setContentsMargins(-1, -1, 472, -1)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_visualizza_consegna = QtWidgets.QLabel(self.frame_vis_consegna)
        self.label_visualizza_consegna.setStyleSheet("\n"
                                                     "font: 400 17pt \"SF Pro\";")
        self.label_visualizza_consegna.setObjectName("label_visualizza_consegna")
        self.horizontalLayout_35.addWidget(self.label_visualizza_consegna)
        self.verticalLayout_44.addWidget(self.frame_vis_consegna)
        self.frame_9 = QtWidgets.QFrame(self.frame_white_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_prodotti = QtWidgets.QLabel(self.frame_9)
        self.label_prodotti.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_prodotti.setStyleSheet("\n"
                                          "font: 400 17pt \"SF Pro\";")
        self.label_prodotti.setObjectName("label_prodotti")
        self.horizontalLayout_36.addWidget(self.label_prodotti)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.tableWidget_visualizza_prodotti = QtWidgets.QTableWidget(self.frame_10)
        self.tableWidget_visualizza_prodotti.setStyleSheet("")
        self.tableWidget_visualizza_prodotti.setObjectName("tableWidget_visualizza_prodotti")
        self.tableWidget_visualizza_prodotti.setColumnCount(1)
        self.tableWidget_visualizza_prodotti.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_visualizza_prodotti.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_visualizza_prodotti.setHorizontalHeaderItem(0, item)
        self.verticalLayout_45.addWidget(self.tableWidget_visualizza_prodotti)
        self.horizontalLayout_36.addWidget(self.frame_10)
        self.verticalLayout_44.addWidget(self.frame_9)
        self.frame_11 = QtWidgets.QFrame(self.frame_white_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.label_visualizza_totale = QtWidgets.QLabel(self.frame_11)
        self.label_visualizza_totale.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_visualizza_totale.setStyleSheet("\n"
                                                   "font: 400 17pt \"SF Pro\";")
        self.label_visualizza_totale.setObjectName("label_visualizza_totale")
        self.verticalLayout_47.addWidget(self.label_visualizza_totale)
        self.verticalLayout_44.addWidget(self.frame_11)
        self.verticalLayout_46.addWidget(self.frame_white_3)
        self.stackedWidget_ordini.addWidget(self.page_visualizza_ordine)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.label_scritta_mod_ordine = QtWidgets.QLabel(self.page)
        self.label_scritta_mod_ordine.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_scritta_mod_ordine.setStyleSheet("font: 800 22pt \"Apple SD Gothic Neo\";")
        self.label_scritta_mod_ordine.setObjectName("label_scritta_mod_ordine")
        self.verticalLayout_50.addWidget(self.label_scritta_mod_ordine)
        self.frame_white_4 = QtWidgets.QFrame(self.page)
        self.frame_white_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 16px;\n"
                                         "")
        self.frame_white_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white_4.setObjectName("frame_white_4")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.frame_white_4)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.frame_mod_cliente = QtWidgets.QFrame(self.frame_white_4)
        self.frame_mod_cliente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mod_cliente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mod_cliente.setObjectName("frame_mod_cliente")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_mod_cliente)
        self.horizontalLayout_37.setContentsMargins(-1, 0, 200, 0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_mod_cliente = QtWidgets.QLabel(self.frame_mod_cliente)
        self.label_mod_cliente.setStyleSheet("\n"
                                             "font: 400 17pt \"SF Pro\";")
        self.label_mod_cliente.setObjectName("label_mod_cliente")
        self.horizontalLayout_37.addWidget(self.label_mod_cliente)
        self.lineEdit_mod_nome_cliente = QtWidgets.QLineEdit(self.frame_mod_cliente)
        self.lineEdit_mod_nome_cliente.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_mod_nome_cliente.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(235, 235, 235);")
        self.lineEdit_mod_nome_cliente.setObjectName("lineEdit_mod_nome_cliente")
        self.horizontalLayout_37.addWidget(self.lineEdit_mod_nome_cliente)
        self.verticalLayout_48.addWidget(self.frame_mod_cliente)
        self.frame_mod_indirizzo = QtWidgets.QFrame(self.frame_white_4)
        self.frame_mod_indirizzo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mod_indirizzo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mod_indirizzo.setObjectName("frame_mod_indirizzo")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.frame_mod_indirizzo)
        self.horizontalLayout_38.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_38.setSpacing(10)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_mod_indirizzo = QtWidgets.QLabel(self.frame_mod_indirizzo)
        self.label_mod_indirizzo.setStyleSheet("\n"
                                               "font: 400 17pt \"SF Pro\";")
        self.label_mod_indirizzo.setObjectName("label_mod_indirizzo")
        self.horizontalLayout_38.addWidget(self.label_mod_indirizzo)
        self.lineEdit_mod_indirizzo = QtWidgets.QLineEdit(self.frame_mod_indirizzo)
        self.lineEdit_mod_indirizzo.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_mod_indirizzo.setStyleSheet("border-radius: 10px;\n"
                                                  "background-color: rgb(235, 235, 235);")
        self.lineEdit_mod_indirizzo.setObjectName("lineEdit_mod_indirizzo")
        self.horizontalLayout_38.addWidget(self.lineEdit_mod_indirizzo)
        self.verticalLayout_48.addWidget(self.frame_mod_indirizzo)
        self.frame_mod_consegna = QtWidgets.QFrame(self.frame_white_4)
        self.frame_mod_consegna.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mod_consegna.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mod_consegna.setObjectName("frame_mod_consegna")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.frame_mod_consegna)
        self.horizontalLayout_39.setContentsMargins(-1, -1, 472, -1)
        self.horizontalLayout_39.setSpacing(10)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_pagaadora_7 = QtWidgets.QLabel(self.frame_mod_consegna)
        self.label_pagaadora_7.setStyleSheet("\n"
                                             "font: 400 17pt \"SF Pro\";")
        self.label_pagaadora_7.setObjectName("label_pagaadora_7")
        self.horizontalLayout_39.addWidget(self.label_pagaadora_7)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_mod_consegna)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.dateEdit_2.setStyleSheet("background-color: rgb(235,235,235);\n"
                                      "border-radius: 10px")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_39.addWidget(self.dateEdit_2)
        self.verticalLayout_48.addWidget(self.frame_mod_consegna)
        self.frame_12 = QtWidgets.QFrame(self.frame_white_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_mod_prodotti = QtWidgets.QLabel(self.frame_12)
        self.label_mod_prodotti.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_mod_prodotti.setStyleSheet("\n"
                                              "font: 400 17pt \"SF Pro\";")
        self.label_mod_prodotti.setObjectName("label_mod_prodotti")
        self.horizontalLayout_40.addWidget(self.label_mod_prodotti)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_41.setContentsMargins(0, -1, 600, -1)
        self.horizontalLayout_41.setSpacing(30)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.comboBox_mod_prodotti = QtWidgets.QComboBox(self.frame_16)
        self.comboBox_mod_prodotti.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_mod_prodotti.setMaximumSize(QtCore.QSize(350, 16777215))
        self.comboBox_mod_prodotti.setStyleSheet("border-radius: 10px;\n"
                                                 "background-color: rgb(235, 235, 235);")
        self.comboBox_mod_prodotti.setObjectName("comboBox_mod_prodotti")
        self.comboBox_mod_prodotti.addItem("")
        self.comboBox_mod_prodotti.addItem("")
        self.horizontalLayout_41.addWidget(self.comboBox_mod_prodotti)
        self.pushButton_modi_aggiungi_prodotto = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_modi_aggiungi_prodotto.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_modi_aggiungi_prodotto.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_modi_aggiungi_prodotto.setStyleSheet("font: 800 24pt \"Apple SD Gothic Neo\";\n"
                                                             "background-color: rgb(0, 189, 0);\n"
                                                             "border-radius: 11px;\n"
                                                             "\n"
                                                             "color: rgb(255, 255, 255);")
        self.pushButton_modi_aggiungi_prodotto.setObjectName("pushButton_modi_aggiungi_prodotto")
        self.horizontalLayout_41.addWidget(self.pushButton_modi_aggiungi_prodotto)
        self.verticalLayout_49.addWidget(self.frame_16)
        self.tableWidget_mod_prodotti = QtWidgets.QTableWidget(self.frame_14)
        self.tableWidget_mod_prodotti.setStyleSheet("")
        self.tableWidget_mod_prodotti.setObjectName("tableWidget_mod_prodotti")
        self.tableWidget_mod_prodotti.setColumnCount(1)
        self.tableWidget_mod_prodotti.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mod_prodotti.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mod_prodotti.setHorizontalHeaderItem(0, item)
        self.verticalLayout_49.addWidget(self.tableWidget_mod_prodotti)
        self.horizontalLayout_40.addWidget(self.frame_14)
        self.verticalLayout_48.addWidget(self.frame_12)
        self.verticalLayout_50.addWidget(self.frame_white_4)
        self.frame_17 = QtWidgets.QFrame(self.page)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.pushButton_modifica_dipendenti = QtWidgets.QPushButton(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_modifica_dipendenti.sizePolicy().hasHeightForWidth())
        self.pushButton_modifica_dipendenti.setSizePolicy(sizePolicy)
        self.pushButton_modifica_dipendenti.setMinimumSize(QtCore.QSize(0, 36))
        self.pushButton_modifica_dipendenti.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_modifica_dipendenti.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_modifica_dipendenti.setStyleSheet("font: 700 14pt \"Apple SD Gothic Neo\";\n"
                                                          "background-color: rgb(255, 255, 255);\n"
                                                          "border-radius: 11px;\n"
                                                          "background-color: rgba(0, 122, 255, 204);\n"
                                                          "color: rgb(255, 255, 255);")
        self.pushButton_modifica_dipendenti.setObjectName("pushButton_modifica_dipendenti")
        self.horizontalLayout_42.addWidget(self.pushButton_modifica_dipendenti)
        self.verticalLayout_50.addWidget(self.frame_17)
        self.stackedWidget_ordini.addWidget(self.page)
        self.verticalLayout_37.addWidget(self.stackedWidget_ordini)
        self.stackedWidget.addWidget(self.clienti)
        self.contabilita = QtWidgets.QWidget()
        self.contabilita.setObjectName("contabilita")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.contabilita)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_contabilita = QtWidgets.QLabel(self.contabilita)
        self.label_contabilita.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_contabilita.setStyleSheet("font: 600 36pt \"SF Pro\";")
        self.label_contabilita.setObjectName("label_contabilita")
        self.verticalLayout_29.addWidget(self.label_contabilita)
        self.frame_6 = QtWidgets.QFrame(self.contabilita)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.tabWidget_contabilita = QtWidgets.QTabWidget(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_contabilita.sizePolicy().hasHeightForWidth())
        self.tabWidget_contabilita.setSizePolicy(sizePolicy)
        self.tabWidget_contabilita.setObjectName("tabWidget_contabilita")
        self.settimanale = QtWidgets.QWidget()
        self.settimanale.setObjectName("settimanale")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.settimanale)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_20 = QtWidgets.QFrame(self.settimanale)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.push_sett_prec = QtWidgets.QPushButton(self.frame_20)
        self.push_sett_prec.setMinimumSize(QtCore.QSize(0, 25))
        self.push_sett_prec.setMaximumSize(QtCore.QSize(50, 16777215))
        self.push_sett_prec.setStyleSheet("font: 700 14pt \"Apple SD Gothic Neo\";\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 11px;\n"
                                          "background-color: rgba(0, 122, 255, 204);\n"
                                          "color: rgb(255, 255, 255);")
        self.push_sett_prec.setObjectName("push_sett_prec")
        self.horizontalLayout_18.addWidget(self.push_sett_prec)
        self.label_settimana = QtWidgets.QLabel(self.frame_20)
        self.label_settimana.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_settimana.setStyleSheet("font: 600 20pt \"SF Pro\";")
        self.label_settimana.setObjectName("label_settimana")
        self.horizontalLayout_18.addWidget(self.label_settimana)
        self.push_sett_succ = QtWidgets.QPushButton(self.frame_20)
        self.push_sett_succ.setMinimumSize(QtCore.QSize(0, 25))
        self.push_sett_succ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.push_sett_succ.setStyleSheet("font: 700 14pt \"Apple SD Gothic Neo\";\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 11px;\n"
                                          "background-color: rgba(0, 122, 255, 204);\n"
                                          "color: rgb(255, 255, 255);")
        self.push_sett_succ.setObjectName("push_sett_succ")
        self.horizontalLayout_18.addWidget(self.push_sett_succ)
        self.verticalLayout_36.addWidget(self.frame_20)
        self.tableWidget_settimanale = QtWidgets.QTableWidget(self.settimanale)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_settimanale.sizePolicy().hasHeightForWidth())
        self.tableWidget_settimanale.setSizePolicy(sizePolicy)
        self.tableWidget_settimanale.setStyleSheet("font: 400 14pt \"Apple SD Gothic Neo\";\n"
                                                   "")
        self.tableWidget_settimanale.setObjectName("tableWidget_settimanale")
        self.tableWidget_settimanale.setColumnCount(4)
        self.tableWidget_settimanale.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_settimanale.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_settimanale.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_settimanale.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_settimanale.setHorizontalHeaderItem(3, item)
        self.verticalLayout_36.addWidget(self.tableWidget_settimanale)
        self.frame_21 = QtWidgets.QFrame(self.settimanale)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.checkBox_sett_entrate = QtWidgets.QCheckBox(self.frame_21)
        self.checkBox_sett_entrate.setStyleSheet("font: 400 18pt \"Apple SD Gothic Neo\";")
        self.checkBox_sett_entrate.setObjectName("checkBox_sett_entrate")
        self.horizontalLayout_19.addWidget(self.checkBox_sett_entrate)
        self.checkBox_sett_uscite = QtWidgets.QCheckBox(self.frame_21)
        self.checkBox_sett_uscite.setStyleSheet("font: 400 18pt \"Apple SD Gothic Neo\";")
        self.checkBox_sett_uscite.setObjectName("checkBox_sett_uscite")
        self.horizontalLayout_19.addWidget(self.checkBox_sett_uscite)
        self.verticalLayout_36.addWidget(self.frame_21)
        self.label_sett_ricavi_costi_utile = QtWidgets.QLabel(self.settimanale)
        self.label_sett_ricavi_costi_utile.setStyleSheet("font: 400 20pt \"Apple SD Gothic Neo\";")
        self.label_sett_ricavi_costi_utile.setObjectName("label_sett_ricavi_costi_utile")
        self.verticalLayout_36.addWidget(self.label_sett_ricavi_costi_utile)
        self.tabWidget_contabilita.addTab(self.settimanale, "")
        self.mensile = QtWidgets.QWidget()
        self.mensile.setObjectName("mensile")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.mensile)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.frame_24 = QtWidgets.QFrame(self.mensile)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.push_mese_prec = QtWidgets.QPushButton(self.frame_24)
        self.push_mese_prec.setMinimumSize(QtCore.QSize(0, 25))
        self.push_mese_prec.setMaximumSize(QtCore.QSize(50, 16777215))
        self.push_mese_prec.setStyleSheet("font: 700 14pt \"Apple SD Gothic Neo\";\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 11px;\n"
                                          "background-color: rgba(0, 122, 255, 204);\n"
                                          "color: rgb(255, 255, 255);")
        self.push_mese_prec.setObjectName("push_mese_prec")
        self.horizontalLayout_45.addWidget(self.push_mese_prec)
        self.label_mese = QtWidgets.QLabel(self.frame_24)
        self.label_mese.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_mese.setStyleSheet("font: 600 20pt \"SF Pro\";")
        self.label_mese.setObjectName("label_mese")
        self.horizontalLayout_45.addWidget(self.label_mese)
        self.push_mese_succ = QtWidgets.QPushButton(self.frame_24)
        self.push_mese_succ.setMinimumSize(QtCore.QSize(0, 25))
        self.push_mese_succ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.push_mese_succ.setStyleSheet("font: 700 14pt \"Apple SD Gothic Neo\";\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 11px;\n"
                                          "background-color: rgba(0, 122, 255, 204);\n"
                                          "color: rgb(255, 255, 255);")
        self.push_mese_succ.setObjectName("push_mese_succ")
        self.horizontalLayout_45.addWidget(self.push_mese_succ)
        self.verticalLayout_52.addWidget(self.frame_24)
        self.tableWidget_mensile = QtWidgets.QTableWidget(self.mensile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_mensile.sizePolicy().hasHeightForWidth())
        self.tableWidget_mensile.setSizePolicy(sizePolicy)
        self.tableWidget_mensile.setStyleSheet("font: 400 14pt \"Apple SD Gothic Neo\";")
        self.tableWidget_mensile.setObjectName("tableWidget_mensile")
        self.tableWidget_mensile.setColumnCount(4)
        self.tableWidget_mensile.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mensile.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mensile.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mensile.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mensile.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mensile.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mensile.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mensile.setHorizontalHeaderItem(3, item)
        self.verticalLayout_52.addWidget(self.tableWidget_mensile)
        self.frame_25 = QtWidgets.QFrame(self.mensile)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.checkBox_mese_entrate = QtWidgets.QCheckBox(self.frame_25)
        self.checkBox_mese_entrate.setStyleSheet("font: 400 18pt \"Apple SD Gothic Neo\";")
        self.checkBox_mese_entrate.setObjectName("checkBox_mese_entrate")
        self.horizontalLayout_46.addWidget(self.checkBox_mese_entrate)
        self.checkBox_mese_uscite = QtWidgets.QCheckBox(self.frame_25)
        self.checkBox_mese_uscite.setStyleSheet("font: 400 18pt \"Apple SD Gothic Neo\";")
        self.checkBox_mese_uscite.setObjectName("checkBox_mese_uscite")
        self.horizontalLayout_46.addWidget(self.checkBox_mese_uscite)
        self.verticalLayout_52.addWidget(self.frame_25)
        self.label_mese_ricavi_costi_utile = QtWidgets.QLabel(self.mensile)
        self.label_mese_ricavi_costi_utile.setStyleSheet("font: 400 20pt \"Apple SD Gothic Neo\";")
        self.label_mese_ricavi_costi_utile.setObjectName("label_mese_ricavi_costi_utile")
        self.verticalLayout_52.addWidget(self.label_mese_ricavi_costi_utile)
        self.tabWidget_contabilita.addTab(self.mensile, "")
        self.verticalLayout_35.addWidget(self.tabWidget_contabilita)
        self.verticalLayout_29.addWidget(self.frame_6)
        self.frame_19 = QtWidgets.QFrame(self.contabilita)
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_vocidibilancio = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_vocidibilancio.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_vocidibilancio.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_vocidibilancio.setStyleSheet("font: 700 16pt \"Apple SD Gothic Neo\";\n"
                                                     "background-color: rgb(255, 255, 255);\n"
                                                     "border-radius: 11px;\n"
                                                     "background-color: rgba(0, 122, 255, 204);\n"
                                                     "color: rgb(255, 255, 255);")
        self.pushButton_vocidibilancio.setObjectName("pushButton_vocidibilancio")
        self.horizontalLayout_17.addWidget(self.pushButton_vocidibilancio)
        self.verticalLayout_29.addWidget(self.frame_19)
        self.stackedWidget.addWidget(self.contabilita)
        self.statistiche = QtWidgets.QWidget()
        self.statistiche.setObjectName("statistiche")
        self.stackedWidget.addWidget(self.statistiche)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.main_frame)
        self.verticalLayout.addWidget(self.central_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        # pagina StackedWidget2 per modificare il dipendente
        self.page_modifica_dipendente = QtWidgets.QWidget()
        self.page_modifica_dipendente.setObjectName("page_modifica_dipendente")
        self.verticalLayout_102 = QtWidgets.QVBoxLayout(self.page_modifica_dipendente)
        self.verticalLayout_102.setContentsMargins(7, 2, 20, 16)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName("verticalLayout_10")
        self.frame_scritta2 = QtWidgets.QFrame(self.page_modifica_dipendente)
        self.frame_scritta2.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_scritta2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_scritta2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_scritta2.setObjectName("frame_scritta2")
        self.verticalLayout_112 = QtWidgets.QVBoxLayout(self.frame_scritta2)
        self.verticalLayout_112.setObjectName("verticalLayout_11")
        self.label_scritta2 = QtWidgets.QLabel(self.frame_scritta2)
        self.label_scritta2.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_scritta2.setStyleSheet("font: 800 22pt \"Apple SD Gothic Neo\";")
        self.label_scritta2.setObjectName("label_scritta2")
        self.verticalLayout_112.addWidget(self.label_scritta2)
        self.verticalLayout_102.addWidget(self.frame_scritta2)
        self.frame_white2 = QtWidgets.QFrame(self.page_modifica_dipendente)
        self.frame_white2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 16px;\n"
                                        "")
        self.frame_white2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white2.setObjectName("frame_white2")
        self.verticalLayout_122 = QtWidgets.QVBoxLayout(self.frame_white2)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName("verticalLayout_122")
        self.frame_nome2 = QtWidgets.QFrame(self.frame_white2)
        self.frame_nome2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_nome2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_nome2.setObjectName("frame_nome2")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.frame_nome2)
        self.horizontalLayout_62.setContentsMargins(-1, 0, 200, 0)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.label_nome2 = QtWidgets.QLabel(self.frame_nome2)
        self.label_nome2.setStyleSheet("\n"
                                       "font: 400 17pt \"SF Pro\";")
        self.label_nome2.setObjectName("label_nome2")
        self.horizontalLayout_62.addWidget(self.label_nome2)
        self.lineEdit_nome2 = QtWidgets.QLineEdit(self.frame_nome2)
        self.lineEdit_nome2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_nome2.setStyleSheet("border-radius: 10px;\n"
                                          "background-color: rgb(235, 235, 235);")
        self.lineEdit_nome2.setObjectName("lineEdit_nome2")
        self.horizontalLayout_62.addWidget(self.lineEdit_nome2)
        self.verticalLayout_122.addWidget(self.frame_nome2)
        self.frame_ore_settimanali2 = QtWidgets.QFrame(self.frame_white2)
        self.frame_ore_settimanali2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ore_settimanali2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ore_settimanali2.setObjectName("frame_ore_settimanali2")
        self.horizontalLayout_102 = QtWidgets.QHBoxLayout(self.frame_ore_settimanali2)
        self.horizontalLayout_102.setContentsMargins(-1, -1, 472, -1)
        self.horizontalLayout_102.setSpacing(10)
        self.horizontalLayout_102.setObjectName("horizontalLayout_102")
        self.label_oresettimanali2 = QtWidgets.QLabel(self.frame_ore_settimanali2)
        self.label_oresettimanali2.setStyleSheet("\n"
                                                 "font: 400 17pt \"SF Pro\";")
        self.label_oresettimanali2.setObjectName("label_oresettimanali2")
        self.horizontalLayout_102.addWidget(self.label_oresettimanali2)
        self.spinBox_oresettimanali2 = QtWidgets.QSpinBox(self.frame_ore_settimanali2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_oresettimanali2.sizePolicy().hasHeightForWidth())
        self.spinBox_oresettimanali2.setSizePolicy(sizePolicy)
        self.spinBox_oresettimanali2.setMinimumSize(QtCore.QSize(60, 30))
        self.spinBox_oresettimanali2.setStyleSheet("border-radius: 10px;\n"
                                                   "background-color: rgb(235, 235, 235);")
        self.spinBox_oresettimanali2.setObjectName("spinBox_oresettimanali2")
        self.horizontalLayout_102.addWidget(self.spinBox_oresettimanali2)
        self.verticalLayout_122.addWidget(self.frame_ore_settimanali2)
        self.frame_paga_ad_ora2 = QtWidgets.QFrame(self.frame_white2)
        self.frame_paga_ad_ora2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_paga_ad_ora2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_paga_ad_ora2.setObjectName("frame_paga_ad_ora2")
        self.horizontalLayout_92 = QtWidgets.QHBoxLayout(self.frame_paga_ad_ora2)
        self.horizontalLayout_92.setContentsMargins(-1, -1, 472, -1)
        self.horizontalLayout_92.setSpacing(10)
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")
        self.label_pagaadora2 = QtWidgets.QLabel(self.frame_paga_ad_ora2)
        self.label_pagaadora2.setStyleSheet("\n"
                                            "font: 400 17pt \"SF Pro\";")
        self.label_pagaadora2.setObjectName("label_pagaadora2")
        self.horizontalLayout_92.addWidget(self.label_pagaadora2)
        self.spinBox_pagaadora2 = QtWidgets.QSpinBox(self.frame_paga_ad_ora2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_pagaadora2.sizePolicy().hasHeightForWidth())
        self.spinBox_pagaadora2.setSizePolicy(sizePolicy)
        self.spinBox_pagaadora2.setMinimumSize(QtCore.QSize(60, 30))
        self.spinBox_pagaadora2.setStyleSheet("border-radius: 10px;\n"
                                              "background-color: rgb(235, 235, 235);")
        self.spinBox_pagaadora2.setObjectName("spinBox_pagaadora2")
        self.horizontalLayout_92.addWidget(self.spinBox_pagaadora2)
        self.verticalLayout_122.addWidget(self.frame_paga_ad_ora2)
        self.frame_tipodicontratto2 = QtWidgets.QFrame(self.frame_white2)
        self.frame_tipodicontratto2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tipodicontratto2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tipodicontratto2.setObjectName("frame_tipodicontratto2")
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout(self.frame_tipodicontratto2)
        self.horizontalLayout_82.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_82.setObjectName("horizontalLayout_8")
        self.label_tipodicontratto2 = QtWidgets.QLabel(self.frame_tipodicontratto2)
        self.label_tipodicontratto2.setStyleSheet("\n"
                                                  "font: 400 17pt \"SF Pro\";")
        self.label_tipodicontratto2.setObjectName("label_tipodicontratto2")
        self.horizontalLayout_82.addWidget(self.label_tipodicontratto2)
        self.lineEdit_tipodicontratto2 = QtWidgets.QLineEdit(self.frame_tipodicontratto2)
        self.lineEdit_tipodicontratto2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_tipodicontratto2.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(235, 235, 235);")
        self.lineEdit_tipodicontratto2.setObjectName("lineEdit_tipodicontratto2")
        self.horizontalLayout_82.addWidget(self.lineEdit_tipodicontratto2)
        self.verticalLayout_122.addWidget(self.frame_tipodicontratto2)
        self.frame_email2 = QtWidgets.QFrame(self.frame_white2)
        self.frame_email2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_email2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_email2.setObjectName("frame_email2")
        self.horizontalLayout_72 = QtWidgets.QHBoxLayout(self.frame_email2)
        self.horizontalLayout_72.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_72.setObjectName("horizontalLayout_7")
        self.label_email2 = QtWidgets.QLabel(self.frame_email2)
        self.label_email2.setStyleSheet("\n"
                                        "font: 400 17pt \"SF Pro\";")
        self.label_email2.setObjectName("label_email2")
        self.horizontalLayout_72.addWidget(self.label_email2)
        self.lineEdit_email2 = QtWidgets.QLineEdit(self.frame_email2)
        self.lineEdit_email2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_email2.setStyleSheet("border-radius: 10px;\n"
                                           "background-color: rgb(235, 235, 235);")
        self.lineEdit_email2.setObjectName("lineEdit_email2")
        self.horizontalLayout_72.addWidget(self.lineEdit_email2)
        self.verticalLayout_122.addWidget(self.frame_email2)
        self.frame_telefono2 = QtWidgets.QFrame(self.frame_white2)
        self.frame_telefono2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_telefono2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_telefono2.setObjectName("frame_telefono2")
        self.horizontalLayout_112 = QtWidgets.QHBoxLayout(self.frame_telefono2)
        self.horizontalLayout_112.setContentsMargins(-1, -1, 200, -1)
        self.horizontalLayout_112.setObjectName("horizontalLayout_11")
        self.label_telefono2 = QtWidgets.QLabel(self.frame_telefono2)
        self.label_telefono2.setStyleSheet("\n"
                                           "font: 400 17pt \"SF Pro\";")
        self.label_telefono2.setObjectName("label_telefono2")
        self.horizontalLayout_112.addWidget(self.label_telefono2)
        self.lineEdit_telefono2 = QtWidgets.QLineEdit(self.frame_telefono2)
        self.lineEdit_telefono2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_telefono2.setStyleSheet("border-radius: 10px;\n"
                                              "background-color: rgb(235, 235, 235);")
        self.lineEdit_telefono2.setObjectName("lineEdit_telefono2")
        self.horizontalLayout_112.addWidget(self.lineEdit_telefono2)
        self.verticalLayout_122.addWidget(self.frame_telefono2)
        self.frame_salva_dipendenti2 = QtWidgets.QFrame(self.frame_white2)
        self.frame_salva_dipendenti2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salva_dipendenti2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salva_dipendenti2.setObjectName("frame_salva_dipendenti2")
        self.horizontalLayout_122 = QtWidgets.QHBoxLayout(self.frame_salva_dipendenti2)
        self.horizontalLayout_122.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_122.setObjectName("horizontalLayout_122")
        self.pushButton_salva_dipendenti2 = QtWidgets.QPushButton(self.frame_salva_dipendenti2)
        # self.pushButton_salva_dipendenti2.setEnabled(False)
        self.pushButton_salva_dipendenti2.setMinimumSize(QtCore.QSize(0, 36))
        self.pushButton_salva_dipendenti2.setMaximumSize(QtCore.QSize(145, 16777215))
        self.pushButton_salva_dipendenti2.setStyleSheet("font: 700 14pt \"Apple SD Gothic Neo\";\n"
                                                        "background-color: rgb(255, 255, 255);\n"
                                                        "border-radius: 11px;\n"
                                                        "background-color: rgba(0, 122, 255, 204);\n"
                                                        "color: rgb(255, 255, 255);")
        self.pushButton_salva_dipendenti2.setObjectName("pushButton_salva_dipendenti2")
        self.horizontalLayout_122.addWidget(self.pushButton_salva_dipendenti2)
        self.verticalLayout_122.addWidget(self.frame_salva_dipendenti2)
        self.verticalLayout_102.addWidget(self.frame_white2)
        self.stackedWidget_2.addWidget(self.page_modifica_dipendente)
        self.label_nome2.setText("Nome")
        self.label_oresettimanali2.setText("Ore settimanali")
        self.label_pagaadora2.setText("Paga ad ora (€)")
        self.label_tipodicontratto2.setText("Tipo di contratto")
        self.label_email2.setText("E-mail")
        self.label_telefono2.setText("Telefono")
        self.pushButton_salva_dipendenti2.setText("Modifica dipendente")
        self.statistiche = QWidget()
        self.statistiche.setObjectName(u"statistiche")
        self.verticalLayout_51 = QVBoxLayout(self.statistiche)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_statistiche = QFrame(self.statistiche)
        self.frame_statistiche.setObjectName(u"frame_statistiche")
        sizePolicy.setHeightForWidth(self.frame_statistiche.sizePolicy().hasHeightForWidth())
        self.frame_statistiche.setSizePolicy(sizePolicy)
        self.frame_statistiche.setMinimumSize(QSize(0, 50))
        self.frame_statistiche.setMaximumSize(QSize(16777215, 55))
        self.frame_statistiche.setFrameShape(QFrame.StyledPanel)
        self.frame_statistiche.setFrameShadow(QFrame.Raised)
        self.frame_statistiche.setLineWidth(-1)
        self.label = QLabel(self.frame_statistiche)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 600 36pt \"SF Pro\";\n"
                                 "color: rgb(0, 0, 0);")
        self.label.setMaximumSize(QSize(16777215, 30))
        self.verticalLayout_51.addWidget(self.label)

        self.verticalLayout_51.addWidget(self.frame_statistiche)

        self.label_tot_dipendenti = QLabel(self.statistiche)
        self.label_tot_dipendenti.setObjectName(u"label_tot_dipendenti")
        self.label_tot_dipendenti.setMaximumSize(QSize(16777215, 60))
        self.label_tot_dipendenti.setStyleSheet(u"font: 500 18pt \"SF Pro\";\n"
                                                "color: rgb(0, 0, 0);")

        self.verticalLayout_51.addWidget(self.label_tot_dipendenti)

        self.label_tot_att_da_completare = QLabel(self.statistiche)
        self.label_tot_att_da_completare.setObjectName(u"label_tot_att_da_completare")
        self.label_tot_att_da_completare.setMaximumSize(QSize(16777215, 60))
        self.label_tot_att_da_completare.setStyleSheet(u"font: 500 18pt \"SF Pro\";\n"
                                                       "color: rgb(0, 0, 0);")

        self.verticalLayout_51.addWidget(self.label_tot_att_da_completare)

        self.label_tot_att_completate = QLabel(self.statistiche)
        self.label_tot_att_completate.setObjectName(u"label_tot_att_completate")
        self.label_tot_att_completate.setMaximumSize(QSize(16777215, 60))
        self.label_tot_att_completate.setStyleSheet(u"font: 500 18pt \"SF Pro\";\n"
                                                    "color: rgb(0, 0, 0);")

        self.verticalLayout_51.addWidget(self.label_tot_att_completate)

        self.label_tot_frutta = QLabel(self.statistiche)
        self.label_tot_frutta.setObjectName(u"label_tot_frutta")
        self.label_tot_frutta.setMaximumSize(QSize(16777215, 60))
        self.label_tot_frutta.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                            "font: 500 18pt \"SF Pro\";")

        self.verticalLayout_51.addWidget(self.label_tot_frutta)

        self.label_tot_verdura = QLabel(self.statistiche)
        self.label_tot_verdura.setObjectName(u"label_tot_verdura")
        self.label_tot_verdura.setMaximumSize(QSize(16777215, 60))
        self.label_tot_verdura.setStyleSheet(u"font: 500 18pt \"SF Pro\";\n"
                                             "color: rgb(0, 0, 0);")

        self.verticalLayout_51.addWidget(self.label_tot_verdura)

        self.label_erbe_aromatiche = QLabel(self.statistiche)
        self.label_erbe_aromatiche.setObjectName(u"label_erbe_aromatiche")
        self.label_erbe_aromatiche.setMaximumSize(QSize(16777215, 60))
        self.label_erbe_aromatiche.setStyleSheet(u"font: 500 18pt \"SF Pro\";\n"
                                                 "color: rgb(0, 0, 0);")

        self.verticalLayout_51.addWidget(self.label_erbe_aromatiche)

        self.label_altro = QLabel(self.statistiche)
        self.label_altro.setObjectName(u"label_altro")
        self.label_altro.setMaximumSize(QSize(16777215, 60))
        self.label_altro.setStyleSheet(u"font: 500 18pt \"SF Pro\";\n"
                                       "color: rgb(0, 0, 0);")

        self.verticalLayout_51.addWidget(self.label_altro)

        self.label_valore_magazzino = QLabel(self.statistiche)
        self.label_valore_magazzino.setObjectName(u"label_valore_magazzino")
        self.label_valore_magazzino.setMaximumSize(QSize(16777215, 60))
        self.label_valore_magazzino.setStyleSheet(u"font: 500 18pt \"SF Pro\";\n"
                                                  "color: rgb(0, 0, 0);")

        self.verticalLayout_51.addWidget(self.label_valore_magazzino)

        self.label_tot_ordinazioni = QLabel(self.statistiche)
        self.label_tot_ordinazioni.setObjectName(u"label_tot_ordinazioni")
        self.label_tot_ordinazioni.setMaximumSize(QSize(16777215, 60))
        self.label_tot_ordinazioni.setStyleSheet(u"font: 500 18pt \"SF Pro\";\n"
                                                 "color: rgb(0, 0, 0);")

        self.verticalLayout_51.addWidget(self.label_tot_ordinazioni)

        self.label_9 = QLabel(self.statistiche)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_51.addWidget(self.label_9)

        self.stackedWidget.addWidget(self.statistiche)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        # parte con il main frame vuoto
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # prende il file .json e popola la lista_prodotti_salvati dipendenti
        self.controller = ControlloreListaDipendenti()

        self.listview_model = QStandardItemModel(self.listWidget_dipendenti)

        for dipendente in self.controller.get_lista():
            item = QStandardItem()
            item.setText(dipendente.nome)
            item.setEditable(False)
            self.listview_model.appendRow(item)
        self.listWidget_dipendenti.setModel(self.listview_model)

        # visalizza a schermo le info di un dipendente
        self.controller2 = ControlloreDipendente(dipendente)

        def get_info_dipendente_selezionato():
            try:
                selected = self.listWidget_dipendenti.selectedIndexes()[0].row()

                with open("dipendenti/data/lista_dipendenti_iniziali.json", "r") as file:
                    data = json.load(file)
                dip = data[selected]

                self.label_scrittvisualizzadipendente.setText(dip['nome'])
                self.label_visualizza_nome.setText("Nome:  " + dip['nome'])
                self.label_visualizza_oresettimanali.setText("Ore settimanali:  " + str(dip['ore']))
                self.label__visualizza_pagaadora.setText("Paga ad ora (€):  " + str(dip['compenso_a_ore']))
                self.label_visualizza_tipodicontratto.setText("Tipo di contratto:  " + dip['tipo_contratto'])
                self.label_visualizza_email_.setText("E-mail:  " + dip['email'])
                self.label_telefono_2.setText("Telefono:  " + dip['telefono'])
            except Exception:
                QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                QMessageBox.about(MainWindow, " ", "Devi selezionare prima un dipendente!")
                self.stackedWidget_2.setCurrentWidget(self.page_empty)

        self.push_visualizza.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentWidget(self.page_visualizza_dipendente))
        self.push_visualizza.clicked.connect(lambda: get_info_dipendente_selezionato())

        # elimina un dipendente dalla lista
        def box_question_eliminare_dipendente():
            try:
                selected = self.listWidget_dipendenti.selectedIndexes()[0].row()
                with open("dipendenti/data/lista_dipendenti_iniziali.json") as file:
                    data = json.load(file)
                dip = data[selected]

                QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                q = QMessageBox.question(MainWindow, '', "Sei sicuro di voler eliminare " + dip[
                    'nome'] + " dalla lista dei dipendenti?", QMessageBox.Yes | QMessageBox.No)
                if q == QMessageBox.Yes:
                    del data[selected]
                    with open("dipendenti/data/lista_dipendenti_iniziali.json", 'w') as f:
                        json.dump(data, f, indent=4)

                    self.stackedWidget_2.setCurrentWidget(self.page_empty)

                    QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                    QMessageBox.about(MainWindow, "",
                                      dip['nome'] + " è stato eliminato dalla lista dei dipendenti")

                    self.controller = ControlloreListaDipendenti()
                    self.listview_model = QStandardItemModel(self.listWidget_dipendenti)
                    for dipendente in self.controller.get_lista():
                        item = QStandardItem()
                        item.setText(dipendente.nome)
                        item.setEditable(False)
                        self.listview_model.appendRow(item)
                    self.listWidget_dipendenti.setModel(self.listview_model)

                else:
                    pass

            except Exception:
                QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                QMessageBox.about(MainWindow, " ", "Devi selezionare prima un dipendente!")
                self.stackedWidget_2.setCurrentWidget(self.page_empty)

        self.push_elimina.clicked.connect(lambda: box_question_eliminare_dipendente())

        # prende il testo dei lineEdit in CreaNuovoDipendente e fa l'append al file .json
        def new_employee():
            self.stackedWidget_2.setCurrentWidget(self.page_crea_nuovo_dipendente)
            self.label_scritta.setText("Crea un nuovo dipendente!")
            self.lineEdit_nome.clear()
            self.spinBox_oresettimanali.clear()
            self.spinBox_pagaadora.clear()
            self.lineEdit_tipodicontratto.clear()
            self.lineEdit_email.clear()
            self.lineEdit_telefono.clear()

            def get_line_edits():
                nome = self.lineEdit_nome.text()
                ore = self.spinBox_oresettimanali.value()
                pagaadora = self.spinBox_pagaadora.value()
                tipodicontratto = self.lineEdit_tipodicontratto.text()
                email = self.lineEdit_email.text()
                telefono = self.lineEdit_telefono.text()

                if nome == "" or ore == "" or pagaadora == "" or tipodicontratto == "" or email == "" or telefono == "":
                    QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                    QMessageBox.critical(MainWindow, 'ERRORE!', 'Completa tutti i campi richiesti!', QMessageBox.Ok,
                                         QMessageBox.Ok)

                else:

                    dipendente_creato = {
                        "nome": str(nome),
                        "ore": ore,
                        "compenso_a_ore": pagaadora,
                        "tipo_contratto": str(tipodicontratto),
                        "email": str(email),
                        "telefono": str(telefono)
                    }

                    with open("dipendenti/data/lista_dipendenti_iniziali.json", "r+") as file:
                        data = json.load(file)
                        data.append(dipendente_creato)
                        file.seek(0)
                        json.dump(data, file, indent=4)

                    QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                    QMessageBox.about(MainWindow, "",
                                      str(nome) + " è stato creato correttamente nella lista dei dipendenti!")

                    self.lineEdit_nome.clear()
                    self.spinBox_oresettimanali.clear()
                    self.spinBox_pagaadora.clear()
                    self.lineEdit_tipodicontratto.clear()
                    self.lineEdit_email.clear()
                    self.lineEdit_telefono.clear()

                    self.contr = ControlloreListaDipendenti()
                    self.listview_model2 = QStandardItemModel(self.listWidget_dipendenti)

                    for dipendente in self.contr.get_lista():
                        item = QStandardItem()
                        item.setText(dipendente.nome)
                        item.setEditable(False)
                        self.listview_model2.appendRow(item)
                    self.listWidget_dipendenti.setModel(self.listview_model2)

            self.pushButton_salva_dipendenti.clicked.connect(lambda: get_line_edits())

        self.push_creanuovodipendente.clicked.connect(lambda: new_employee())
        self.retranslateUi(MainWindow)

        # modifica i dati di un dipendente

        def update_info_dipendente():
            try:
                selected = self.listWidget_dipendenti.selectedIndexes()[0].row()

                with open("dipendenti/data/lista_dipendenti_iniziali.json") as file:
                    data = json.load(file)
                dip = data[selected]
                self.label_scritta2.setText(dip['nome'])

                self.lineEdit_nome2.setText(dip['nome'])
                self.spinBox_oresettimanali2.setValue(dip['ore'])
                self.spinBox_pagaadora2.setValue(dip['compenso_a_ore'])
                self.lineEdit_tipodicontratto2.setText(dip['tipo_contratto'])
                self.lineEdit_email2.setText(dip['email'])
                self.lineEdit_telefono2.setText(dip['telefono'])

                def salva_dipendente_modificato():
                    dip['nome'] = self.lineEdit_nome2.text()
                    dip['ore'] = self.spinBox_oresettimanali2.value()
                    dip['compenso_a_ore'] = self.spinBox_pagaadora2.value()
                    dip['tipo_contratto'] = self.lineEdit_tipodicontratto2.text()
                    dip['email'] = self.lineEdit_email2.text()
                    dip['telefono'] = self.lineEdit_telefono2.text()
                    self.label_scritta2.setText(self.lineEdit_nome2.text())

                    with open("dipendenti/data/lista_dipendenti_iniziali.json", "w") as file:
                        json.dump(data, file, indent=4)

                    QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                    QMessageBox.about(MainWindow, "",
                                      "Il dipendente " + self.lineEdit_nome2.text() + " è stato modificato correttamente!")

                    self.contr = ControlloreListaDipendenti()
                    self.listview_model2 = QStandardItemModel(self.listWidget_dipendenti)

                    for dipendente in self.contr.get_lista():
                        item = QStandardItem()
                        item.setText(dipendente.nome)
                        item.setEditable(False)
                        self.listview_model2.appendRow(item)
                    self.listWidget_dipendenti.setModel(self.listview_model2)

                self.pushButton_salva_dipendenti2.clicked.connect(lambda: salva_dipendente_modificato())
            except Exception:
                QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                QMessageBox.about(MainWindow, " ", "Devi selezionare prima un dipendente!")
                self.stackedWidget_2.setCurrentWidget(self.page_empty)

        self.push_modifica.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_modifica_dipendente))
        self.push_modifica.clicked.connect(lambda: update_info_dipendente())

        # sezione Lista Prodotti
        self.push_mag_listaprodotti.clicked.connect(self.vista_lista_prodotti)

        # sezione Piano di Lavoro
        self.push_listadelleattivita.clicked.connect(self.vista_piano_lavoro)

        # popolo le listWidget di PianoLavoro
        def fill_task_calendar():
            self.listWidget_2.clear()
            self.listWidget_3.clear()
            self.listWidget_4.clear()
            self.listWidget_5.clear()
            self.listWidget_6.clear()
            self.listWidget_7.clear()
            self.listWidget_8.clear()
            with open('pianodilavoro/data/lista_task.json') as f:
                tasks = json.load(f)
                for task in tasks:
                    if task['giorni_rimanenti_alla_scadenza'] == 0:
                        self.listWidget_2.addItem(task['nome_task'])
                    elif task['giorni_rimanenti_alla_scadenza'] == 1:
                        self.listWidget_3.addItem(task['nome_task'])
                    elif task['giorni_rimanenti_alla_scadenza'] == 2:
                        self.listWidget_4.addItem(task['nome_task'])
                    elif task['giorni_rimanenti_alla_scadenza'] == 3:
                        self.listWidget_5.addItem(task['nome_task'])
                    elif task['giorni_rimanenti_alla_scadenza'] == 4:
                        self.listWidget_6.addItem(task['nome_task'])
                    elif task['giorni_rimanenti_alla_scadenza'] == 5:
                        self.listWidget_7.addItem(task['nome_task'])
                    elif task['giorni_rimanenti_alla_scadenza'] == 6:
                        self.listWidget_8.addItem(task['nome_task'])
                    else:
                        pass
        self.push_pianodilavoro.clicked.connect(lambda: fill_task_calendar())



        def elimina_lista_attivita():
            QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0);"
                                                  "background-color: rgb(235, 235, 235);"
                                                  "border: none")
            q = QMessageBox.question(MainWindow, '',
                                     "Sei sicuro di voler eliminare tutta la lista delle attività? ",
                                     QMessageBox.Yes | QMessageBox.No)
            if q == QMessageBox.Yes:
                tasks = []
                with open("pianodilavoro/data/lista_task.json", 'w') as file:
                    json.dump(tasks, file)
                self.listWidget_2.clear()
                self.listWidget_3.clear()
                self.listWidget_4.clear()
                self.listWidget_5.clear()
                self.listWidget_6.clear()
                self.listWidget_7.clear()
                self.listWidget_8.clear()
        self.push_eliminapianodilavoro.clicked.connect(lambda: elimina_lista_attivita())

        # MAGAZZINO

        def aggiorna_magazzino():
            lista_magazzino = ControlloreListaProdottiSalvati()
            self.tableWidget_frutta.setRowCount(lista_magazzino.get_count_lista_frutta())  #
            self.tableWidget_frutta.setColumnCount(2)
            self.tableWidget_frutta.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Quantità"))
            self.tableWidget_frutta.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Valore (€)"))
            row_frutta = 0  #
            for frutto in lista_magazzino.get_lista_frutta():  #

                self.tableWidget_frutta.setVerticalHeaderItem(row_frutta, QtWidgets.QTableWidgetItem(frutto['nome']))
                self.tableWidget_frutta.verticalHeader().setMinimumWidth(130)
                self.tableWidget_frutta.setItem(row_frutta, 0, QtWidgets.QTableWidgetItem(str(frutto['quantita'])))
                self.tableWidget_frutta.setItem(row_frutta, 1, QtWidgets.QTableWidgetItem(str(round((frutto['quantita'] * frutto['prezzo_su_unita']), 2))))
                row_frutta = row_frutta + 1
            #
            self.tableWidget_verdura.setRowCount(lista_magazzino.get_count_lista_verdura())
            self.tableWidget_verdura.setColumnCount(2)
            self.tableWidget_verdura.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Quantità"))
            self.tableWidget_verdura.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Valore (€)"))
            row_verdura = 0
            for verdura in lista_magazzino.get_lista_verdura():
                self.tableWidget_verdura.setVerticalHeaderItem(row_verdura, QtWidgets.QTableWidgetItem(verdura['nome']))
                self.tableWidget_verdura.verticalHeader().setMinimumWidth(130)
                self.tableWidget_verdura.setItem(row_verdura, 0, QtWidgets.QTableWidgetItem(str(verdura['quantita'])))
                self.tableWidget_verdura.setItem(row_verdura, 1, QtWidgets.QTableWidgetItem(
                    str(round((verdura['quantita'] * verdura['prezzo_su_unita']), 2))))
                row_verdura = row_verdura + 1

            self.tableWidget_erbe_aromatiche.setRowCount(lista_magazzino.get_count_lista_erbe_aromatiche())
            self.tableWidget_erbe_aromatiche.setColumnCount(2)
            self.tableWidget_erbe_aromatiche.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Quantità"))
            self.tableWidget_erbe_aromatiche.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Valore (€)"))
            row_erbe_aromatiche = 0
            for erba in lista_magazzino.get_lista_erbe_aromatiche():
                self.tableWidget_erbe_aromatiche.setVerticalHeaderItem(row_erbe_aromatiche,
                                                                       QtWidgets.QTableWidgetItem(erba['nome']))
                self.tableWidget_erbe_aromatiche.verticalHeader().setMinimumWidth(130)
                self.tableWidget_erbe_aromatiche.setItem(row_erbe_aromatiche, 0,
                                                         QtWidgets.QTableWidgetItem(str(erba['quantita'])))
                self.tableWidget_erbe_aromatiche.setItem(row_erbe_aromatiche, 1, QtWidgets.QTableWidgetItem(
                    str(round((erba['quantita'] * erba['prezzo_su_unita']), 2))))
                row_erbe_aromatiche = row_erbe_aromatiche + 1

            self.tableWidget_altro.setRowCount(lista_magazzino.get_count_lista_altro())
            self.tableWidget_altro.setColumnCount(2)
            self.tableWidget_altro.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Quantità"))
            self.tableWidget_altro.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Valore (€)"))
            row_altro = 0
            for altro in lista_magazzino.get_lista_altro():
                self.tableWidget_altro.setVerticalHeaderItem(row_altro, QtWidgets.QTableWidgetItem(altro['nome']))
                self.tableWidget_altro.verticalHeader().setMinimumWidth(130)
                self.tableWidget_altro.setItem(row_altro, 0, QtWidgets.QTableWidgetItem(str(altro['quantita'])))
                self.tableWidget_altro.setItem(row_altro, 1, QtWidgets.QTableWidgetItem(
                    str(round((altro['quantita'] * altro['prezzo_su_unita']), 2))))
                row_altro = row_altro + 1
        self.push_magazzino.clicked.connect(lambda: aggiorna_magazzino())

        lista_magazzino = ControlloreListaProdottiSalvati()
        def get_quantita_magazzino():
            lista_magazzino = ControlloreListaProdottiSalvati()
            row_frutta = 0
            for frutto in lista_magazzino.get_lista_frutta():
                index = lista_magazzino.get_index_by_name(self.tableWidget_frutta.verticalHeaderItem(row_frutta).text())
                quantita = int(self.tableWidget_frutta.item(row_frutta, 0).text())
                lista_magazzino.modifica_quantita_by_index(index, quantita)
                self.tableWidget_frutta.setItem(row_frutta, 1, QtWidgets.QTableWidgetItem(str(round(quantita * lista_magazzino.get_prezzo_by_index(index), 2))))
                row_frutta += 1

            row_verdura = 0
            for verdura in lista_magazzino.get_lista_verdura():
                index = lista_magazzino.get_index_by_name(self.tableWidget_verdura.verticalHeaderItem(row_verdura).text())
                quantita = int(self.tableWidget_verdura.item(row_verdura, 0).text())
                lista_magazzino.modifica_quantita_by_index(index, quantita)
                self.tableWidget_verdura.setItem(row_verdura, 1, QtWidgets.QTableWidgetItem(str(round(quantita * lista_magazzino.get_prezzo_by_index(index),2))))
                row_verdura += 1

            row_erbe_aromatiche = 0
            for erba_aromatica in lista_magazzino.get_lista_erbe_aromatiche():
                index = lista_magazzino.get_index_by_name(self.tableWidget_erbe_aromatiche.verticalHeaderItem(row_erbe_aromatiche).text())
                quantita = int(self.tableWidget_erbe_aromatiche.item(row_erbe_aromatiche, 0).text())
                lista_magazzino.modifica_quantita_by_index(index, quantita)
                self.tableWidget_erbe_aromatiche.setItem(row_erbe_aromatiche, 1, QtWidgets.QTableWidgetItem(str(round(quantita * lista_magazzino.get_prezzo_by_index(index),2))))
                row_erbe_aromatiche += 1

            row_altro = 0
            for altro in lista_magazzino.get_lista_altro():
                index = lista_magazzino.get_index_by_name(self.tableWidget_altro.verticalHeaderItem(row_altro).text())
                quantita = int(self.tableWidget_altro.item(row_altro, 0).text())
                lista_magazzino.modifica_quantita_by_index(index, quantita)
                self.tableWidget_altro.setItem(row_altro, 1, QtWidgets.QTableWidgetItem(str(round(quantita * lista_magazzino.get_prezzo_by_index(index),2))))
                row_altro += 1
        self.push_mag_salva.clicked.connect(lambda: get_quantita_magazzino())


        # CLIENTI
        self.stackedWidget_ordini.setCurrentWidget(self.page_2)
        lista_ordini = ControlloreListaOrdinazioni()
        for ordine in lista_ordini.get_lista_ordinazioni():
            self.listWidget_ordini.addItem(ordine.get_nome_cliente())

        # visualizza un ordine di un cliente
        def visualizza_ordine():
            self.stackedWidget_ordini.setCurrentWidget(self.page_visualizza_ordine)
            selected = self.listWidget_ordini.selectedIndexes()[0].row()
            lista_ordini = ControlloreListaOrdinazioni()
            ordine_selezionato = lista_ordini.get_ordine_by_index(selected)

            self.label_scritta_ordine.setText("Ordine di: " + ordine_selezionato.get_nome_cliente())
            self.label_visualizza_nome_cliente.setText("Nome cliente:  " + ordine_selezionato.get_nome_cliente())
            self.label_visualizza_indirizzo.setText("Indirizzo di consegna:  " + ordine_selezionato.get_indirizzo())
            self.label_visualizza_consegna.setText("Giorno della consegna:  " + ordine_selezionato.get_data())
            self.label_prodotti.setText("Prodotti")
            self.tableWidget_visualizza_prodotti.setRowCount(ordine_selezionato.get_count_prodotti())
            self.tableWidget_visualizza_prodotti.setColumnCount(1)
            self.tableWidget_visualizza_prodotti.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem(str("Quantità")))
            totale = 0
            lista_prodotti = ControlloreListaProdottiSalvati()
            row = 0
            for row in range(ordine_selezionato.get_count_prodotti()):
                self.tableWidget_visualizza_prodotti.setVerticalHeaderItem(row, QtWidgets.QTableWidgetItem(
                    str(ordine_selezionato.get_prodotto_by_index(row))))
                self.tableWidget_visualizza_prodotti.setItem(row, 0, QtWidgets.QTableWidgetItem(
                    str(ordine_selezionato.get_quantita_by_index(row))))
                totale += (ordine_selezionato.get_quantita_by_index(row)) * (
                    lista_prodotti.get_prezzo_by_name(ordine_selezionato.get_prodotto_by_index(row)))
                row += 1
            self.label_visualizza_totale.setText("Totale:  " + str(totale) + " €")

        self.push_visualizza_ordine.clicked.connect(lambda: visualizza_ordine())

        def crea_nuovo_ordine():
            self.stackedWidget_ordini.setCurrentWidget(self.page_crea_nuovo_ordine)
            self.dateEdit_consegna.setDate(datetime.date.today())
            for prodotto in lista_magazzino.get_lista():
                self.comboBox_prodotti.addItem(prodotto.get_nome())
                prodotti = []
                quantita = []

            def aggiungi_prodotto():
                prod = self.comboBox_prodotti.currentText()
                if prod == "":
                    QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                    QMessageBox.critical(MainWindow, 'ERRORE!', 'Devi selezionare prima un prodotto!', QMessageBox.Ok,
                                         QMessageBox.Ok)
                else:
                    self.listWidget_nome_prodotti.addItem(prod)
                    prodotti.append(prod)
                    self.listWidget_quantita_prodotti.addItem(str(self.spinBox_quantita_prodotti.value()))
                    quantita.append(self.spinBox_quantita_prodotti.value())
                    self.comboBox_prodotti.setCurrentIndex(0)
                    self.spinBox_quantita_prodotti.setValue(0)

            self.push_aggiungi_prodotti.clicked.connect(lambda: aggiungi_prodotto())

            def elimina_prodotto_da_ordine():
                selected = self.listWidget_nome_prodotti.selectedIndexes()[0].row()
                del prodotti[selected]
                del quantita[selected]
                self.listWidget_nome_prodotti.clear()
                self.listWidget_quantita_prodotti.clear()

                for prodotto in prodotti:
                    self.listWidget_nome_prodotti.addItem(prodotto)
                for q in quantita:
                    self.listWidget_quantita_prodotti.addItem(str(q))

            self.pushButton_rimuovi_prodotto.clicked.connect(lambda: elimina_prodotto_da_ordine())

            def aggiungi_ordine():
                nome = self.lineEdit_nome_cliente.text()
                indirizzo = self.lineEdit_indirizzo.text()
                if nome == "" or indirizzo == "":
                    QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                    QMessageBox.critical(MainWindow, 'ERRORE!', 'Completa tutti i campi richiesti!', QMessageBox.Ok,
                                         QMessageBox.Ok)
                else:
                    data_consegna_sfalsata = self.dateEdit_consegna.date()
                    data_consegna_giusta = str(
                        str(data_consegna_sfalsata.day()) + "-" + str(data_consegna_sfalsata.month()) + "-" + str(
                            data_consegna_sfalsata.year()))
                    lista_ordini.add_ordine(nome, indirizzo, data_consegna_giusta, prodotti, quantita)
                    self.lineEdit_nome_cliente.clear()
                    self.lineEdit_indirizzo.clear()
                    self.dateEdit_consegna.setDate(datetime.date.today())
                    self.comboBox_prodotti.setCurrentIndex(0)
                    self.spinBox_quantita_prodotti.setValue(0)
                    self.listWidget_nome_prodotti.clear()
                    self.listWidget_quantita_prodotti.clear()
                    self.listWidget_ordini.addItem(nome)

            self.pushButton_salva_ordine.clicked.connect(lambda: aggiungi_ordine())

        self.push_creanuovoordine.clicked.connect(lambda: crea_nuovo_ordine())

        def elimina_ordine():
            try:
                selected = self.listWidget_ordini.selectedIndexes()[0].row()
                nome_eliminato = self.listWidget_ordini.currentItem().text()
                QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                q = QMessageBox.question(MainWindow, '',
                                         "Sei sicuro di voler eliminare '" + nome_eliminato + "' dalla lista delle ordinazioni?",
                                         QMessageBox.Yes | QMessageBox.No)
                if q == QMessageBox.Yes:
                    with open("clienti/data/lista_ordinazioni.json", "r") as file:
                        data = json.load(file)
                    with open("clienti/data/lista_ordinazioni.json", "w") as file:
                        del data[selected]
                        json.dump(data, file, indent=4)
                    self.listWidget_ordini.clear()
                    lista_ordini = ControlloreListaOrdinazioni()
                    for ordine in lista_ordini.get_lista_ordinazioni():
                        self.listWidget_ordini.addItem(ordine.get_nome_cliente())
                    self.stackedWidget_ordini.setCurrentWidget(self.page_2)

                    QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                    QMessageBox.about(MainWindow, "",
                                      "'" + nome_eliminato + "' è stato eliminato dalla lista delle ordinazioni")
            except Exception:
                QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
                QMessageBox.about(MainWindow, " ", "Devi selezionare prima un ordine!")

        self.push_elimina_ordine.clicked.connect(lambda: elimina_ordine())

        # CONTABILITA'
        self.pushButton_vocidibilancio.clicked.connect(self.vista_voci_di_bilancio)
        self.push_sett_prec.clicked.connect(lambda: self.click_sett_prec(self.bilancio))
        self.push_sett_succ.clicked.connect(lambda: self.click_sett_succ(self.bilancio))
        self.push_mese_prec.clicked.connect(lambda: self.click_mese_prec(self.bilancio))
        self.push_mese_succ.clicked.connect(lambda: self.click_mese_succ(self.bilancio))
        self.checkBox_sett_entrate.setChecked(True)
        self.checkBox_sett_uscite.setChecked(True)
        self.checkBox_mese_entrate.setChecked(True)
        self.checkBox_mese_uscite.setChecked(True)
        self.visualizzaBilancioSettimanale(self.bilancio)
        self.visualizzaBilancioMensile(self.bilancio)
        self.checkBox_sett_entrate.stateChanged.connect(lambda: self.visualizzaBilancioSettimanale(self.bilancio))
        self.checkBox_sett_uscite.stateChanged.connect(lambda: self.visualizzaBilancioSettimanale(self.bilancio))
        self.checkBox_mese_entrate.stateChanged.connect(lambda: self.visualizzaBilancioMensile(self.bilancio))
        self.checkBox_mese_uscite.stateChanged.connect(lambda: self.visualizzaBilancioMensile(self.bilancio))

    def click_sett_prec(self, bilancio):
        bilancio.previous_sett()
        self.visualizzaBilancioSettimanale(bilancio)

    def click_sett_succ(self, bilancio):
        bilancio.next_sett()
        self.visualizzaBilancioSettimanale(bilancio)

    def click_mese_prec(self, bilancio):
        bilancio.previous_mens()
        self.visualizzaBilancioMensile(bilancio)

    def click_mese_succ(self, bilancio):
        bilancio.next_mens()
        self.visualizzaBilancioMensile(bilancio)

    def visualizzaBilancioSettimanale(self, bilancio):
        row_bilancio = 0
        bilancio_sett = bilancio.bilancio_corrente_sett
        dat_iniziale_str = bilancio_sett.get_data_iniziale().strftime('%d %B %Y')
        dat_finale_str = bilancio_sett.get_data_finale().strftime('%d %B %Y')
        self.label_settimana.setText('{dt1} - {dt2}'.format(dt1=dat_iniziale_str, dt2= dat_finale_str))
        if self.checkBox_sett_entrate.isChecked() and not self.checkBox_sett_uscite.isChecked():
            l = len(bilancio_sett.get_entrate_settimanali())
            self.tableWidget_settimanale.setRowCount(l)
            self.tableWidget_settimanale.setColumnWidth(0, 130)
            for voce in bilancio_sett.get_entrate_settimanali():
                self.tableWidget_settimanale.setItem(row_bilancio, 0, QtWidgets.QTableWidgetItem(voce[0].get_nome()))
                entrata = 'Sì'
                self.tableWidget_settimanale.setItem(row_bilancio, 1, QtWidgets.QTableWidgetItem(entrata))
                self.tableWidget_settimanale.setItem(row_bilancio, 2, QtWidgets.QTableWidgetItem(str(voce[1].date())))
                self.tableWidget_settimanale.setItem(row_bilancio, 3, QtWidgets.QTableWidgetItem(
                    '{euro}.{cent}€'.format(euro=str(voce[0].get_valore_euro()[0]),
                                            cent=str(voce[0].get_valore_euro()[1]))))
                row_bilancio += 1
            ricavo_str = centToEuroString(bilancio_sett.get_ricavo())
            costi_str = centToEuroString(bilancio_sett.get_costi())
            utile_str = centToEuroString(bilancio_sett.get_utile())
            self.label_sett_ricavi_costi_utile.setText('Ricavi: {ricavi}    Costi: {costi}    Utile: {utile}'.format(ricavi = ricavo_str, costi  = costi_str, utile = utile_str))

        if (not self.checkBox_sett_entrate.isChecked()) and self.checkBox_sett_uscite.isChecked():
            l = len(bilancio_sett.get_uscite_settimanali())
            self.tableWidget_settimanale.setRowCount(l)
            self.tableWidget_settimanale.setColumnWidth(0, 130)
            for voce in bilancio_sett.get_uscite_settimanali():
                self.tableWidget_settimanale.setItem(row_bilancio, 0, QtWidgets.QTableWidgetItem(voce[0].get_nome()))
                entrata = 'No'
                self.tableWidget_settimanale.setItem(row_bilancio, 1, QtWidgets.QTableWidgetItem(entrata))
                self.tableWidget_settimanale.setItem(row_bilancio, 2, QtWidgets.QTableWidgetItem(str(voce[1].date())))
                self.tableWidget_settimanale.setItem(row_bilancio, 3, QtWidgets.QTableWidgetItem(
                    '{euro}.{cent}€'.format(euro=str(voce[0].get_valore_euro()[0]),
                                            cent=str(voce[0].get_valore_euro()[1]))))
                row_bilancio += 1
            ricavo_str = centToEuroString(bilancio_sett.get_ricavo())
            costi_str = centToEuroString(bilancio_sett.get_costi())
            utile_str = centToEuroString(bilancio_sett.get_utile())
            self.label_sett_ricavi_costi_utile.setText('Ricavi: {ricavi}    Costi: {costi}    Utile: {utile}'.format(ricavi = ricavo_str, costi  = costi_str, utile = utile_str))


        if not self.checkBox_sett_entrate.isChecked() and not self.checkBox_sett_uscite.isChecked():
            self.tableWidget_settimanale.setRowCount(0)
        if self.checkBox_sett_entrate.isChecked() and self.checkBox_sett_uscite.isChecked():
            l = len(bilancio_sett.get_voci_settimanali())
            self.tableWidget_settimanale.setRowCount(l)
            self.tableWidget_settimanale.setColumnWidth(0, 130)
            for voce in bilancio_sett.get_voci_settimanali():
                self.tableWidget_settimanale.setItem(row_bilancio, 0, QtWidgets.QTableWidgetItem(voce[0].get_nome()))
                entrata = None
                if voce[2]:
                    entrata = 'Sì'
                else:
                    entrata = 'No'
                self.tableWidget_settimanale.setItem(row_bilancio, 1, QtWidgets.QTableWidgetItem(entrata))
                self.tableWidget_settimanale.setItem(row_bilancio, 2, QtWidgets.QTableWidgetItem(str(voce[1].date())))
                self.tableWidget_settimanale.setItem(row_bilancio, 3, QtWidgets.QTableWidgetItem(
                    '{euro}.{cent}€'.format(euro=str(voce[0].get_valore_euro()[0]),
                                            cent=str(voce[0].get_valore_euro()[1]))))
                row_bilancio += 1
            ricavo_str = centToEuroString(bilancio_sett.get_ricavo())
            costi_str = centToEuroString(bilancio_sett.get_costi())
            utile_str = centToEuroString(bilancio_sett.get_utile())
            self.label_sett_ricavi_costi_utile.setText('Ricavi: {ricavi}    Costi: {costi}    Utile: {utile}'.format(ricavi = ricavo_str, costi  = costi_str, utile = utile_str))

    def visualizzaBilancioMensile(self, bilancio):
        row_bilancio = 0
        bilancio_mens = bilancio.bilancio_corrente_mens
        #dat_iniziale_str = bilancio.bilancio_corrente_mens.get_data_iniziale().strftime('%d %B %Y')
        #dat_finale_str = bilancio.bilancio_corrente_mens.get_data_finale().strftime('%d %B %Y')
        #self.label_mese.setText('{dt1} - {dt2}'.format(dt1=dat_iniziale_str, dt2= dat_finale_str))
        data = datetime.date(self.bilancio.bilancio_corrente_mens.anno, self.bilancio.bilancio_corrente_mens.mese,day=1)
        self.label_mese.setText(data.strftime('%B %Y'))
        if self.checkBox_mese_entrate.isChecked() and not self.checkBox_mese_uscite.isChecked():
            l = len(bilancio.bilancio_corrente_mens.get_entrate_mensili())
            self.tableWidget_mensile.setRowCount(l)
            self.tableWidget_mensile.setColumnWidth(0, 130)
            for voce in bilancio.bilancio_corrente_mens.get_entrate_mensili():
                self.tableWidget_mensile.setItem(row_bilancio, 0, QtWidgets.QTableWidgetItem(voce[0].get_nome()))
                entrata = 'Sì'
                self.tableWidget_mensile.setItem(row_bilancio, 1, QtWidgets.QTableWidgetItem(entrata))
                self.tableWidget_mensile.setItem(row_bilancio, 2, QtWidgets.QTableWidgetItem(str(voce[1].date())))
                self.tableWidget_mensile.setItem(row_bilancio, 3, QtWidgets.QTableWidgetItem(
                    '{euro}.{cent}€'.format(euro=str(voce[0].get_valore_euro()[0]),
                                            cent=str(voce[0].get_valore_euro()[1]))))
                row_bilancio += 1
            ricavo_str = centToEuroString(bilancio_mens.get_ricavo())
            costi_str = centToEuroString(bilancio_mens.get_costi())
            utile_str = centToEuroString(bilancio_mens.get_utile())
            self.label_mese_ricavi_costi_utile.setText('Ricavi: {ricavi}    Costi: {costi}    Utile: {utile}'.format(ricavi = ricavo_str, costi  = costi_str, utile = utile_str))

        if (not self.checkBox_mese_entrate.isChecked()) and self.checkBox_mese_uscite.isChecked():
            l = len(bilancio.bilancio_corrente_mens.get_uscite_mensili())
            self.tableWidget_mensile.setRowCount(l)
            self.tableWidget_mensile.setColumnWidth(0, 130)
            for voce in bilancio.bilancio_corrente_mens.get_uscite_mensili():
                self.tableWidget_mensile.setItem(row_bilancio, 0, QtWidgets.QTableWidgetItem(voce[0].get_nome()))
                entrata = 'No'
                self.tableWidget_mensile.setItem(row_bilancio, 1, QtWidgets.QTableWidgetItem(entrata))
                self.tableWidget_mensile.setItem(row_bilancio, 2, QtWidgets.QTableWidgetItem(str(voce[1].date())))
                self.tableWidget_mensile.setItem(row_bilancio, 3, QtWidgets.QTableWidgetItem(
                    '{euro}.{cent}€'.format(euro=str(voce[0].get_valore_euro()[0]),
                                            cent=str(voce[0].get_valore_euro()[1]))))
                row_bilancio += 1
            ricavo_str = centToEuroString(bilancio_mens.get_ricavo())
            costi_str = centToEuroString(bilancio_mens.get_costi())
            utile_str = centToEuroString(bilancio_mens.get_utile())
            self.label_mese_ricavi_costi_utile.setText('Ricavi: {ricavi}    Costi: {costi}    Utile: {utile}'.format(ricavi = ricavo_str, costi  = costi_str, utile = utile_str))

        if not self.checkBox_mese_entrate.isChecked() and not self.checkBox_mese_uscite.isChecked():
            self.tableWidget_mensile.setRowCount(0)
            ricavo_str = centToEuroString(bilancio_mens.get_ricavo())
            costi_str = centToEuroString(bilancio_mens.get_costi())
            utile_str = centToEuroString(bilancio_mens.get_utile())
            self.label_mese_ricavi_costi_utile.setText('Ricavi: {ricavi}    Costi: {costi}    Utile: {utile}'.format(ricavi = ricavo_str, costi  = costi_str, utile = utile_str))
        if self.checkBox_mese_entrate.isChecked() and self.checkBox_mese_uscite.isChecked():
            l = len(bilancio.bilancio_corrente_mens.get_voci_mensili())
            self.tableWidget_mensile.setRowCount(l)
            self.tableWidget_mensile.setColumnWidth(0, 130)
            for voce in bilancio.bilancio_corrente_mens.get_voci_mensili():
                self.tableWidget_mensile.setItem(row_bilancio, 0, QtWidgets.QTableWidgetItem(voce[0].get_nome()))
                entrata = None
                if voce[2]:
                    entrata = 'Sì'
                else:
                    entrata = 'No'
                self.tableWidget_mensile.setItem(row_bilancio, 1, QtWidgets.QTableWidgetItem(entrata))
                self.tableWidget_mensile.setItem(row_bilancio, 2, QtWidgets.QTableWidgetItem(str(voce[1].date())))
                self.tableWidget_mensile.setItem(row_bilancio, 3, QtWidgets.QTableWidgetItem(
                    '{euro}.{cent}€'.format(euro=str(voce[0].get_valore_euro()[0]),
                                            cent=str(voce[0].get_valore_euro()[1]))))
                row_bilancio += 1
            ricavo_str = centToEuroString(bilancio_mens.get_ricavo())
            costi_str = centToEuroString(bilancio_mens.get_costi())
            utile_str = centToEuroString(bilancio_mens.get_ricavo() - bilancio_mens.get_costi())
            self.label_mese_ricavi_costi_utile.setText('Ricavi: {ricavi}    Costi: {costi}    Utile: {utile}'.format(ricavi = ricavo_str, costi  = costi_str, utile = utile_str))

        # STATISTICHE
        controllore_lista_dipendenti = ControlloreListaDipendenti()
        self.label_tot_dipendenti.setText("TOT DIPENDENTI:  " + str(controllore_lista_dipendenti.get_numero_dipendenti()))
        controllore_pianolavoro = ControllorePianoLavoro()
        self.label_tot_att_da_completare.setText("TOT. ATTIVITA' DA COMPLETARE:  " + str(controllore_pianolavoro.get_count_task_completate()))
        self.label_tot_att_completate.setText("TOT. ATTIVITA' COMPLETATE:  " + str(controllore_pianolavoro.get_count_task_da_completare()))
        controllore_magazzino = ControlloreListaProdottiSalvati()
        self.label_tot_frutta.setText("TOT. PRODOTTI 'FRUTTA' NEL MAGAZZINO:  " + str(controllore_magazzino.get_count_lista_frutta()))
        self.label_tot_verdura.setText("TOT. PRODOTTI 'VERDURA' NEL MAGAZZINO:  "+ str(controllore_magazzino.get_count_lista_verdura()))
        self.label_erbe_aromatiche.setText("TOT. PRODOTTI 'ERBE AROMATICHE' NEL MAGAZZINO:  "+ str(controllore_magazzino.get_count_lista_erbe_aromatiche()))
        self.label_altro.setText("TOT. PRODOTTI 'ALTRO' NEL MAGAZZINO:  "+ str(controllore_magazzino.get_count_lista_altro()))
        self.label_valore_magazzino.setText("TOT. VALORE MAGAZZINO:  " + str(controllore_magazzino.valore_totale()) + "€")
        controllore_ordini = ControlloreListaOrdinazioni()
        self.label_tot_ordinazioni.setText("TOT. ORDINAZIONI:  " + str(controllore_ordini.get_numero_ordinazioni()))

    def aggiorna_bilancio(self, bilancio):
        self.visualizzaBilancioSettimanale(bilancio)
        self.visualizzaBilancioMensile(bilancio)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_home.setText(_translate("MainWindow", "HOME"))
        self.label_tit_homepage.setText("Azienda Agricola \"LaGiuseppina\"")
        self.label_descrizione_sito.setText("Benvenuto nella Homepage! \n"
                                                                                     "Grazie a questo software avrai a disposizione degli efficaci strumenti per la gestione della tua azienda.  \n"
                                                                                     "Potrai infatti cliccare sulle 6 sezioni che vedi a sinistra per accedere alle diverse sezioni del programma \norganizzando cos\u00ec il tuo business in modo otttimale.")
        self.la_giuseppina.setWhatsThis(_translate("MainWindow",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:696; color:#ffffff;\">LaGiuseppina</span></p></body></html>"))
        self.la_giuseppina.setText(_translate("MainWindow", "LaGiuseppina"))
        self.push_dipendenti.setText(_translate("MainWindow", "DIPENDENTI"))
        self.push_pianodilavoro.setText(_translate("MainWindow", "PIANO DI LAVORO"))
        self.push_magazzino.setText(_translate("MainWindow", "MAGAZZINO"))
        self.push_clienti.setText(_translate("MainWindow", "CLIENTI"))
        self.push_contabilita.setText(_translate("MainWindow", "CONTABILITA\'"))
        self.push_statistiche.setText(_translate("MainWindow", "STATISTICHE"))

        tday = datetime.date.today()
        self.giorno.setText(_translate("MainWindow", str(tday.day)))

        mua = ["Gennaio",
               "Febbraio",
               "Marzo",
               "Aprile",
               "Maggio",
               "Giugno",
               "Luglio",
               "Agosto,",
               "Settembre",
               "Ottobre",
               "Novembre",
               "Dicembre"]

        muaj = mua[tday.month - 1]

        self.mese.setText(_translate("MainWindow", muaj))
        self.anno.setText(_translate("MainWindow", str(tday.year)))
        self.frame_listadeidipendenti_2.setText(_translate("MainWindow", "LISTA DEI DIPENDENTI"))
        self.push_visualizza.setText(_translate("MainWindow", "Visualizza"))
        self.push_modifica.setText(_translate("MainWindow", "Modifica"))
        self.push_elimina.setText(_translate("MainWindow", "Elimina"))
        self.push_creanuovodipendente.setText(_translate("MainWindow", "Crea un nuovo \n"
                                                                       " dipendente"))
        self.label_scritta.setText(_translate("MainWindow", "Crea un nuovo dipendente!"))
        self.label_nome.setText(_translate("MainWindow", "Nome"))
        self.label_oresettimanali.setText(_translate("MainWindow", "Ore settimanali"))
        self.label_pagaadora.setText(_translate("MainWindow", "Paga ad ora (€)"))
        self.label_tipodicontratto.setText(_translate("MainWindow", "Tipo di contratto"))
        self.label_email.setText(_translate("MainWindow", "E-mail"))
        self.label_telefono.setText(_translate("MainWindow", "Telefono"))
        self.pushButton_salva_dipendenti.setText(_translate("MainWindow", "Salva dipendente"))
        self.label_14.setText(_translate("MainWindow", "PIANO DI LAVORO"))
        self.label_oggi.setText(_translate("MainWindow", "Oggi"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_16.setText(_translate("MainWindow", "Domani"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.setSortingEnabled(__sortingEnabled)

        dit = ["Domenica",
               "Lunedì",
               "Martedì",
               "Mercoledì",
               "Giovedì",
               "Venerdì",
               "Sabato",
               "Domenica"]

        t2 = datetime.timedelta(days=2)
        t3 = datetime.timedelta(days=3)
        t4 = datetime.timedelta(days=4)
        t5 = datetime.timedelta(days=5)
        t6 = datetime.timedelta(days=6)

        dita2 = tday + t2
        dita3 = tday + t3
        dita4 = tday + t4
        dita5 = tday + t5
        dita6 = tday + t6

        self.label_17.setText(_translate("MainWindow", str(dit[dita2.isoweekday()]) + " " + str(dita2.day) + " " + str(
            mua[dita2.month - 1])))
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)

        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.label_18.setText(_translate("MainWindow", str(dit[dita3.isoweekday()]) + " " + str(dita3.day) + " " + str(
            mua[dita3.month - 1])))
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)

        self.listWidget_5.setSortingEnabled(__sortingEnabled)
        self.label_19.setText(_translate("MainWindow", str(dit[dita4.isoweekday()]) + " " + str(dita4.day) + " " + str(
            mua[dita4.month - 1])))
        __sortingEnabled = self.listWidget_6.isSortingEnabled()
        self.listWidget_6.setSortingEnabled(False)

        self.listWidget_6.setSortingEnabled(__sortingEnabled)
        self.label_20.setText(_translate("MainWindow", str(dit[dita5.isoweekday()]) + " " + str(dita5.day) + " " + str(
            mua[dita5.month - 1])))
        __sortingEnabled = self.listWidget_7.isSortingEnabled()
        self.listWidget_7.setSortingEnabled(False)

        self.listWidget_7.setSortingEnabled(__sortingEnabled)
        self.label_21.setText(_translate("MainWindow", str(dit[dita6.isoweekday()]) + " " + str(dita6.day) + " " + str(
            mua[dita6.month - 1])))
        __sortingEnabled = self.listWidget_8.isSortingEnabled()
        self.listWidget_8.setSortingEnabled(False)

        self.listWidget_8.setSortingEnabled(__sortingEnabled)
        self.push_listadelleattivita.setText(_translate("MainWindow", "LISTA DELLE ATTIVITA\'"))
        self.push_eliminapianodilavoro.setText(_translate("MainWindow", "ELIMINA PIANO DI LAVORO"))
        self.label_35.setText(_translate("MainWindow", "MAGAZZINO"))
        self.label_37.setText(_translate("MainWindow", "Frutta"))
        self.label_36.setText(_translate("MainWindow", "Erbe aromatiche"))
        self.label_38.setText(_translate("MainWindow", "Verdura"))
        self.label_39.setText(_translate("MainWindow", "Altro"))

        self.push_mag_listaprodotti.setText(_translate("MainWindow", "LISTA DEI PRODOTTI"))
        self.push_mag_salva.setText(_translate("MainWindow", "SALVA"))
        self.frame_listadelleordinazioni.setText(_translate("MainWindow", "LISTA DELLE ORDINAZIONI"))
        __sortingEnabled = self.listWidget_ordini.isSortingEnabled()
        self.listWidget_ordini.setSortingEnabled(False)
        self.listWidget_ordini.setSortingEnabled(__sortingEnabled)
        self.push_visualizza_ordine.setText(_translate("MainWindow", "Visualizza"))
        self.push_elimina_ordine.setText(_translate("MainWindow", "Elimina"))
        self.push_creanuovoordine.setText(_translate("MainWindow", "Crea un nuovo \n"
                                                                   " ordine"))
        self.label_scritta_crea_ordine.setText(_translate("MainWindow", "Crea un nuovo ordine!"))
        self.label_nome_cliente.setText(_translate("MainWindow", "Nome cliente"))
        self.label_indirizzo.setText(_translate("MainWindow", "Indirizzo di consegna"))
        self.label_pagaadora_2.setText(_translate("MainWindow", "Giorno della consegna"))
        self.label_quantita.setText(_translate("MainWindow", "Prodotti"))
        self.push_aggiungi_prodotti.setText(_translate("MainWindow", "+"))
        self.pushButton_salva_ordine.setText(_translate("MainWindow", "Salva ordine"))
        self.label_scritta_mod_ordine.setText(_translate("MainWindow", "Ordine di Mario Rossi!"))
        self.label_mod_cliente.setText(_translate("MainWindow", "Nome cliente"))
        self.label_mod_indirizzo.setText(_translate("MainWindow", "Indirizzo di consegna"))
        self.label_pagaadora_7.setText(_translate("MainWindow", "Giorno della consegna"))
        self.label_mod_prodotti.setText(_translate("MainWindow", "Prodotti"))
        self.comboBox_mod_prodotti.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox_mod_prodotti.setItemText(1, _translate("MainWindow", "New Item"))
        self.pushButton_modi_aggiungi_prodotto.setText(_translate("MainWindow", "+"))
        self.pushButton_rimuovi_prodotto.setText(_translate("MainWindow", "-"))
        item = self.tableWidget_mod_prodotti.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_mod_prodotti.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Quantita"))
        self.pushButton_modifica_dipendenti.setText(_translate("MainWindow", "Salva ordine"))
        self.label_contabilita.setText(_translate("MainWindow", "CONTABILITA\'"))
        self.push_sett_prec.setText(_translate("MainWindow", "<"))
        self.label_settimana.setText(_translate("MainWindow", "SETTIMANA 25/04 - 1/05"))
        self.push_sett_succ.setText(_translate("MainWindow", ">"))
        item = self.tableWidget_settimanale.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Voce"))
        item = self.tableWidget_settimanale.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Entrata?"))
        item = self.tableWidget_settimanale.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidget_settimanale.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valore (€)"))
        self.checkBox_sett_entrate.setText(_translate("MainWindow", "Entrate"))
        self.checkBox_sett_uscite.setText(_translate("MainWindow", "Uscite"))
        self.label_sett_ricavi_costi_utile.setText(_translate("MainWindow", "Ricavi:    Costi:    Utile: "))
        self.tabWidget_contabilita.setTabText(self.tabWidget_contabilita.indexOf(self.settimanale),
                                              _translate("MainWindow", "Settimanale"))
        self.push_mese_prec.setText(_translate("MainWindow", "<"))
        self.label_mese.setText(_translate("MainWindow", "APRILE 2022"))
        self.push_mese_succ.setText(_translate("MainWindow", ">"))
        item = self.tableWidget_mensile.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", '1'))
        item = self.tableWidget_mensile.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", '2'))
        item = self.tableWidget_mensile.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", '3'))
        item = self.tableWidget_mensile.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Voce"))
        item = self.tableWidget_mensile.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Entrata?"))
        item = self.tableWidget_mensile.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidget_mensile.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valore (€)"))
        self.checkBox_mese_entrate.setText(_translate("MainWindow", "Entrate"))
        self.checkBox_mese_uscite.setText(_translate("MainWindow", "Uscite"))
        self.label_mese_ricavi_costi_utile.setText(_translate("MainWindow", "Ricavi:    Costi:    Utile:"))
        self.tabWidget_contabilita.setTabText(self.tabWidget_contabilita.indexOf(self.mensile),
                                              _translate("MainWindow", "Mensile"))
        self.pushButton_vocidibilancio.setText(_translate("MainWindow", "Voci di bilancio"))
        self.label.setText("STATISTICHE")


