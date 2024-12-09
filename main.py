from flask import Flask, render_template

app_gabriel = Flask(__name__, template_folder='templates')

@app_gabriel.route('/')
def raiz():
    return 'Olá, turma!'

@app_gabriel.route('/ola')
def ola():
    return 'Olá, turma!'

def saudacoes(nome):
    return f'Olá, {nome}!'

@app_gabriel.route('/<id>')
def saudacao(id):
    return render_template('homepage_nome.html', nome=id)

@app_gabriel.route("/index")
def indice():
    return render_template("index.html")

@app_gabriel.route("/usuario")
def dados_usuario():
    nome_usuario = "Gabriel"
    dados_usu = {"profissao": "Desenvolvedor web", "disciplina": "Desenvolvimento Web III"}
    return render_template("usuario.html", nome=nome_usuario, dados=dados_usu)

@app_gabriel.route("/usuario/<nome_usuario>/<nome_profissao>/<nome_disciplina>")
def usuario(nome_usuario, nome_profissao, nome_disciplina):  
    dados_usu = {"profissao": nome_profissao, "disciplina": nome_disciplina}
    return render_template("usuario.html", nome=nome_usuario, dados=dados_usu)

@app_gabriel.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app_gabriel.run(port=8000)
