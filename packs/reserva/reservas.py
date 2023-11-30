from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.reserva import mostrarReservas
from packs.reserva.AgregarReser import AgregarReserva

class Reservas(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/Reservas.ui', self)
        self.mostrarTabla()
        self.btnAgregarR.clicked.connect(self.abrir_Agregar)
        self.btnRegresarR.clicked.connect(self.regresar)


    def mostrarTabla(self):
        self.infoReserva = mostrarReservas()
        self.tblReservasR.setRowCount(0)

        for fila in self.infoReserva:
            fila_res = self.tblReservasR.rowCount()
            self.tblReservasR.insertRow(fila_res)

            for columna, valor in enumerate(fila):
                item =QTableWidgetItem(str(valor))
                self.tblReservasR.setItem(fila_res,columna,item)

    def abrir_Agregar(self, dato):
        self.ventana2= AgregarReserva(dato)
        self.close()
        self.ventana2.show()

    def regresar(self):
        from main import MainWindow
        self.close()
        self.main = MainWindow()
        self.main.show()