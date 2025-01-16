import sys
from pathlib import Path

def get_resource_path(relative_path):
    """Retorna o caminho correto para o arquivo,
    dependendo se o app está rodando de um arquivo .exe ou não"""
    try:
        # Se o código estiver sendo executado a partir de um arquivo.exe pelo
        # PyInstaller
        if getattr(sys, 'frozen', False):
            # Quando é um arquivo.exe, os arquivos são guardados pelo MEIPASS
            base_path = Path(sys._MEIPASS)
        else:
            # Se for executado pelo arquivo.py
            base_path = Path(__file__).resolve().parent.parent
        print(base_path)
        return base_path / relative_path
    except Exception as e:
        print("Erro ao acessar o path", e)
        return None

