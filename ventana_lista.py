from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow

from ui_lista import Ui_ListWindow


class ListWindow(QMainWindow):
    def __init__(self):
        super(ListWindow, self).__init__()
        self.ui = Ui_ListWindow()
        self.ui.setupUi(self)

    def agregar_row(self, persona):
        row_position = self.ui.tb_covid.rowCount()
        self.ui.tb_covid.insertRow(row_position)
        self.ui.tb_covid.setItem(row_position, 0, QtWidgets.QTableWidgetItem(persona.dni))
        self.ui.tb_covid.setItem(row_position, 1, QtWidgets.QTableWidgetItem(persona.nombre))
        self.ui.tb_covid.setItem(row_position, 2, QtWidgets.QTableWidgetItem(persona.apellido))
        self.ui.tb_covid.setItem(row_position, 3, QtWidgets.QTableWidgetItem(persona.fecha.toString()))
