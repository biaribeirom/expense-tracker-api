# AC - ExpenseTracker API

**Disciplina:** Projeto de Cloud  
**Prazo:** 27/08 
**Formato:** Duplas ou trios  

## Objetivo

Desenvolver uma API REST completa para controle financeiro pessoal, aplicando os conceitos de FastAPI e Azure App Service aprendidos em aula.

## Descrição do Projeto

**ExpenseTracker** é um sistema simples para gerenciar receitas e despesas pessoais, permitindo:
- Cadastrar transações financeiras
- Categorizar receitas e despesas
- Consultar saldo atual
- Buscar transações com filtros

## Especificação Técnica

### Modelo de Dados
```python
class Transacao(BaseModel):
    id: Optional[int] = None
    descricao: str = Field(..., min_length=3, max_length=100)
    valor: float = Field(..., gt=0)
    categoria: str = Field(...)
    tipo: str = Field(...)  # "receita" ou "despesa"
    data_criacao: Optional[datetime] = None
```

### Categorias Válidas
- **Receitas:** Salário, Freelance, Vendas, Outros
- **Despesas:** Alimentação, Transporte, Lazer, Contas, Outros

### Validações Obrigatórias
- Valor deve ser positivo
- Tipo deve ser "receita" ou "despesa"
- Categoria deve existir na lista para o tipo correspondente
- Descrição entre 3 e 100 caracteres

## Endpoints Obrigatórios

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Mensagem de boas-vindas |
| GET | `/transacoes` | Listar todas as transações |
| POST | `/transacoes` | Criar nova transação |
| GET | `/transacoes/{id}` | Buscar transação por ID |
| PUT | `/transacoes/{id}` | Atualizar transação |
| DELETE | `/transacoes/{id}` | Deletar transação |
| GET | `/transacoes/buscar` | Busca com filtros |
| GET | `/saldo` | Saldo atual |

### Filtros de Busca
- `categoria` - Filtrar por categoria específica
- `tipo` - Filtrar por receita ou despesa
- `termo` - Buscar na descrição

**Exemplo:** `/transacoes/buscar?tipo=despesa&categoria=Alimentação`

### Resposta do Saldo
```json
{
    "saldo_atual": 1500.75,
    "total_receitas": 3000.00,
    "total_despesas": 1499.25
}
```

## Entregáveis

### 1. API Funcionando
- URL pública do Azure App Service
- Todos os 8 endpoints implementados
- Validações funcionando corretamente

### 2. Documentação
- **README.md** contendo:
  - Descrição do projeto
  - Link Github
  - URL da API no Azure
  - Lista dos endpoints
  - Instruções de como testar
  - **Nomes de todos os integrantes da equipe**
  - Divisão de responsabilidades (quem fez o quê verificavel por commits)

### 3. Testes
- Arquivo .http com testes de todos os endpoints
- Incluir testes de validação (casos de erro)
- Testes devem funcionar tanto local quanto no Azure

## Exemplos de Testes

```http
### 1. Verificar API
GET {{host}}/

### 2. Criar receita
POST {{host}}/transacoes
Content-Type: application/json

{
    "descricao": "Salário Agosto",
    "valor": 3000.00,
    "categoria": "Salário",
    "tipo": "receita"
}

### 3. Criar despesa
POST {{host}}/transacoes
Content-Type: application/json

{
    "descricao": "Supermercado",
    "valor": 150.50,
    "categoria": "Alimentação",
    "tipo": "despesa"
}

### 4. Buscar todas
GET {{host}}/transacoes

### 5. Buscar por tipo
GET {{host}}/transacoes/buscar?tipo=despesa

### 6. Ver saldo
GET {{host}}/saldo

### 7. Teste de validação (deve falhar)
POST {{host}}/transacoes
Content-Type: application/json

{
    "descricao": "Teste",
    "valor": -100,
    "categoria": "Inválida",
    "tipo": "receita"
}

@host = https://seu-app.azurewebsites.net
```

## Forma de Entrega

**Enviar pelo SAVA até 27/08 - UM TRABALHO POR EQUIPE:**
1. URL da API no Azure
2. Link do repositório GitHub 
3. Arquivo README.md
4. Arquivo de testes .http

**Assunto:** [NOMES DOS INTEGRANTES] - AC ExpenseTracker  
**Importante:** Apenas um integrante envia, mas deve incluir todos os nomes