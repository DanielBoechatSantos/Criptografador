from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os
import sys

class CriptografiaApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criptografia de Arquivos")
        self.setGeometry(300, 200, 400, 200)
        self.setStyleSheet("background-color: #6E75FF;")  # Fundo azul suave
        self.btn_criptografar = QtWidgets.QPushButton("Criptografar", self)
        self.btn_criptografar.setGeometry(100, 60, 200, 50)
        self.btn_criptografar.setStyleSheet(self.button_style())
        self.btn_criptografar.clicked.connect(self.criptografar)

        self.btn_descriptografar = QtWidgets.QPushButton("Descriptografar", self)
        self.btn_descriptografar.setGeometry(100, 130, 200, 50)
        self.btn_descriptografar.setStyleSheet(self.button_style())
        self.btn_descriptografar.clicked.connect(self.descriptografar)

    def button_style(self):
        return """
        QPushButton {
            background-color: #393D85;  /* Azul suave */
            color: white;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: #034A0A;  /* Hover verde suave */
        }
        """

    def generate_key(self, password):
        salt = b'salt_cryptography' 
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def criptografar(self):
        password, ok = QInputDialog.getText(self, "Senha", "Digite a senha para criptografar:", QtWidgets.QLineEdit.Password)
        if ok and password:
            key = self.generate_key(password)
            file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo para criptografar")
            if file_path:
                with open(file_path, "rb") as file:
                    file_data = file.read()
                encrypted_data = Fernet(key).encrypt(file_data)
                with open(file_path, "wb") as file:
                    file.write(encrypted_data)
                QMessageBox.information(self, "Sucesso", "Arquivo criptografado com sucesso!")

    def descriptografar(self):
        password, ok = QInputDialog.getText(self, "Senha", "Digite a senha para descriptografar:", QtWidgets.QLineEdit.Password)
        if ok and password:
            key = self.generate_key(password)
            file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo para descriptografar")
            if file_path:
                try:
                    with open(file_path, "rb") as file:
                        encrypted_data = file.read()
                    decrypted_data = Fernet(key).decrypt(encrypted_data)
                    with open(file_path, "wb") as file:
                        file.write(decrypted_data)
                    QMessageBox.information(self, "Sucesso", "Arquivo descriptografado com sucesso!")
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Falha ao descriptografar o arquivo: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    janela = CriptografiaApp()
    janela.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
