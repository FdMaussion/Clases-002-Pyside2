import sys
import pickle

import requests
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, QDate, QSettings
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox

from ui_principal import Ui_MainWindow
from ventana_lista import ListWindow

from persona import Persona


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.le_fecha_registro.setDate(QDate().currentDate())
        self.init_provincias()

        self.list_window = ListWindow()
        self.personas = self.read_file()

        if len(self.personas):
            self.list_window.show()
            for persona in self.personas:
                self.list_window.agregar_row(persona)

        self.settings = QSettings('Demolandico', 'CovidHelper')
        geometry = self.settings.value('geometryMain', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)

    def init_provincias(self):
        url = "https://apis.datos.gob.ar/georef/api/provincias?orden=nombre&campos=nombre"
        provinces = requests.get(url).json()["provincias"]
        for i, province in enumerate(provinces):
            province_name = province["nombre"]
            self.ui.cb_provincia.addItem(province_name)
            self.ui.cb_provincia.setItemText(i, province_name)

    @Slot()
    def clear_all(self):
        self.ui.le_dni.setText("")
        self.ui.le_apellido.setText("")
        self.ui.le_edad.setText("")
        self.ui.le_nombre.setText("")
        self.ui.cb_provincia.setCurrentIndex(0)
        self.ui.cb_sexo.setCurrentIndex(0)
        self.ui.le_fecha_registro.setDate(QDate().currentDate())

    @Slot()
    def register(self):
        persona = Persona(
            self.ui.le_dni.text(),
            self.ui.le_nombre.text(),
            self.ui.le_apellido.text(),
            self.ui.le_edad.text(),
            self.ui.cb_sexo.currentText(),
            self.ui.cb_provincia.currentText(),
            self.ui.le_fecha_registro.date()
        )
        print(persona)
        if not persona.is_empty():
            self.personas.append(persona)
            self.save_file()
            self.clear_all()
            if self.list_window.isHidden():
                self.list_window.show()
            self.list_window.agregar_row(persona)
        else:
            QMessageBox().warning(self, "Datos Faltantes", "Cuidado!!! Faltan datos")

    def save_file(self):
        with open("personas.vector", "wb") as pickle_file:
            pickle.dump(self.personas, pickle_file)

    def read_file(self):
        try:
            with open("personas.vector", "rb") as pickle_file:
                personas = pickle.load(pickle_file)
        except FileNotFoundError:
            personas = []
        return personas

    def closeEvent(self, event):
        geometry = self.saveGeometry()
        self.settings.setValue('geometryMain', geometry)
        self.list_window.close()
        super(MainWindow, self).closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    principal = MainWindow()
    principal.show()

    sys.exit(app.exec_())
