# Flask Web Application - PTBDSWS

Este projeto é um exemplo simples de aplicação web usando Flask, criado para a disciplina PTBDSWS.

## Funcionalidades

- **Página inicial**: Apresenta links para todas as rotas do sistema, com layout moderno e responsivo.
- **Cumprimentar usuário** (`/user/<nome>`): Exibe uma saudação personalizada usando o nome informado na URL.
- **Exibir User-Agent** (`/request`): Mostra o cabeçalho User-Agent da requisição HTTP.
- **Resposta personalizada e cookie** (`/response`): Retorna uma resposta HTML e define um cookie chamado `answer` com valor `404`.
- **Requisição inválida** (`/badrequest`): Retorna um erro HTTP 400 (Bad Request).
- **Erro 404** (`/error`): Retorna um erro HTTP 404 (Not Found).
- **Redirecionar para IFSP** (`/redirect`): Redireciona o usuário para o site oficial do IFSP.

## Como executar

1. Instale o Flask (se necessário):
   ```powershell
   pip install flask
2. Execute o arquivo principal:
    ```powershell
   python appflask

3. Acesse
   ```powershell
    http://localhost:5000
  
## Sobre
Desenvolvido para fins didáticos na disciplina PTBDSWS.
