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

# Função auxiliar para criar o botão de voltar
def back_button():
    return '''
        <div style="margin-top: 20px;">
            <a href="/" style="
                display: inline-block;
                text-decoration: none;
                background: #1976d2;
                color: white;
                padding: 10px 16px;
                border-radius: 8px;
                font-weight: 500;
                box-shadow: 0 2px 8px rgba(25, 118, 210, 0.2);
                transition: background 0.2s;">
                ⬅ Voltar ao Início
            </a>
        </div>
    '''

# Página inicial
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
                text-align: center;
            }
            h1, h2 {
                color: black;
                margin: 0 0 1em;
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
            <h1>Disciplina PTBDSWS</h1>
            <h2>Lucca Zovedi</h2>
            <ul>
                <li><a href="/user/Zovedi">Cumprimentar usuário</a></li>
                <li><a href="/request">Exibir User-Agent</a></li>
                <li><a href="/response">Resposta personalizada e cookie</a></li>
                <li><a href="/badrequest">Requisição inválida (400)</a></li>
                <li><a href="/error">Erro 404</a></li>
                <li><a href="/redirect">Redirecionar para IFSP</a></li>
                <li><a href="/user/identify/Zovedi/PT3039463/IFSP">Identificação</a></li>
                <li><a href="/inforequest">IP Request</a></li>
            </ul>
        </div>
    </body>
    </html>
    '''

# Cumprimentar usuário
@app.route('/user/<name>')
def greet_user(name):
    return f'<h1>Hello, {name}!</h1>' + back_button()

# Exibir cabeçalho User-Agent
@app.route('/request')
def console():
    user_agent = request.headers.get('User-Agent')
    return f'<h1>User-Agent:</h1><p>{user_agent}</p>' + back_button()

# Requisições inválidas
@app.route('/badrequest')
def bad_request():
    return '<h1>Erro 400 - Requisição Inválida</h1>' + back_button(), 400

# Resposta personalizada e cookie
@app.route('/response')
def cookie():
    response = make_response('<i>This document carries a cookie!</i>' + back_button())
    response.set_cookie('answer', '404')
    return response

# Redirecionamento
@app.route('/redirect')
def redirect_user():
    return redirect('https://ptb.ifsp.edu.br')

# Erro 404
@app.route('/error')
def error():
    return '<h1>Erro 404 - Página não encontrada</h1>' + back_button(), 404

# Identificação do usuário
@app.route('/user/identify/<name>/<user_id>/<institute>')
def identify_user(name, user_id, institute):
    return f'''
        <h1>Avaliação contínua Aula 030!</h1>
        <h2>Aluno: {name}</h2>
        <h2>Prontuário: {user_id}</h2>
        <h2>Instituição: {institute}</h2>
    ''' + back_button()

# Info do Request
@app.route('/inforequest')
def console1():
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    host = request.host
    return f'''
        <h1>Informações do Usuário</h1>
        <h2>IP: {ip}</h2>
        <h2>Navegador: {user_agent}</h2>
        <h2>Host: {host}</h2>
    ''' + back_button()

# Executar
if __name__ == '__main__':
    app.run(debug=True)

