from banco import conectar

# Conectar ao banco
conexao = conectar()
cursor = conexao.cursor()

# ------------------------
# Inserindo pacientes
# ------------------------

cursor.execute("""
INSERT INTO pacientes (nome, idade)
VALUES ('João Silva', 30)
""")

cursor.execute("""
INSERT INTO pacientes (nome, idade)
VALUES ('Maria Souza', 25)
""")

# --------------------------
# Inserindo médicos
# ---------------------------

cursor.execute("""
INSERT INTO medicos (nome, especialidade)
VALUES ('Dra. Ana', 'Pediatra')
""")

cursor.execute("""
INSERT INTO medicos (nome, especialidade)
VALUES ('Dr. Carlos', 'Cardiologista')
""")

# --------------------------------
# TABELA DE USUÀRIOS
# --------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

# ------------------------------------
# INSERINDO USUÀRIO
# ------------------------------------

cursor.execute("""
INSERT INTO usuarios (usuario, senha)
VALUES (?, ?)
""",("admin", "123"))

# Salva as alterações
conexao.commit()

# Fecha a conexão
conexao.close()

print("Dados de teste inseridos com sucesso!!!")