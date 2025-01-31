"""Configuração da janela"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                               QMessageBox, QProgressDialog)
from PySide6.QtGui import QPixmap
import sys

# importando a ui pronta feita por mim no Qt Designer
from ui.ui_window import Ui_MainWindow

import dbthreads
import utils.decript as decript
from utils.resource_path import get_resource_path


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config()

    def config(self):
        """Configurações básicas da Window como, as conexões entre Signals e Slots"""
        self.window_icon = QPixmap(get_resource_path("images\\ExecScript.ico"))
        self.setWindowTitle("ExecScript")
        self.setWindowIcon(self.window_icon)
        self.pushButtonScript.clicked.connect(self.selecionar_script)
        self.pushButtonKey.clicked.connect(self.selecionar_key)
        self.pushButton_4.clicked.connect(self.run_script)
        self.pushButtonTest.clicked.connect(self.testar_conexao)
        self.conexao_lines = [
            self.lineEditUser,
            self.lineEditPwd,
            self.lineEditHost,
            self.lineEditPort,
            self.lineEditSID,
            self.lineEditSerName
        ]
        self.script_lines = [
            self.lineEditScript,
            self.lineEditKey
        ]
        self.textos = []
        self.arquivos = []
        self.dialog = None

    def verificar_conteudo_conexao(self):
        # Tratando as QLineEdit da área de conexão
        self.textos = [line.text().strip()
                       for line in self.conexao_lines if line.text().strip()]
        if len(self.textos) != 5:
            self.exibir_erro("Enter a valid connection")
            return False
        return True

    def verificar_conteudo_script(self):
        # Tratando as QLineEdit da área de selecionar Script
        self.arquivos = [line.text().strip()
                         for line in self.script_lines if line.text().strip()]
        if len(self.arquivos) != 2:
            self.exibir_erro("Enter a valid script")
            return False
        return True

    def testar_conexao(self):
        """Função para testar a conexão com o banco de dados"""
        if not self.verificar_conteudo_conexao():
            return

        # Pegando informações inseridas pelo usuário
        user, pwd, host, porta, service = self.textos
        dsn = f"{host}:{porta}/{service}"

        # Configurando e iniciando a thread de testar conexão
        self.thread_conexao = dbthreads.ConexaoThread(user, pwd, dsn)
        self.thread_conexao.sucesso.connect(self.exibir_sucesso)
        self.thread_conexao.erro.connect(self.exibir_erro)
        self.thread_conexao.finalizado.connect(self.pushButtonTest.setEnabled)
        self.thread_conexao.finalizado.connect(self.pushButton_4.setEnabled)
        self.thread_conexao.start()

    def exibir_sucesso(self, mensagem):
        """Função para exibir mensagem de sucesso"""
        QMessageBox.information(self, "Success!", mensagem)

    def exibir_erro(self, mensagem):
        """Função para exibir mensagem de erro"""
        QMessageBox.critical(self, "Error!", mensagem)

    def run_script(self) -> None:
        """Função para rodar o Script selecionado no banco selecionado"""
        if not self.verificar_conteudo_conexao() or not self.verificar_conteudo_script():
            return
        script, key = self.arquivos

        # bloco de descriptografar
        try:
            with open(script, 'r') as arquivo:
                conteudo = arquivo.read()

            with open(key, 'r') as arquivo:
                chave = arquivo.read()

            conteudo_bytes = bytes.fromhex(conteudo)
            descriptografado = decript.descriptografar(chave, conteudo_bytes)
            comando = descriptografado.decode('utf-8')
        except Exception as e:
            QMessageBox.critical(self, "Error decrypting file", str(e))
            return

        # bloco de execucao do script
        user, pwd, host, porta, service = self.textos
        dsn = f"{host}:{porta}/{service}"

        # Configuração e inicialização da thread de executar comando
        self.thread_run = dbthreads.ExecutarThread(user, pwd, dsn, comando)
        self.thread_run.finalizado.connect(self.finalizar_script)
        self.thread_run.erro.connect(self.exibir_erro)
        self.thread_run.sucesso.connect(self.exibir_sucesso)
        self.thread_run.progresso.connect(self.update_progress)

        # Configuração da barra de progresso
        self.dialog = QProgressDialog("Executing Script",
                                      "Cancel", 0, 100, self)

        self.dialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.dialog.show()

        self.thread_run.start()

    def update_progress(self, value: int) -> None:
        """Função para atualizar o valor da barra de progresso"""
        if self.dialog:
            self.dialog.setValue(value)

    def finalizar_script(self):
        """Função para ser executada depois da finalização da thread"""
        if self.dialog:
            self.dialog.close()
            self.dialog = None

    def selecionar_script(self):
        """Função para selecionar um script"""
        file = self.selecionar_arquivo("Encrypted File (*.enc)")
        if not file:
            return
        self.lineEditScript.setText(file)

    def selecionar_key(self):
        """Função para selecionar uma chave"""
        file = self.selecionar_arquivo("Encypted File (*.key)")
        if not file:
            return
        self.lineEditKey.setText(file)

    def selecionar_arquivo(self, tipo):
        """Função para selecionar um arquivo"""
        file, _ = QFileDialog.getOpenFileName(
            self,
            caption="Select a file",
            dir='.',
            filter=f"{tipo};;All Files (*)"
        )
        if file:
            return file
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
