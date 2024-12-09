import re
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Função para validar a senha
def validar_senha(senha):
    # Expressão regular para validar a senha
    if len(senha) < 6:
        return False, "A senha deve ter pelo menos 6 caracteres."
    if not re.search(r'[A-Z]', senha):  # Verifica se tem pelo menos uma letra maiúscula
        return False, "A senha deve conter pelo menos uma letra maiúscula."
    if not re.search(r'[0-9]', senha):  # Verifica se tem pelo menos um número
        return False, "A senha deve conter pelo menos um número."
    if not re.search(r'[\W_]', senha):  # Verifica se tem pelo menos um caractere especial
        return False, "A senha deve conter pelo menos um caractere especial."   
    return True, ""

# Página inicial (Login)
@app.route('/')
def login():
    return render_template('login.html')

# Página de Cadastro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        senha = request.form['senha']
        confirmacao_senha = request.form['confirmacao_senha']
        
        # Verifica se as senhas coincidem
        if senha != confirmacao_senha:
            return "<script>alert('Senhas não coincidem!');window.history.back();</script>"
        
        # Valida a senha
        is_valid, message = validar_senha(senha)
        if not is_valid:
            return f"<script>alert('{message}');window.history.back();</script>"
        
        # Aqui você pode adicionar lógica para salvar os dados no banco de dados ou outra lógica.
        return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
