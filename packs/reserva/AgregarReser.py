import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.reserva import  crearReserva, Reservas


class AgregarReserva(QMainWindow):
    def __init__(self, datos=None ):
        super().__init__()
        loadUi('interface/AgregarRes.ui', self)
        self.dato = datos
        self.infoInicial()
        self.btnConfirmarAR.clicked.connect(self.agregarReserva)
        self.btnRegresarAR.clicked.connect(self.regresar)

    def infoInicial(self):
        if self.dato is not None:
            self.txtCantidadAR.setText(str(self.dato[0]))
            self.txtReferenciaAR.setText(str(self.dato[1]))
        
    def agregarReserva(self):
        cantidad= self.txtCantidadAR.text()
        estado= self.comboBox.currentText()
        referencia= self.txtReferenciaAR.text()
        reserva = Reservas(cantidad, estado, referencia)
        crearReserva(reserva)
        self.limpiar()

    def regresar(self):
        from packs.reserva.reservas import Reservas
        self.close()
        self.main =Reservas()
        self.main.show()

    def limpiar(self):
        self.txtCantidadAR.clear()
        self.txtReferenciaAR.clear()

    def insertarDato(self):
        self.txtCantidadAR.setText(self.info[0])
