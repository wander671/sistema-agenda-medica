import sqlite3
import os

def conectar():
    """
    Cria uma conexão com o banco de dados SQLite.
    """
    try:
        Base_dir = os.path.dirname(os.path.abspath(__file__))
        caminho_banco = os.path.join(Base_dir, "agenda.db")
        conexao = sqlite3.connect(caminho_banco)
        conexao.row_factory = sqlite3.Row
        return conexao
    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

def inicializar_banco():
    """
    Cria as tabelas e insere dados iniciais de teste se o banco estiver vazio.
    """
    conexao = conectar()
    if conexao is None:
        return

    cursor = conexao.cursor()

    # 1. Cria a tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
    """)

    # 2. Cria a tabela de médicos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especialidade TEXT NOT NULL
    )
    """)

    # 3. Cria a tabela de pacientes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    """)

    # 4. Cria a tabela de consultas (ligando pacientes e médicos)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        medico_id INTEGER,
        data TEXT,
        hora TEXT,
        FOREIGN KEY (paciente_id) REFERENCES pacientes (id),
        FOREIGN KEY (medico_id) REFERENCES medicos (id)
    )
    """)

    # 5. Insere o usuário admin (INSERT OR IGNORE evita erro se ele já existir)
    cursor.execute("""
    INSERT OR IGNORE INTO usuarios (usuario, senha)
    VALUES (?, ?)
    """, ("admin", "123"))

    # 6. Insere médicos de teste apenas se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM medicos")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO medicos (nome, especialidade) VALUES ('Dra. Ana', 'Pediatra')")
        cursor.execute("INSERT INTO medicos (nome, especialidade) VALUES ('Dr. Carlos', 'Cardiologista')")

    # 7. Insere pacientes de teste apenas se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM pacientes")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO pacientes (nome, idade) VALUES ('João Silva', 30)")
        cursor.execute("INSERT INTO pacientes (nome, idade) VALUES ('Maria Souza', 25)")

    # Salva as alterações e fecha a conexão
    conexao.commit()
    conexao.close()
    print("Banco de dados verificado e inicializado com sucesso!")