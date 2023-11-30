from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt6.uic import loadUi
from packs.Inventario.inventario import Inventario
from packs.proveedores.proveedores import Proveedores
from packs.despacho.despacho import Despacho
from packs.cliente.clientes import Clientes
from packs.reserva.reservas import Reservas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interface/principal.ui', self)
        self.btnInventarioP.clicked.connect(self.abrir_inventario)
        self.btnProveedoresP.clicked.connect(self.abrir_proveedores)
        self.btnDespachoP.clicked.connect(self.abrir_despacho)
        self.btnClienteP.clicked.connect(self.abrir_cliente)
        self.btnReservasP.clicked.connect(self.abrir_reserva)

    def abrir_inventario(self):
        self.ventana2 = Inventario()
        self.close()
        self.ventana2.show()

    def abrir_proveedores(self):
        self.ventana3 = Proveedores()
        self.close()
        self.ventana3.show()

    def abrir_despacho(self):
        self.ventana4 = Despacho()
        self.close()
        self.ventana4.show()

    def abrir_cliente(self):
        self.ventana5 = Clientes()
        self.close()
        self.ventana5.show()

    def abrir_reserva(self):
        self.ventana6 = Reservas()
        self.close()
        self.ventana6.show()
        
if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()