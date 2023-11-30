from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.inventario import Productos, crearProducto
from modules.consultas.proveedor import mostrarProveedores, mostrarNombreProveedor

class AgregarInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/AgregarInve.ui', self)
        self.infoComboBox()
        self.btnRegresarAInv.clicked.connect(self.regresar)
        self.btnConfirmarAInv.clicked.connect(self.guardarInventario)

    def infoComboBox(self):
        self.infoCliente = mostrarNombreProveedor()
        for id, nombre in self.infoCliente:
            self.comboBox34.addItem(nombre, id)
        
        self.comboBox34.currentIndexChanged.connect(self.idProveedor)

    def idProveedor(self):
        index = self.comboBox34.currentIndex()
        id = self.comboBox34.itemData(index)
        return id

    def guardarInventario(self):
        nombre = self.txtNombreEInv.text()
        precio = self.txtPrecioEInv.text()
        categoria = self.txtCategoriaEInv.text()
        stock = self.txtStockEInv.text()
        proveedor = self.comboBox34.currentIndex()
        info = Productos(nombre, precio, categoria, stock, proveedor)
        crearProducto(info)
        self.limpiar()
    
    def limpiar(self):
        self.txtNombreEInv.clear()
        self.txtPrecioEInv.clear()
        self.txtCategoriaEInv.clear()
        self.txtStockEInv.clear()

    def regresar(self):
        from packs.Inventario.inventario import Inventario
        self.close()
        self.main = Inventario()
        self.main.show()

