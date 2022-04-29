import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Progetto.listaprodotti.controller.ControlloreListaProdottiSalvati import ControlloreListaProdottiSalvati
from Progetto.listaprodotti.model.Prodotto import Prodotto
from Progetto.magazzino.controller import ControlloreListaMagazzino


class VistaProdottiMagazzino(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 670)
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
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_frutta = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_frutta.setMinimumSize(QtCore.QSize(110, 30))
        self.pushButton_frutta.setStyleSheet("font: 400 14pt \"Apple SD Gothic Neo\";\n"
                                             "background-color: rgb(219, 0, 0);\n"
                                             "border-top-color: rgb(255, 0, 26);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius: 12px;")
        self.pushButton_frutta.setObjectName("pushButton_frutta")
        self.verticalLayout_4.addWidget(self.pushButton_frutta)
        self.pushButton_verdura = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_verdura.setMinimumSize(QtCore.QSize(110, 30))
        self.pushButton_verdura.setStyleSheet("font: 400 14pt \"Apple SD Gothic Neo\";\n"
                                              "border-top-color: rgb(255, 0, 26);\n"
                                              "background-color: rgb(0, 160, 0);\n"
                                              "border-radius: 12px;\n"
                                              "color: rgb(255, 255, 255);")
        self.pushButton_verdura.setObjectName("pushButton_verdura")
        self.verticalLayout_4.addWidget(self.pushButton_verdura)
        self.pushButton_erbe = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_erbe.setMinimumSize(QtCore.QSize(110, 30))
        self.pushButton_erbe.setStyleSheet("font: 400 14pt \"Apple SD Gothic Neo\";\n"
                                           "border-top-color: rgb(255, 0, 26);\n"
                                           "background-color: rgb(254, 160, 0);\n"
                                           "border-radius: 12px;\n"
                                           "color: rgb(255, 255, 255);")
        self.pushButton_erbe.setObjectName("pushButton_erbe")
        self.verticalLayout_4.addWidget(self.pushButton_erbe)
        self.pushButton_altro = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_altro.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_altro.setMaximumSize(QtCore.QSize(167777, 16777215))
        self.pushButton_altro.setStyleSheet("font: 400 14pt \"Apple SD Gothic Neo\";\n"
                                            "border-top-color: rgb(255, 0, 26);\n"
                                            "background-color: rgb(112, 112, 112);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 12px;")
        self.pushButton_altro.setObjectName("pushButton_altro")
        self.verticalLayout_4.addWidget(self.pushButton_altro)
        self.frame_18 = QtWidgets.QFrame(self.frame_5)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_4.addWidget(self.frame_18)
        self.pushButton_mostra_tutto = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_mostra_tutto.setMinimumSize(QtCore.QSize(110, 40))
        self.pushButton_mostra_tutto.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                                   "border-top-color: rgb(255, 0, 26);\n"
                                                   "background-color: rgb(255, 255, 255);\n"
                                                   "color: rgb(0,0,0);"
                                                   "border-radius: 12px;")
        self.pushButton_mostra_tutto.setObjectName("pushButton_mostra_tutto")
        self.verticalLayout_4.addWidget(self.pushButton_mostra_tutto)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.listWidget_prodotti = QtWidgets.QListWidget(self.frame_4)
        self.listWidget_prodotti.setStyleSheet("background-color: rgb(255, 255, 255);"
                                               "color: rgb(0,0,0);"
                                               "font-size: 15px;")
        self.listWidget_prodotti.setObjectName("listWidget_prodotti")
        self.horizontalLayout_2.addWidget(self.listWidget_prodotti)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 12)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_visualizza = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_visualizza.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_visualizza.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                                 "border-top-color: rgb(255, 0, 26);\n"
                                                 "background-color: rgb(255, 255, 255);\n"
                                                 "color: rgb(0,0,0);"
                                                 "border-radius: 12px;")
        self.pushButton_visualizza.setObjectName("pushButton_visualizza")
        self.verticalLayout_2.addWidget(self.pushButton_visualizza)
        self.pushButton_modifica = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_modifica.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_modifica.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                               "border-top-color: rgb(255, 0, 26);\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "color: rgb(0,0,0);"
                                               "border-radius: 12px;")
        self.pushButton_modifica.setObjectName("pushButton_modifica")
        self.verticalLayout_2.addWidget(self.pushButton_modifica)
        self.pushButton_elimina = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_elimina.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_elimina.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                              "border-top-color: rgb(255, 0, 26);"
                                              "color: rgb(0,0,0);\n"
                                              "background-color: rgb(255, 255, 255);\n"
                                              "border-radius: 12px;")
        self.pushButton_elimina.setObjectName("pushButton_elimina")
        self.verticalLayout_2.addWidget(self.pushButton_elimina)
        self.pushButton_crea_prodotto = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_crea_prodotto.setMinimumSize(QtCore.QSize(120, 42))
        self.pushButton_crea_prodotto.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                                    "border-top-color: rgb(255, 0, 26);\n"
                                                    "background-color: rgb(0, 122, 254);\n"
                                                    "border-radius: 17px;\n"
                                                    "color: rgb(255, 255, 255);")
        self.pushButton_crea_prodotto.setObjectName("pushButton_crea_prodotto")
        self.verticalLayout_2.addWidget(self.pushButton_crea_prodotto)
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
        self.page_visualizza_prodotto = QtWidgets.QWidget()
        self.page_visualizza_prodotto.setObjectName("page_visualizza_prodotto")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_visualizza_prodotto)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_nome_titolo = QtWidgets.QLabel(self.page_visualizza_prodotto)
        self.label_nome_titolo.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_nome_titolo.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                             "color: rgb(0, 0, 0);")
        self.label_nome_titolo.setObjectName("label_nome_titolo")
        self.verticalLayout_3.addWidget(self.label_nome_titolo)
        self.frame_bianco = QtWidgets.QFrame(self.page_visualizza_prodotto)
        self.frame_bianco.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 16px;\n"
                                        "")
        self.frame_bianco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bianco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bianco.setObjectName("frame_bianco")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_bianco)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_nome_prodotto = QtWidgets.QLabel(self.frame_bianco)
        self.label_nome_prodotto.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                               "color: rgb(0,0,0);")
        self.label_nome_prodotto.setObjectName("label_nome_prodotto")
        self.verticalLayout_5.addWidget(self.label_nome_prodotto)
        self.label_categoria = QtWidgets.QLabel(self.frame_bianco)
        self.label_categoria.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                           "color: rgb(0,0,0);")
        self.label_categoria.setObjectName("label_categoria")
        self.verticalLayout_5.addWidget(self.label_categoria)
        self.label_tip_unita = QtWidgets.QLabel(self.frame_bianco)
        self.label_tip_unita.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                           "color: rgb(0,0,0);")
        self.label_tip_unita.setObjectName("label_tip_unita")
        self.verticalLayout_5.addWidget(self.label_tip_unita)
        self.label_prezzo_unita = QtWidgets.QLabel(self.frame_bianco)
        self.label_prezzo_unita.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                              "color: rgb(0,0,0);")
        self.label_prezzo_unita.setObjectName("label_prezzo_unita")
        self.verticalLayout_5.addWidget(self.label_prezzo_unita)
        self.verticalLayout_3.addWidget(self.frame_bianco)
        self.stackedWidget.addWidget(self.page_visualizza_prodotto)
        self.page_crea_prodotto = QtWidgets.QWidget()
        self.page_crea_prodotto.setObjectName("page_crea_prodotto")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_crea_prodotto)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.page_crea_prodotto)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_7.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                   "color: rgb(0,0,0);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.frame_biannco_2 = QtWidgets.QFrame(self.page_crea_prodotto)
        self.frame_biannco_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-radius: 16px;\n"
                                           "")

        self.frame_biannco_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_biannco_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_biannco_2.setObjectName("frame_biannco_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_biannco_2)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_biannco_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(-1, 12, 200, 12)
        self.horizontalLayout_4.setSpacing(25)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                   "color: rgb(0,0,0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_nome.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_nome.setStyleSheet("border-radius: 10px;\n"
                                         "background-color: rgb(235, 235, 235);"
                                         "color: rgb(0,0,0);")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.horizontalLayout_4.addWidget(self.lineEdit_nome)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_biannco_2)
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
                                   "color: rgb(0,0,0);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.comboBox_categoria = QtWidgets.QComboBox(self.frame_9)
        self.comboBox_categoria.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_categoria.setStyleSheet("border-radius: 10px;\n"
                                              "background-color: rgb(235, 235, 235);"
                                              "color: rgb(0,0,0);")
        self.comboBox_categoria.setObjectName("comboBox_categoria")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_categoria)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_biannco_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setContentsMargins(-1, -1, 400, -1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        self.label_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_10.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.comboBox_tpo_unita = QtWidgets.QComboBox(self.frame_10)
        self.comboBox_tpo_unita.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_tpo_unita.setStyleSheet("border-radius: 10px;\n"
                                              "background-color: rgb(235, 235, 235);"
                                              "color: rgb(0,0,0);")
        self.comboBox_tpo_unita.setObjectName("comboBox_tpo_unita")
        self.comboBox_tpo_unita.addItem("")
        self.comboBox_tpo_unita.addItem("")
        self.comboBox_tpo_unita.addItem("")
        self.comboBox_tpo_unita.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_tpo_unita)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.frame_8 = QtWidgets.QFrame(self.frame_biannco_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setContentsMargins(-1, -1, 410, -1)
        self.horizontalLayout_9.setSpacing(40)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                   "color: rgb(0,0,0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.doubleSpinBox_prezzo_unita = QtWidgets.QDoubleSpinBox(self.frame_8)
        self.doubleSpinBox_prezzo_unita.setMinimumSize(QtCore.QSize(0, 25))
        self.doubleSpinBox_prezzo_unita.setStyleSheet("border-radius: 10px;\n"
                                                      "background-color: rgb(235, 235, 235);"
                                                      "color: rgb(0,0,0);")
        self.doubleSpinBox_prezzo_unita.setObjectName("doubleSpinBox_prezzo_unita")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_prezzo_unita)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.frame_11 = QtWidgets.QFrame(self.frame_biannco_2)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setContentsMargins(400, 0, 110, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_salva_prodotto = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_salva_prodotto.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_salva_prodotto.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                                     "border-top-color: rgb(255, 0, 26);\n"
                                                     "background-color: rgb(0, 122, 254);\n"
                                                     "border-radius: 17px;\n"
                                                     "color: rgb(255, 255, 255);")
        self.pushButton_salva_prodotto.setObjectName("pushButton_salva_prodotto")
        self.horizontalLayout_8.addWidget(self.pushButton_salva_prodotto)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.verticalLayout_6.addWidget(self.frame_biannco_2)
        self.stackedWidget.addWidget(self.page_crea_prodotto)
        self.page_modifica_prodotto = QtWidgets.QWidget()
        self.page_modifica_prodotto.setObjectName("page_modifica_prodotto")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_modifica_prodotto)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.page_modifica_prodotto)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_12.setStyleSheet("font: 800 20pt \"Apple SD Gothic Neo\";"
                                    "color: rgb(0,0,0);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.frame_biannco_3 = QtWidgets.QFrame(self.page_modifica_prodotto)
        self.frame_biannco_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-radius: 16px;\n"
                                           "")
        self.frame_biannco_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_biannco_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_biannco_3.setObjectName("frame_biannco_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_biannco_3)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_12 = QtWidgets.QFrame(self.frame_biannco_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setContentsMargins(-1, 12, 200, 12)
        self.horizontalLayout_10.setSpacing(25)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.frame_12)
        self.label_13.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.lineEdit_mod_nome = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_mod_nome.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_mod_nome.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(235, 235, 235);"
                                             "color: rgb(0,0,0);")
        self.lineEdit_mod_nome.setObjectName("lineEdit_mod_nome")
        self.horizontalLayout_10.addWidget(self.lineEdit_mod_nome)
        self.verticalLayout_8.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_biannco_3)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setContentsMargins(-1, 8, 350, 8)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.frame_13)
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_14.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.comboBox_mod_categoria = QtWidgets.QComboBox(self.frame_13)
        self.comboBox_mod_categoria.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_mod_categoria.setStyleSheet("border-radius: 10px;\n"
                                                  "background-color: rgb(235, 235, 235);"
                                                  "color: rgb(0,0,0);")
        self.comboBox_mod_categoria.setObjectName("comboBox_mod_categoria")
        self.comboBox_mod_categoria.addItem("")
        self.comboBox_mod_categoria.addItem("")
        self.comboBox_mod_categoria.addItem("")
        self.comboBox_mod_categoria.addItem("")
        self.comboBox_mod_categoria.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_mod_categoria)
        self.verticalLayout_8.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_biannco_3)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setContentsMargins(-1, -1, 400, -1)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.frame_14)
        self.label_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_15.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                    "color: rgb(0,0,0);")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.comboBox_mod_tipo_unita = QtWidgets.QComboBox(self.frame_14)
        self.comboBox_mod_tipo_unita.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_mod_tipo_unita.setStyleSheet("border-radius: 10px;\n"
                                                   "background-color: rgb(235, 235, 235);"
                                                   "color: rgb(0,0,0);")
        self.comboBox_mod_tipo_unita.setObjectName("comboBox_mod_tipo_unita")
        self.comboBox_mod_tipo_unita.addItem("")
        self.comboBox_mod_tipo_unita.addItem("")
        self.comboBox_mod_tipo_unita.addItem("")
        self.comboBox_mod_tipo_unita.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_mod_tipo_unita)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.frame_16 = QtWidgets.QFrame(self.frame_biannco_3)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setContentsMargins(-1, -1, 410, -1)
        self.horizontalLayout_14.setSpacing(40)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_3 = QtWidgets.QLabel(self.frame_16)
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_3.setStyleSheet("font: 400 15pt \"SF Pro\";"
                                   "color: rgb(0,0,0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_14.addWidget(self.label_3)
        self.doubleSpinBox_mod_prezzo_unita = QtWidgets.QDoubleSpinBox(self.frame_16)
        self.doubleSpinBox_mod_prezzo_unita.setMinimumSize(QtCore.QSize(0, 25))
        self.doubleSpinBox_mod_prezzo_unita.setStyleSheet("border-radius: 10px;\n"
                                                          "background-color: rgb(235, 235, 235);"
                                                          "color: rgb(0,0,0);")
        self.doubleSpinBox_mod_prezzo_unita.setObjectName("doubleSpinBox_mod_prezzo_unita")
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_mod_prezzo_unita)
        self.verticalLayout_8.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_biannco_3)
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setContentsMargins(400, 0, 110, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_modifca_prodotto = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_modifca_prodotto.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_modifca_prodotto.setStyleSheet("font: 700 15pt \"Apple SD Gothic Neo\";\n"
                                                       "border-top-color: rgb(255, 0, 26);\n"
                                                       "background-color: rgb(0, 122, 254);\n"
                                                       "border-radius: 17px;\n"
                                                       "color: rgb(255, 255, 255);")
        self.pushButton_modifca_prodotto.setObjectName("pushButton_modifca_prodotto")
        self.horizontalLayout_15.addWidget(self.pushButton_modifca_prodotto)
        self.verticalLayout_8.addWidget(self.frame_17)
        self.verticalLayout_9.addWidget(self.frame_biannco_3)
        self.stackedWidget.addWidget(self.page_modifica_prodotto)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lista_prodotti_salvati = ControlloreListaProdottiSalvati()

        for prodotto_salvato in self.lista_prodotti_salvati.get_lista():
            self.listWidget_prodotti.addItem(prodotto_salvato.get_nome())
        #self.listWidget_prodotti.sortItems()


        def visualizza_frutta():
            self.listWidget_prodotti.clear()
            self.listWidget_prodotti.setStyleSheet("background-color: rgb(255,255,255);"
                                                   "color: rgb(255,0,0);"
                                                   "font-size: 15px;")
            for frutto in self.lista_prodotti_salvati.get_lista_frutta():
                self.listWidget_prodotti.addItem(frutto["nome"])
            #self.listWidget_prodotti.sortItems()

        self.pushButton_frutta.clicked.connect(lambda: visualizza_frutta())

        def visualizza_verdura():
            self.listWidget_prodotti.clear()
            self.listWidget_prodotti.setStyleSheet("background-color: rgb(255,255,255);"
                                                   "color: rgb(0,100,0);"
                                                   "font-size: 15px;")
            for verdura in self.lista_prodotti_salvati.get_lista_verdura():
                self.listWidget_prodotti.addItem(verdura["nome"])
            #self.listWidget_prodotti.sortItems()

        self.pushButton_verdura.clicked.connect(lambda: visualizza_verdura())

        def visualizza_erbe_aromatcihe():
            self.listWidget_prodotti.clear()
            self.listWidget_prodotti.setStyleSheet("background-color: rgb(255,255,255);"
                                                   "color: rgb(255,211,25);"
                                                   "font-size: 15px;")
            for erba_aromatica in self.lista_prodotti_salvati.get_lista_erbe_aromatiche():
                self.listWidget_prodotti.addItem(erba_aromatica["nome"])
            #self.listWidget_prodotti.sortItems()

        self.pushButton_erbe.clicked.connect(lambda: visualizza_erbe_aromatcihe())

        def visualizza_altro():
            self.listWidget_prodotti.clear()
            self.listWidget_prodotti.setStyleSheet("background-color: rgb(255,255,255);"
                                                   "color: rgb(169, 169, 169);"
                                                   "font-size: 15px;")
            for altro in self.lista_prodotti_salvati.get_lista_altro():
                self.listWidget_prodotti.addItem(altro["nome"])
            #self.listWidget_prodotti.sortItems()
        self.pushButton_altro.clicked.connect(lambda: visualizza_altro())

        def visualizza_tutto():
            self.listWidget_prodotti.clear()
            self.listWidget_prodotti.setStyleSheet("background-color: rgb(255,255,255);"
                                                   "color: rgb(0,0,0);"
                                                   "font-size: 15px;")
            lista_prod_salvati = ControlloreListaProdottiSalvati()
            for prodotto_salvato in lista_prod_salvati.get_lista():
                self.listWidget_prodotti.addItem(prodotto_salvato.get_nome())
            #self.listWidget_prodotti.sortItems()
        self.pushButton_mostra_tutto.clicked.connect(lambda: visualizza_tutto())

        def page_nuovo_prodotto():
            self.stackedWidget.setCurrentWidget(self.page_crea_prodotto)

            def salva_nuovo_prodotto():
                nome_prodotto = self.lineEdit_nome.text().capitalize()
                categoria = self.comboBox_categoria.currentText()
                tipo_unita = self.comboBox_tpo_unita.currentText()
                prezzo_su_unita = self.doubleSpinBox_prezzo_unita.value()

                if nome_prodotto == "" or categoria == "" or tipo_unita == "" or prezzo_su_unita == 0.0:
                    QMessageBox.setStyleSheet(MainWindow,
                                              "color: rgb(0, 0, 0); background-color: rgb(235, 235, 235); border:none")
                    QMessageBox.critical(MainWindow, 'ERRORE!', 'Completa correttamente tutti i campi richiesti!',
                                         QMessageBox.Ok,
                                         QMessageBox.Ok)
                else:

                    prodotto_creato = {
                        "nome": nome_prodotto,
                        "categoria": categoria,
                        "tipo_unita": tipo_unita,
                        "prezzo_su_unita": prezzo_su_unita,
                        "quantita": 0
                    }
                    with open("listaprodotti/data/ListaProdottiSalvati.json", "r+") as file:
                        data = json.load(file)
                        data.append(prodotto_creato)
                        file.seek(0)
                        json.dump(data, file, indent=4)
                    self.listWidget_prodotti.addItem(nome_prodotto)
                    #self.listWidget_prodotti.sortItems()
                    self.lineEdit_nome.clear()
                    self.comboBox_categoria.setCurrentIndex(0)
                    self.comboBox_tpo_unita.setCurrentIndex(0)
                    self.doubleSpinBox_prezzo_unita.setValue(0.00)

                    QMessageBox.about(MainWindow, "", "Il nuovo prodotto è stato salvato con successo!")
                    QMessageBox.setStyleSheet(MainWindow, "color: rgb(0,0,0);"
                                                          "background-color: rgb(235, 235, 235);"
                                                          "border: none;")
            self.pushButton_salva_prodotto.clicked.connect(lambda: salva_nuovo_prodotto())
        self.pushButton_crea_prodotto.clicked.connect(lambda: page_nuovo_prodotto())


        def elimina_prodotto():
          try:
            indice_di_controllo = self.listWidget_prodotti.selectedIndexes()[0].row()
            nomeselezionato = self.listWidget_prodotti.currentItem().text()

            QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0);"
                                                  "background-color: rgb(235, 235, 235);"
                                                  "border: none")
            q = QMessageBox.question(MainWindow, '', "Sei sicuro di voler eliminare " + "'" + nomeselezionato + "'" + " dalla lista dei prodotti?", QMessageBox.Yes | QMessageBox.No)

            if q == QMessageBox.Yes:
              with open('listaprodotti/data/ListaProdottiSalvati.json') as f:
                prodotti = json.load(f)
                i = 0
                for prodotto in prodotti:
                  if prodotto["nome"] == nomeselezionato:
                     del prodotti[i]
                  else:
                     i = i+1


              with open("listaprodotti/data/ListaProdottiSalvati.json", 'w') as f:
                json.dump(prodotti, f, indent=4)

              with open('listaprodotti/data/ListaProdottiSalvati.json') as f:
                prodotti_aggiornati = json.load(f)
                self.listWidget_prodotti.clear()

              for prodotto_salvato in prodotti_aggiornati:
                self.listWidget_prodotti.addItem(prodotto_salvato["nome"])
              QMessageBox.about(MainWindow, "",
                                "Il prodotto '" + nomeselezionato + "' è stata eliminato dalla lista dei prodotti!")
              QMessageBox.setStyleSheet(MainWindow, "color: rgb(0, 0, 0);"
                                                    "background-color: rgb(235, 235, 235);"
                                                    "border: none;")

          except Exception:
              QMessageBox.setStyleSheet(MainWindow,
                                        "color: rgb(0, 0, 0); background-color: rgb(235, 235, 235); border:none;")
              QMessageBox.critical(MainWindow, 'ERRORE!',
                                   "Selezionare prima un prodotto dalla lista!",
                                   QMessageBox.Ok, QMessageBox.Ok)
        self.pushButton_elimina.clicked.connect(lambda: elimina_prodotto())


        def visualizza_prodotto():
          try:
            indice_di_controllo = self.listWidget_prodotti.selectedIndexes()[0].row()
            lista = ControlloreListaProdottiSalvati()
            self.stackedWidget.setCurrentWidget(self.page_visualizza_prodotto)
            nomeselezionato = self.listWidget_prodotti.currentItem().text()
            for prodotto_salvato in lista.get_lista():
                if prodotto_salvato.get_nome() == nomeselezionato:
                    self.label_nome_titolo.setText(prodotto_salvato.get_nome())
                    self.label_nome_prodotto.setText("Nome del prodotto:  " + prodotto_salvato.get_nome())
                    self.label_categoria.setText("Categoria:  " + prodotto_salvato.get_categoria())
                    self.label_tip_unita.setText("Tipo unità:  " + prodotto_salvato.get_tipo_unita())
                    self.label_prezzo_unita.setText("Prezzo per unità:  " + str(prodotto_salvato.get_prezzo_su_unita()) + "€")
          except Exception:
              QMessageBox.setStyleSheet(MainWindow,
                                        "color: rgb(0, 0, 0); background-color: rgb(235, 235, 235); border:none;")
              QMessageBox.critical(MainWindow, 'ERRORE!',
                                   "Selezionare prima un prodotto dalla lista!",
                                   QMessageBox.Ok, QMessageBox.Ok)

        self.pushButton_visualizza.clicked.connect(lambda: visualizza_prodotto())


        def page_modifica_prodotto():

            indice_di_controllo = self.listWidget_prodotti.selectedIndexes()[0].row()
            self.stackedWidget.setCurrentWidget(self.page_modifica_prodotto)
            nomeselezionato = self.listWidget_prodotti.currentItem().text()

            lista = ControlloreListaProdottiSalvati()

            for prodotto_salvato in lista.get_lista():
                if prodotto_salvato.get_nome() == nomeselezionato:
                   self.label_12.setText(prodotto_salvato.get_nome())
                   self.lineEdit_mod_nome.setText(prodotto_salvato.get_nome())

                   if prodotto_salvato.get_categoria() == "Frutta":
                      index = 1
                   elif prodotto_salvato.get_categoria() == "Verdura":
                      index = 2
                   elif prodotto_salvato.get_categoria() == "Erbe aromatiche":
                      index = 3
                   else:
                      index = 4
                   self.comboBox_mod_categoria.setCurrentIndex(index)

                   if prodotto_salvato.get_tipo_unita() == "al chilo":
                      indice = 1
                   elif prodotto_salvato.get_tipo_unita() == "al litro":
                      indice = 2
                   else:
                      indice = 3
                   self.comboBox_mod_tipo_unita.setCurrentIndex(indice)

                   self.doubleSpinBox_mod_prezzo_unita.setValue(prodotto_salvato.get_prezzo_su_unita())

            def salva_prodotto_salvato():
              nomeselezionato = self.listWidget_prodotti.currentItem().text()
              lista = ControlloreListaProdottiSalvati()
              i = lista.get_index_by_name(nomeselezionato)

              with open("listaprodotti/data/ListaProdottiSalvati.json", "r") as f:
                lista_prodotti = json.load(f)
              with open("listaprodotti/data/ListaProdottiSalvati.json", "w") as f:


                self.label_12.setText(self.lineEdit_mod_nome.text())
                lista_prodotti[i]['nome'] = self.lineEdit_mod_nome.text().capitalize()
                lista_prodotti[i]['categoria'] = self.comboBox_mod_categoria.currentText()
                lista_prodotti[i]['tipo_unita'] = self.comboBox_mod_tipo_unita.currentText()
                lista_prodotti[i]['prezzo_su_unita'] = self.doubleSpinBox_mod_prezzo_unita.value()


                json.dump(lista_prodotti, f, indent=4)

              self.listWidget_prodotti.clear()
              for elem in lista_prodotti:
                    self.listWidget_prodotti.addItem(elem['nome'])

            self.pushButton_modifca_prodotto.clicked.connect(lambda: salva_prodotto_salvato())

        self.pushButton_modifica.clicked.connect(lambda: page_modifica_prodotto())

        self.stackedWidget.setCurrentIndex(0)

        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_frutta.setText(_translate("MainWindow", "Frutta"))
        self.pushButton_verdura.setText(_translate("MainWindow", "Verdura"))
        self.pushButton_erbe.setText(_translate("MainWindow", "Erbe aromatiche"))
        self.pushButton_altro.setText(_translate("MainWindow", "Altro"))
        self.pushButton_mostra_tutto.setText(_translate("MainWindow", "Mostra tutto"))
        self.pushButton_visualizza.setText(_translate("MainWindow", "Visualizza"))
        self.pushButton_modifica.setText(_translate("MainWindow", "Modifica"))
        self.pushButton_elimina.setText(_translate("MainWindow", "Elimina"))
        self.pushButton_crea_prodotto.setText(_translate("MainWindow", "Crea un \n"
                                                                       " nuovo prodotto"))

        self.label_7.setText(_translate("MainWindow", "Crea una nuovo prodotto!"))
        self.label_8.setText(_translate("MainWindow", "Nome prodotto: "))
        self.label_9.setText(_translate("MainWindow", "Categoria: "))
        self.comboBox_categoria.setItemText(0, _translate("MainWindow", ""))
        self.comboBox_categoria.setItemText(1, _translate("MainWindow", "Frutta"))
        self.comboBox_categoria.setItemText(2, _translate("MainWindow", "Verdura"))
        self.comboBox_categoria.setItemText(3, _translate("MainWindow", "Erbe aromatiche"))
        self.comboBox_categoria.setItemText(4, _translate("MainWindow", "Altro"))
        self.label_10.setText(_translate("MainWindow", "Tipo unità:"))
        self.comboBox_tpo_unita.setItemText(0, _translate("MainWindow", ""))
        self.comboBox_tpo_unita.setItemText(1, _translate("MainWindow", "al chilo"))
        self.comboBox_tpo_unita.setItemText(2, _translate("MainWindow", "al litro"))
        self.comboBox_tpo_unita.setItemText(3, _translate("MainWindow", "al pezzo"))
        self.label_2.setText(_translate("MainWindow", "Prezzo per unità:"))
        self.pushButton_salva_prodotto.setText(_translate("MainWindow", "Salva prodotto"))
        self.label_12.setText(_translate("MainWindow", "Uva"))
        self.label_13.setText(_translate("MainWindow", "Nome prodotto: "))
        self.label_14.setText(_translate("MainWindow", "Categoria: "))
        self.comboBox_mod_categoria.setItemText(0, _translate("MainWindow", ""))
        self.comboBox_mod_categoria.setItemText(1, _translate("MainWindow", "Frutta"))
        self.comboBox_mod_categoria.setItemText(2, _translate("MainWindow", "Verdura"))
        self.comboBox_mod_categoria.setItemText(3, _translate("MainWindow", "Erbe aromatiche"))
        self.comboBox_mod_categoria.setItemText(4, _translate("MainWindow", "Altro"))
        self.label_15.setText(_translate("MainWindow", "Tipo unità:"))
        self.comboBox_mod_tipo_unita.setItemText(0, _translate("MainWindow", ""))
        self.comboBox_mod_tipo_unita.setItemText(1, _translate("MainWindow", "al chilo"))
        self.comboBox_mod_tipo_unita.setItemText(2, _translate("MainWindow", "al litro"))
        self.comboBox_mod_tipo_unita.setItemText(3, _translate("MainWindow", "al pezzo"))
        self.label_3.setText(_translate("MainWindow", "Prezzo per unità:"))
        self.pushButton_modifca_prodotto.setText(_translate("MainWindow", "Modifica prodotto"))
