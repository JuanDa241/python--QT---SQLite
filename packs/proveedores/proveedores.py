from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.proveedor import mostrarProveedores, eliminarProveedor
from packs.proveedores.agregarProve import AgregarProveedor
from packs.proveedores.editarProveedor import EditarProveedor

class Proveedores(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/Proveedores.ui', self)
        self.mostrarTabla()
        self.btnRegresarP.clicked.connect(self.regresar)
        self.btnEditarP.clicked.connect(self.abrir_Editar)
        self.btnEliminarP.clicked.connect(self.eliminarProveedor)
        self.btnAgregarP.clicked.connect(self.abrir_Agregar)

    def mostrarTabla(self):
        self.infoProvedores = mostrarProveedores()
        self.tblProveedores.setRowCount(0)

        for fila in self.infoProvedores:
            fila_prove = self.tblProveedores.rowCount()
            self.tblProveedores.insertRow(fila_prove)

            for columna, valor in enumerate(fila):
                item = QTableWidgetItem(str(valor))
                self.tblProveedores.setItem(fila_prove, columna, item)
    
    def eliminarProveedor(self):
        selected_row = self.tblProveedores.currentRow()
        selected_column = self.tblProveedores.currentColumn()

        if selected_row != -1 and selected_column != -1:
            item = self.tblProveedores.item(selected_row, selected_column)
            valor = item.text()
            eliminarProveedor(valor)
            self.mostrarTabla()  

    def infoEditar(self):
        filaSeleccionada = self.tblProveedores.currentRow()
        if filaSeleccionada != -1:
            datos = []
            for columna in range(self.tblProveedores.columnCount()):
                item = self.tblProveedores.item(filaSeleccionada, columna)
                datos.append(item.text())
        return datos
        
    def abrir_Agregar(self):
        self.ventana2 = AgregarProveedor()
        self.close()
        self.ventana2.show()

    def abrir_Editar(self):
        self.ventana3 = EditarProveedor(self.infoEditar())
        self.close()
        self.ventana3.show()

    def regresar(self):
        from main import MainWindow
        self.close()
        self.main = MainWindow()
        self.main.show()