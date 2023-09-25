from flask import Flask, render_template

main = Flask(__name__)

# Página de login
@main.route('/')
@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

if __name__ == '__main__':
    main.run(port=8080)