from flask import Flask, render_template, request, session, redirect, jsonify
from banco import conectar
import requests

app = Flask(__name__)
# Chave usada para proteger a sessão
app.secret_key = "123456"

# Define a rota principal (raiz) do sistema
@app.route("/")
def inicio():
    return render_template("login.html")



# Rota que aceita exibições de página (GET) e envios de formulário (POST)
@app.route("/login", methods=["GET", "POST"])
def login():

    # Se o usuario clicou no botão Entrar
    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT* FROM usuarios WHERE usuario = ? AND senha = ?",
            (usuario, senha)
        )

        usuario_encontrado = cursor.fetchone()

        conexao.close()

        if usuario_encontrado:
            # Guarda o nome do usuário na sessão
            session["usuario"] = usuario

            # Vai para a dashboard
            return redirect("/dashboard")

        return "Usuário ou senha inválidos!"

    return render_template("login.html")



# Define a rota da API para consultar as consultas médicas
@app.route("/api/consultas")
def api_consultas():
    # Recebe o termo de busca pela URL
    busca = request.args.get("busca", "").strip()

    # Abre a conexão com banco de dados
    conexao = conectar()

    # Cria o cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Se existe um termo de busca
    if busca:
        print("Busca recebida:", busca)
        # Adiciona % para permitir encontrar o termo em qualquer parte do nome
        termo = f"%{busca}%"

        # Busca pelo nome do paciente OU pelo nome do Médico
        cursor.execute("""
            SELECT
                consultas.id,
                pacientes.nome AS paciente,
                medicos.nome AS medico,
                consultas.data,
                consultas.hora
            FROM consultas
            JOIN pacientes ON consultas.paciente_id = pacientes.id
            JOIN medicos ON consultas.medico_id = medicos.id
            WHERE pacientes.nome LIKE ?
                OR medicos.nome LIKE ?
        """, (termo, termo))

    # Se não existe termo de busca
    else:
        print("Busca vazia: exibindo todas as consultas")
        cursor.execute("""
            SELECT
                consultas.id,
                pacientes.nome AS paciente,
                medicos.nome AS medico,
                consultas.data,
                consultas.hora
            FROM consultas
            JOIN pacientes ON consultas.paciente_id = pacientes.id
            JOIN medicos ON consultas.medico_id = medicos.id
        """)


    # Pega todos os resultados encontrados
    consultas = cursor.fetchall()

    # Fecha a conexão com o banco 
    conexao.close()

    # Cria uma lista para armazenar os resultados
    resultado = []

    # Percorre cada consulta encontrada
    for consulta in consultas:
        resultado.append({
            "id": consulta[0],
            "paciente": consulta[1],
            "medico": consulta[2],
            "data": consulta[3],
            "hora": consulta[4]
        })

    # Retorna os dados da API em formato JSON
    return jsonify(resultado)


# Define a rota HTTP DELETE para excluir uma consulta específica pelo ID via URL
@app.route("/api/consultas/<int:id>", methods=["DELETE"])
def excluir_consulta(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM consultas WHERE id = ?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount == 0:
        conexao.close()
        return jsonify({"erro": "Consulta não encontrada"}), 404

    conexao.close()

    return jsonify({
        "mensagem": "Consulta excluída com sucesso!",
        "id": id
    }), 200



# Define a rota para acessar a página do dashboard
@app.route("/dashboard")
def dashboard():

    # Verifica se existe um usuário logado
    if "usuario" not in session:
        return redirect("/login")

    return render_template("dashboard.html", usuario=session["usuario"])



# Define a rota para o encerramento da sessão do usuário
@app.route("/logout")
def logout():

    # Apaga a sessão
    session.clear()

    # Volta para o login
    return redirect("/login")


# Define a rota '/usuarios-api' e associa à função abaixo
@app.route("/usuarios-api")
def usuarios_api():
    url = "https://jsonplaceholder.typicode.com/users"

    resposta = requests.get(url)

    dados = resposta.json()

    return jsonify(dados)


# A rota aceita um parâmetro dinâmico 'id' do tipo inteiro via URL
@app.route("/usuario-api/<int:id>")
def usuario_api(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}"

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 404:
            return jsonify({"erro": "Usuário não encontrado"}), 404

        dados = resposta.json()

        return jsonify(dados)

    except requests.RequestException:
        return jsonify({"erro": "Erro ao acessar a API externa"}), 500

if __name__ == "__main__":
    app.run(debug=True)