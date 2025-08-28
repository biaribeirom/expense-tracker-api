# ExpenseTracker API – AC1 (Projeto de Cloud)

API REST desenvolvida em FastAPI para controle financeiro pessoal.  
Permite cadastrar receitas e despesas, consultar saldo e buscar transações com filtros.

## links 
- repositório GitHub: https://github.com/biaribeirom/expense-tracker-api
- API no Azure: [https://seu-app.azurewebsites.net](https://expensetrackermulheres-d8c0byewhredd9aq.centralus-01.azurewebsites.net/ )

## funcionalidades
- cadastrar transações (receita ou despesa)
- categorizar receitas e despesas
- listar todas as transações
- buscar transações por ID
- atualizar ou deletar transações
- consultar saldo atual
- buscar transações com filtros (tipo, categoria, termo na descrição)

## endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | mensagem de boas-vindas |
| GET | `/transacoes` | listar todas as transações |
| POST | `/transacoes` | criar nova transação |
| GET | `/transacoes/{id}` | buscar transação por ID |
| PUT | `/transacoes/{id}` | atualizar transação |
| DELETE | `/transacoes/{id}` | deletar transação |
| GET | `/transacoes/buscar` | buscar com filtros (categoria, tipo, termo) |
| GET | `/saldo` | consultar saldo atual |

## como rodar localmente

1. clonar o repositório:
```
   git clone https://github.com/SEU-USUARIO/expense-tracker-api.git
   cd expense-tracker-api
```

2. criar e ativar ambiente virtual 
```
   python -m venv venv
   venv\Scripts\activate
```
3. instalar dependencias
```
  pip install -r requirements.txt
```
4. rodar 
```
  uvicorn main:app --reload
```
5. acessar no navegador 
    http://127.0.0.1:8000/


### integrantes e responsabilidades 
- Maria Beatriz - Models, validações, documentação
- Juliane - Rotas (CRUD e saldo)
- Adriana - Deploy no Azure e testes

### tecnologias usadas
- FastAPI 
- Uvicorn
- Python 
- Azure App Service

### testes
para testar a API, utilizar o arquivo 'tests.http' incluso no repositório 
contém exemplos de reqisições para todos os endpoints, incluindo casos de validação 


