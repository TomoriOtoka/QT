
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Login(QMainWindow):

    def __init__(self):
        super().__init__()

        # Cargar la interfaz del login
        uic.loadUi("2.ui", self)

        # Conectar el botón
        self.btnLogin.clicked.connect(self.iniciar_sesion)

        # Referencia a la segunda ventana
        self.ventana2 = None

    def iniciar_sesion(self):

        # Obtener los datos de los QLineEdit
        usuario = self.inputUsuario.text().strip()
        contrasena = self.inputContrasena.text().strip()

        # 1. Comprobar campos vacíos
        if usuario == "" or contrasena == "":
            QMessageBox.warning(
                self,
                "Advertencia",
                "Por favor, complete todos los campos."
            )
            return

        # 2. Comprobar usuario y contraseña
        if usuario == "admin" and contrasena == "1234":
            self.abrir_ventana2()

        else:
            QMessageBox.critical(
                self,
                "Error",
                "Usuario o contraseña incorrectos."
            )

    def abrir_ventana2(self):

        # Crear la ventana 2
        self.ventana2 = QMainWindow()

        # Cargar 2.ui
        uic.loadUi("1ui.ui", self.ventana2)

        # Mostrar ventana 2
        self.ventana2.show()

        # Cerrar ventana de login
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Login()
    ventana.show()

    sys.exit(app.exec_())
