from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        
        if senha != confirmacao_senha:
            return "<script>alert('Senhas não coincidem!');window.history.back();</script>"
        
        # Aqui você pode adicionar lógica para salvar os dados no banco de dados ou outra lógica.
        return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
