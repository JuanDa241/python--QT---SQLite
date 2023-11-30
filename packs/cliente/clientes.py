from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.cliente import mostrarClientes, eliminarClieten
from packs.cliente.Agregar import AgregarClientes
from packs.cliente.EditarCli import EditarCli ,actualizarCliente

class Clientes(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/Clientes.ui', self)
        self.mostrarTabla()
        self.btnRegresarC.clicked.connect(self.regresar)
        self.btnEditarC.clicked.connect(self.abrir_Editar)
        self.btnEliminarC.clicked.connect(self.eliminarCliente)
        self.btnAgregarC.clicked.connect(self.abrir_Agregar)

    def mostrarTabla(self):
        self.infoCliente = mostrarClientes()
        self.tblCliente.setRowCount(0)

        for fila in self.infoCliente:
            fila_inve = self.tblCliente.rowCount()
            self.tblCliente.insertRow(fila_inve)

            for columna, valor in enumerate(fila):
                item = QTableWidgetItem(str(valor))
                self.tblCliente.setItem(fila_inve, columna, item)

    def eliminarCliente(self):
        selected_row = self.tblCliente.currentRow()
        selected_column = self.tblCliente.currentColumn()

        if selected_row != -1 and selected_column != -1:
            item = self.tblCliente.item(selected_row, selected_column)
            valor = item.text()
            eliminarClieten(valor)
            self.mostrarTabla()  
    
    def regresar(self):
        from main import MainWindow
        self.close()
        self.main = MainWindow()
        self.main.show()

    def infoEditar(self):
        filaSeleccionada = self.tblCliente.currentRow()
        if filaSeleccionada != -1:
            datos = []
            for columna in range(self.tblCliente.columnCount()):
                item = self.tblCliente.item(filaSeleccionada, columna)
                datos.append(item.text())
        return datos
    
    def abrir_Editar(self):
            self.ventana9 = EditarCli(self.infoEditar())
            self.close()
            self.ventana9.show()

    def abrir_Agregar(self):
        self.ventana5 = AgregarClientes()
        self.close()
        self.ventana5.show()