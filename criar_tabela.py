# Importa a função conectar() do arquivo banco.py
from banco import conectar

# Criar a conexão com o banco de dados
conexao = conectar()

# Criar o cursor, que será responsável por executar os comandos SQL
cursor = conexao.cursor()

# ----------------------------
# TABELA DE PACIENTES
# ----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    telefone TEXT
)
""")

# -------------------------------
# TABELA DE MÈDICOS
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS medicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especialidade TEXT
)
""")

# ----------------------------------
# TABELA DE CONSULTAS
# ----------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    medico_id INTEGER,
    data TEXT,
    hora TEXT,

    -- Liga a consulta ao paciente
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),

    -- Liga a consulta ao médico
    FOREIGN KEY (medico_id) REFERENCES medicos(id)

)
""")

# ---------------------------------------
# TABELA DE USUÀRIOS
# ---------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

# Salva todas as alterações
conexao.commit()

# Fecha a conexão
conexao.close()


print("Tabelas criadas com sucesso!!")