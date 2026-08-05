from flask import Flask, render_template, request, session, redirect
from banco import conectar

app = Flask(__name__)
# Chave usada para proteger a sessão
app.secret_key = "123456"

@app.route("/")
def inicio():
    return render_template("login.html")


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

@app.route("/dashboard")
def dashboard():

    # Verifica se existe um usuário logado
    if "usuario" not in session:
        return redirect("/login")

    return render_template("dashboard.html", usuario=session["usuario"])


@app.route("/logout")
def logout():

    # Apaga a sessão
    session.clear()

    # Volta para o login
    return redirect("/login")

    

if __name__ == "__main__":
    app.run(debug=True)