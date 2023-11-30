from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.inventario import mostrarInventario,eliminarProducto
from packs.Inventario.editarInventario import EditarInventario
from packs.Inventario.AgregarInven import AgregarInventario

class Inventario(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/Inventario.ui', self)
        self.btnRegresarI.clicked.connect(self.regresar)
        self.btnEditarI.clicked.connect(self.abrir_editar)
        self.mostrarTabla()
        self.btnBorrarI.clicked.connect(self.eliminarInventario)
        self.btnAgregarI.clicked.connect(self.abrir_Agregar)

    def mostrarTabla(self):
        self.infoInventario = mostrarInventario()
        self.tblInventario.setRowCount(0)

        for fila in self.infoInventario:
            fila_inve = self.tblInventario.rowCount()
            self.tblInventario.insertRow(fila_inve)

            for columna, valor in enumerate(fila):
                item = QTableWidgetItem(str(valor))
                self.tblInventario.setItem(fila_inve, columna, item)

    def eliminarInventario(self):
        selected_row = self.tblInventario.currentRow()
        selected_column = self.tblInventario.currentColumn()

        if selected_row != -1 and selected_column != -1:
            item = self.tblInventario.item(selected_row, selected_column)
            valor = item.text()
            eliminarProducto(valor)
            self.mostrarTabla()  
    
    def regresar(self):
        from main import MainWindow
        self.close()
        self.main = MainWindow()
        self.main.show()

    def abrir_editar(self):
        selected_row = self.tblInventario.currentRow()
        if selected_row != -1:
            data = []
            for columna in range(self.tblInventario.columnCount()):
                item = self.tblInventario.item(selected_row, columna)
                data.append(item.text())

            self.ventana4 = EditarInventario(data)
            self.close()
            self.ventana4.show()

    def abrir_Agregar(self):
        self.ventana5 = AgregarInventario()
        self.close()
        self.ventana5.show()

    
