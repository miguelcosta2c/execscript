"""Thread para testar a conexão com o banco"""

from PySide6.QtCore import QThread, Signal
import oracledb

class ConexaoThread(QThread):
    # Sinalizadores para mandar pra MainWindow o que ocorrer na thread
    finalizado = Signal(bool)
    sucesso = Signal(str)
    erro = Signal(str)

    def __init__(self, user, pwd, dsn):
        # inicializando variáveis
        super().__init__()
        self.user = user
        self.pwd = pwd
        self.dsn = dsn
    
    def run(self) -> None:
        """Função que roda a Thread""" 
        # inicializando variáveis para poder fechar após a finalização da thread
        conexao = None
        cursor = None 
        # Tentando estabelecer uma conexão com o Banco
        try:
            # Sinal Emitido para dizer que a thread foi iniciada
            # E desabilitar os botões da MainWindow
            self.finalizado.emit(False) # button.setEnabled
            conexao = oracledb.connect( # Conexão com o banco de dados Oracle
                user=self.user,
                password=self.pwd,
                dsn=self.dsn
            )
            cursor = conexao.cursor() # Cria um cursor
            # Verificando se a conexão foi bem sucedida
            cursor.execute("SELECT 'Conexão bem-sucedida' FROM dual")
            resultado = cursor.fetchone() # Pegando o resultado

            self.sucesso.emit(resultado[0]) # Emitindo Resultado para MainWindow

        # Tratando Erros
        except oracledb.Error as e:
            # Se acontecer um erro ele emite um sinal de erro
            self.erro.emit(str(e))
        finally:
            # Se houver erro ou não ele finaliza e fecha a conexão se elas
            # existirem
            if cursor: cursor.close()
            if conexao: conexao.close()
            self.finalizado.emit(True)
