"""Thread para executar um comando no banco"""

from PySide6.QtCore import QThread, Signal
import oracledb

class ExecutarThread(QThread):
    # Sinalizadores para mandar pra MainWindow o que ocorrer na thread
    progresso = Signal(int)
    erro = Signal(str)
    sucesso  = Signal(str)
    finalizado = Signal()

    def __init__(self, user: str, pwd: str, dsn: str, cmd: str):
        # inicializando variáveis
        super().__init__()
        self.user = user
        self.pwd = pwd
        self.dsn = dsn
        self.cmd = cmd
    
    def run(self):
        """Função que roda a Thread""" 
        # inicializando variáveis para poder fechar após a finalização da thread
        conexao = None
        cursor = None
        # Tentando estabelecer uma conexão com o Banco
        try:
            conexao = oracledb.connect(
                user=self.user,
                password=self.pwd,
                dsn=self.dsn
            )
            cursor = conexao.cursor()

            # Separando os comandos em uma lista
            comandos = self.cmd.split(";")
            total = len(comandos) # Total de comandos
            # Executando comando por comando
            for i, cmd in enumerate(comandos):
                cursor.execute(cmd)
                # Calculando progresso em porcentagem para a barra de progresso
                # da MainWindow
                progresso = int((i+1) / total * 100)
                self.progresso.emit(progresso) # Emitindo progresso

            conexao.commit() # Dando commit por precaução
            # Emitindo sinal de sucesso
            self.sucesso.emit("Script Finalizado com sucesso")
        # Tratando Erros
        except oracledb.Error as e:
            # Se acontecer um erro ele emite um sinal de erro
            self.erro.emit(str(e))
        finally:
            # Se houver erro ou não ele finaliza e fecha a conexão se elas
            # existirem
            if cursor: cursor.close()
            if conexao: conexao.close()
            self.finalizado.emit()
