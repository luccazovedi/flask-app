# Flask Web Application Example
# ---------------------------------
# Esse aplicativo demonstra rotas básicas do Flask para:
# - Página inicial
# - Cumprimentar usuários
# - Exibir cabeçalhos de requisição
# - Retornar respostas personalizadas e cookies
# - Tratamento de erros
# - Redirecionar usuários
# ---------------------------------

from flask import Flask, request, make_response, abort, redirect

app = Flask(__name__)

# Rota da página inicial
@app.route('/')
def hello_world():
    return '''
    <html>
    <head>
        <title>Flask Demo - PTBDSWS</title>
        <style>
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(120deg, #e0eafc, #cfdef3);
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 500px;
                margin: 40px auto;
                background: #fff;
                border-radius: 12px;
                box-shadow: 0 4px 24px rgba(0,0,0,0.08);
                padding: 32px 24px;
            }
            h1 {
                color: black;
                margin-bottom: 0.5em;
            }
            h2 {
                color: black;
                margin-top: 0;
                margin-bottom: 1.5em;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                margin-bottom: 16px;
            }
            a {
                display: block;
                text-decoration: none;
                background: #1976d2;
                color: #fff;
                padding: 12px 18px;
                border-radius: 8px;
                font-weight: 500;
                box-shadow: 0 2px 8px rgba(25, 118, 210, 0.08);
                transition: background 0.2s;
            }
            a:hover {
                background: #1565c0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello World!</h1>
            <h2>Disciplina PTBDSWS</h2>
            <ul>
                <li><a href="/user/Zovedi">Cumprimentar usuário</a></li>
                <li><a href="/request">Exibir User-Agent</a></li>
                <li><a href="/response">Resposta personalizada e cookie</a></li>
                <li><a href="/badrequest">Requisição inválida (400)</a></li>
                <li><a href="/error">Erro 404</a></li>
                <li><a href="/redirect">Redirecionar para IFSP</a></li>
            </ul>
        </div>
    </body>
    </html>
    '''

# Rota para cumprimentar o usuário pelo nome
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

# Rota para exibir o cabeçalho User-Agent da requisição
@app.route('/request')
def console():
    console = request.headers.get('User-Agent')
    return console

# Rota para requisições inválidas
@app.route('/badrequest')
def bad_request():
    abort(400)

# Rota para retornar com uma resposta personalizada e um cookie
@app.route('/response')
def cookie():
    cookie = make_response('<i>This document carries a cookie!<i>')
    cookie.set_cookie('answer', '404')
    return cookie

# Rota de redirecionamento
@app.route('/redirect')
def redirect_user():
    return redirect('https://ptb.ifsp.edu.br')

# Rota para retornar erro 404
@app.route('/error')
def error():
    abort(404)
