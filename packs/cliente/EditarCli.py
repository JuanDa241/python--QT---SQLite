from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.cliente import Clientes,actualizarCliente

class EditarCli(QMainWindow):
    def __init__(self, datos=None):
        super().__init__()
        loadUi('interface/EditarCli.ui', self)
        self.dato = datos
        self.infoEditar()
        self.btnConfirmarEC.clicked.connect(self.actualizarCliente)
        self.pushButton_2.clicked.connect(self.regresar)

    def infoEditar(self):
            if self.dato is not None:
                self.cedula = self.txtCedulaEC.setText(self.dato[0])
                self.txtNombreEC.setText(self.dato[1])
    
    def actualizarCliente(self):
        cedula = self.txtCedulaEC.text()
        nombre = self.txtNombreEC.text()

        actualizar = Clientes(nombre)
        actualizarCliente(actualizar, cedula)
        self.limpiar()
            
    def regresar(self):
        from packs.cliente.clientes import Clientes
        self.close()
        self.main = Clientes()
        self.main.show()

    def limpiar(self):
        self.txtCedulaEC.clear()
        self.txtNombreEC.clear()
