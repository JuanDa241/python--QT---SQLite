from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from modules.consultas.inventario import actualizarProdcuto, Productos
from modules.consultas.proveedor import mostrarNombreProveedor

class EditarInventario(QMainWindow):
    def __init__(self, data=None):
        super().__init__()
        loadUi('interface/ACTUALIZAR-EDITAR.ui', self)
        self.btnRegresar.clicked.connect(self.regresar)
        self.data = data
        self.formEditar()
        self.infoComboBox()
        self.btnConfirmarA.clicked.connect(self.actualizar)

    def infoComboBox(self):
        self.infoCliente = mostrarNombreProveedor()
        for id, nombre in self.infoCliente:
            self.seleccion.addItem(nombre, id)
        
        self.seleccion.currentIndexChanged.connect(self.idProveedor)

    def idProveedor(self):
        index = self.seleccion.currentIndex()
        id = self.seleccion.itemData(index)
        return id

    def formEditar(self):
        if self.data is not None:
            self.refe.setText(self.data[0]) 
            self.lineEditNombre.setText(self.data[1]) 
            self.lineEdit_2.setText(self.data[2])  
            self.lineEdit_3.setText(self.data[3]) 
            self.lineEdit_4.setText(self.data[4])

    def actualizar(self):
        self.referencia =  self.refe.text()
        self.nombre = self.lineEditNombre.text()
        self.precio = self.lineEdit_2.text()
        self.categoria = self.lineEdit_3.text()
        self.stock = self.lineEdit_4.text()
        self.proveedor = self.seleccion.currentIndex()
        actualizar = Productos( self.nombre, self.precio, self.categoria, self.stock, self.proveedor)
        actualizarProdcuto(actualizar,self.referencia)
        self.limpiar()
    
    def limpiar(self):
        self.refe.clear()
        self.lineEditNombre.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

    def regresar(self):
        from packs.Inventario.inventario import Inventario
        self.close()
        self.main = Inventario()
        self.main.show()

if __name__ == "__main__":
    app = QApplication([])
    window = EditarInventario()
    window.show()
    app.exec()

        