from flask import Flask, render_template, request, redirect, flash

main = Flask(__name__)
main.config['SECRET_KEY'] = "password"

# Página home
@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

# Página de login
@main.route('/login')
def login():
    return render_template('login.html')

# Página de cadastro
@main.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':    # Caso tenha enviado o dados do cadastro
        return redirect('/login')
    else:   # Caso queira somente acessar a página
        return render_template('cadastro.html')

# Função autenticar
@main.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form.get('email')
    senha = request.form.get('senha_login')
    if email == 'admin@ifro.edu' and senha == 'Admin@1234': # Usuário teste
        return 'Você está logado.'
    else:
        flash("Dados inválidos.")
        return redirect ('/login')
    
if __name__ == '__main__':
    main.run(port=8080)