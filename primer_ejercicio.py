import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


app = QApplication(sys.argv)

# Abrir el archivo .ui
archivo = QFile("primer_ejercicio.ui")
archivo.open(QFile.ReadOnly)

loader = QUiLoader()
ventana = loader.load(archivo)

archivo.close()


# Buscar el botón
boton = ventana.findChild(type(ventana.pushButton), "pushButton")


def enviar():
    nombre = ventana.lineEdit.text()
    edad = ventana.spinBox.value()
    pais = ventana.comboBox.currentText()
    fecha = ventana.dateEdit.date().toString("dd/MM/yyyy")
    ocupacion = ventana.lineEdit_5.text()

    mensaje = (
        f"Mensaje de alerta"
    )

    QMessageBox.information(
        ventana,
        "Registro",
        mensaje
    )


# Conectar botón con función
ventana.pushButton.clicked.connect(enviar)


ventana.show()

sys.exit(app.exec())