from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
from modules.consultas.cliente import Clientes, crearCliente

class AgregarClientes(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/AgregarCli.ui', self)
        self.btnRegresarAC.clicked.connect(self.regresar)
        self.btnConfirmarAC.clicked.connect(self.guardarCliente)
    
    def guardarCliente(self):
        nombre = self.txtNombreAC.text()

        cliente = Clientes(nombre)
        crearCliente(cliente)
        self.limpiar()

    def limpiar(self):
        self.txtNombreAC.clear()

    def regresar(self):
        from packs.cliente.clientes import Clientes
        self.close()
        self.main = Clientes()
        self.main.show()


        