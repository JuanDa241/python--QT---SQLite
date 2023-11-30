from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.proveedor import Proveedores, actualizarProveedor

class EditarProveedor(QMainWindow):
    def __init__(self, datos=None):
        super().__init__()
        loadUi('interface/EditarPro.ui', self)
        self.dato = datos
        self.infoEditar()
        self.btnConfirmarEPro.clicked.connect(self.actualizarProveedor)
        self.btnRegresarEPro.clicked.connect(self.regresar)

    def infoEditar(self):
        if self.dato is not None:
            self.idProveedor = self.dato[0]
            self.txtNombreEP.setText(self.dato[1])
            self.txtContactoEP.setText(self.dato[2])
            self.txtDireccionEP.setText(self.dato[3])
            self.txtPrecioEP.setText(self.dato[4])
    
    def actualizarProveedor(self):
        idPro = self.idProveedor
        nombre = self.txtNombreEP.text()
        telefono = self.txtContactoEP.text()
        direccion = self.txtDireccionEP.text()
        precio = self.txtPrecioEP.text()
        actualizar = Proveedores(nombre, telefono,direccion,precio)
        actualizarProveedor(actualizar, idPro)
        self.limpiar()
            
    def limpiar(self):
        self.txtNombreEP.clear()
        self.txtContactoEP.clear()
        self.txtDireccionEP.clear()
        self.txtPrecioEP.clear()
        
    def regresar(self):
        from main import MainWindow
        self.close()
        self.main = MainWindow()
        self.main.show()