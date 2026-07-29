# Importa a biblioteca sqlite3, que permite trabalhar com bancos SQLite
import sqlite3

# Importa a biblioteca os para trabalhar com caminhos de arquivos
import os

def conectar():
    """
    Cria uma conexão com o banco de dados SQLite
    Se o banco não existir, ele seá criado automaticamente.

    """

    # Obtém o caminho da pasta onde este arquivo (banco.py) está localizado
    Base_dir = os.path.dirname(os.path.abspath(__file__))

    # Monta o caminho completo do arquivo agenda.db
    caminho_banco = os.path.join(Base_dir, "agenda.db")

    # Cria a conexão com o banco 
    conexao = sqlite3.connect(caminho_banco)

    # Faz com que os resultados das consultas possam ser acessados pelo nome da coluna
    # Exemplo:
    # usuario["nome"]
    # ao invés de 
    # usuario[1]
    conexao.row_factory = sqlite3.Row

    # retorna a conexão para quem chamou a função
    return conexao