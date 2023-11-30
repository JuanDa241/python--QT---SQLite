from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.despacho import mostrarDespachos
from packs.despacho.agregarDespacho import AgregarDespacho

class Despacho(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/Despacho.ui', self)
        self.btnRegresarD.clicked.connect(self.regresar)
        self.btnAgregarD.clicked.connect(self.abrir_agregarDespacho)
        self.mostrarTabla()

    def mostrarTabla(self):
       self.infoDespacho = mostrarDespachos()
       
       self.tableWidget.setRowCount(0)

       for fila in self.infoDespacho:
            fila_desp = self.tableWidget.rowCount()
            self.tableWidget.insertRow(fila_desp)

            for columna, valor in enumerate(fila):
                item = QTableWidgetItem(str(valor))
                self.tableWidget.setItem(fila_desp, columna, item)

    def abrir_agregarDespacho(self):
        self.ventana5 = AgregarDespacho()
        self.close()
        self.ventana5.show()

    def regresar(self):
        from main import MainWindow
        self.close()
        self.main = MainWindow()
        self.main.show()