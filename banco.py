# Importa a biblioteca sqlite3, que permite trabalhar com bancos SQLite
import sqlite3

# Importa a biblioteca os para trabalhar com caminhos de arquivos
import os


def conectar():
    """
    Cria uma conexão com o banco de dados SQLite.
    Se ocorrer algum erro durante a conexão, ele será tratado.
    """

    try:

        # Obtém o caminho da pasta onde este arquivo (banco.py) está localizado
        Base_dir = os.path.dirname(os.path.abspath(__file__))

        # Monta o caminho completo do arquivo agenda.db
        caminho_banco = os.path.join(Base_dir, "agenda.db")

        # Cria a conexão com o banco
        conexao = sqlite3.connect(caminho_banco)

        # Faz com que os resultados possam ser acessados pelo nome da coluna
        conexao.row_factory = sqlite3.Row

        # Retorna a conexão
        return conexao

    except sqlite3.Error as erro:

        # Exibe o erro no terminal
        print(f"Erro ao conectar ao banco de dados: {erro}")

        # Retorna None caso a conexão falhe
        return None