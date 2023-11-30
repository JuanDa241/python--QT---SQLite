from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.proveedor import Proveedores, crearProveedor

class AgregarProveedor(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/AgregarPro.ui', self)
        self.btnConfirmarAPro.clicked.connect(self.guardarProveedor)
        self.btnRegresarAPro.clicked.connect(self.regresar)

    def guardarProveedor(self):
        nombre = self.txtNombreAP.text()
        telefono = self.txtContactoAP.text()
        direccion = self.txtDireccionAP.text()
        precio = self.txtPrecioAP.text()

        proveedor = Proveedores(nombre, telefono,direccion,precio)
        crearProveedor(proveedor)
        self.limpiar()

    def regresar(self):
        from packs.proveedores.proveedores import Proveedores
        self.close()
        self.main = Proveedores()
        self.main.show()

    def limpiar(self):
        self.txtNombreAP.clear()
        self.txtContactoAP.clear()
        self.txtDireccionAP.clear()
        self.txtPrecioAP.clear()

        