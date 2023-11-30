from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.cliente import mostrarClientes
from modules.consultas.inventario import mostrarIdNombre, editarStock, mostrarStock
from modules.consultas.despacho import Despachos, crearDespachos
from packs.reserva.reservas import Reservas


class AgregarDespacho(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/AgregarDes.ui', self)
        self.infoComboBox()
        self.btnConfirmarAD.clicked.connect(self.agregarDespacho)
        self.btnRegresarAD.clicked.connect(self.regresar)

    def regresar(self):
     from packs.despacho.despacho import Despacho
     self.close()
     self.main = Despacho()
     self.main.show()

    def infoComboBox(self):
        self.infoCliente = mostrarClientes()
        for id, nombre in self.infoCliente:
            self.comboBoxAC.addItem(nombre, id)
        self.comboBoxAC.currentIndexChanged.connect(self.ccCliente)

        self.infoProducto = mostrarIdNombre()
        for referencia, producto in self.infoProducto:
            self.comboBoxPD.addItem(producto, referencia)
        self.comboBoxPD.currentIndexChanged.connect(self.idProducto)

    def ccCliente(self):
        index = self.comboBoxAC.currentIndex()
        id= self.comboBoxAC.itemData(index)
        return id
        
    def idProducto(self):
        index = self.comboBoxPD.currentIndex()
        id= self.comboBoxPD.itemData(index)
        return id
        
    def agregarDespacho(self):
        self.cedula = int(self.ccCliente())
        self.referencia = int(self.idProducto())
        self.cantidad = int(self.txtCnatidadAD.text())
        self.fecha = self.txtFechaAD.text()
        agregarDatos = Despachos(self.cantidad, self.fecha, self.referencia, self.cedula)

        stock = mostrarStock(self.referencia)
        
        if stock > 0:

         crearDespachos(agregarDatos)
         editarStock(self.cantidad, self.referencia)
        else:
           datos = [self.referencia, self.cantidad]
           print(datos)
           Reservas.abrir_Agregar(self, datos)


   
    
       
            


        

        