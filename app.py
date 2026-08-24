from flask import Flask, render_template, request, session, redirect, jsonify
from banco import conectar
import requests
import sqlite3

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

    try:

        # Recebe o termo de busca pela URL
        busca = request.args.get("busca", "").strip()

        # Abre a conexão com o banco de dados
        conexao = conectar()

        # Verifica se a conexão foi criada corretamente
        if conexao is None:
            return jsonify({
                "erro": "Não foi possível conectar ao banco de dados."
            }), 500

        # Cria o cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Se existe um termo de busca
        if busca:

            print("Busca recebida:", busca)

            # Adiciona % para permitir encontrar o termo em qualquer parte do nome
            termo = f"%{busca}%"

            # Busca pelo nome do paciente OU pelo nome do médico
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

    except sqlite3.Error as erro:

        # Exibe o erro no terminal
        print(f"Erro no banco de dados: {erro}")

        # Retorna uma mensagem amigável para a API
        return jsonify({
            "erro": "Ocorreu um erro ao consultar o banco de dados."
        }), 500

    finally:

        # Fecha a conexão com o banco, caso ela tenha sido aberta
        if "conexao" in locals() and conexao is not None:
            conexao.close()



# Define a rota HTTP DELETE para excluir uma consulta específica pelo ID via URL
@app.route("/api/consultas/<int:id>", methods=["DELETE"])
def excluir_consulta(id):

    conexao = None

    try:

        # Abre a conexão com o banco de dados
        conexao = conectar()

        # Verifica se a conexão foi criada corretamente
        if conexao is None:
            return jsonify({
                "erro": "Não foi possível conectar ao banco de dados."
            }), 500

        # Cria o cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Exclui a consulta pelo ID
        cursor.execute(
            "DELETE FROM consultas WHERE id = ?",
            (id,)
        )

        # Confirma a alteração no banco
        conexao.commit()

        # Verifica se alguma consulta foi excluída
        if cursor.rowcount == 0:
            return jsonify({
                "erro": "Consulta não encontrada"
            }), 404

        # Retorna mensagem de sucesso
        return jsonify({
            "mensagem": "Consulta excluída com sucesso!",
            "id": id
        }), 200

    except sqlite3.Error as erro:

        # Desfaz a operação caso ocorra algum erro
        if conexao:
            conexao.rollback()

        # Mostra o erro no terminal
        print(f"Erro ao excluir consulta: {erro}")

        # Retorna uma mensagem amigável
        return jsonify({
            "erro": "Ocorreu um erro ao excluir a consulta."
        }), 500

    finally:

        # Fecha a conexão com o banco
        if conexao:
            conexao.close()


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


# Tratamento global para páginas não encontradas
@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template("404.html"), 404

# Tratamento global para erros internos do servidor
@app.errorhandler(500)
def erro_interno_servidor(erro):
    return render_template("500.html"), 500


# Verifica se este arquivo de código está sendo executado diretamente pelo terminal
# (ou seja, se você não está apenas importando ele dentro de outro arquivo)
if __name__ == "__main__":

    # Permite que o Flask aceite conexões vindas de fora do container.
    # mantém nossa aplicação na porta padrão que já colocamos no Dockerfile
    app.run(host="0.0.0.0", port=5000, debug=True)