from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from models import TransacaoBase

app = FastAPI(title="Expense Tracker API (AC1)", version="1.0.0")

# "banco de dados" em memória (lista) + contador de IDs (padrão didático)
transacoes_db: List[TransacaoBase] = []
next_id = 1


@app.get("/")
def root():
    return {"message": "Expense Tracker API - AC1 (Transações)"}


# LISTAR TODAS
@app.get("/transacoes", response_model=List[TransacaoBase])
def listar_transacoes():
    return transacoes_db


# CRIAR
@app.post("/transacoes", response_model=TransacaoBase, status_code=201)
def criar_transacao(payload: TransacaoBase):
    """
    A validação de campos (descricao, valor>0, tipo, categoria compatível)
    já é feita automaticamente pelo seu models (Pydantic).
    Aqui só preenchemos id e data_criacao no servidor.
    """
    global next_id

    nova = TransacaoBase(
        id=next_id,
        descricao=payload.descricao,
        valor=payload.valor,
        tipo=payload.tipo,
        categoria=payload.categoria,
        data_criacao=datetime.now()  
    )
    transacoes_db.append(nova)
    next_id += 1
    return nova


# BUSCAR POR ID
@app.get("/transacoes/{id}", response_model=TransacaoBase)
def buscar_transacao(id: int):
    t = next((x for x in transacoes_db if x.id == id), None)
    if not t:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return t


# ATUALIZAR (substituição completa)
@app.put("/transacoes/{id}", response_model=TransacaoBase)
def atualizar_transacao(id: int, payload: TransacaoBase):
    """
    Mantemos o mesmo id e preservamos a data_criacao original (se houver).
    Caso a transação não exista, 404.
    """
    idx = next((i for i, x in enumerate(transacoes_db) if x.id == id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    antiga = transacoes_db[idx]
    atualizada = TransacaoBase(
        id=id,
        descricao=payload.descricao,
        valor=payload.valor,
        tipo=payload.tipo,
        categoria=payload.categoria,
        data_criacao=antiga.data_criacao or datetime.now()
    )
    transacoes_db[idx] = atualizada
    return atualizada


# DELETAR
@app.delete("/transacoes/{id}", status_code=204)
def deletar_transacao(id: int):
    idx = next((i for i, x in enumerate(transacoes_db) if x.id == id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    transacoes_db.pop(idx)
    return None  # 204 No Content


# BUSCA COM FILTROS
@app.get("/transacoes/buscar", response_model=List[TransacaoBase])
def buscar_com_filtros(
    categoria: Optional[str] = Query(None, description="Ex.: Alimentação, Transporte, ..."),
    tipo: Optional[str] = Query(None, description='Ex.: "receita" ou "despesa"'),
    termo: Optional[str] = Query(None, description="Termo contido na descrição")
):
    """
    Filtros simples: categoria, tipo e termo (na descrição).
    São combináveis (AND).
    """
    resultados = transacoes_db
    if categoria:
        resultados = [t for t in resultados if (t.categoria or "").lower() == categoria.lower()]
    if tipo:
        resultados = [t for t in resultados if (t.tipo or "").lower() == tipo.lower()]
    if termo:
        resultados = [t for t in resultados if termo.lower() in (t.descricao or "").lower()]
    return resultados


# SALDO (receitas - despesas)
@app.get("/saldo")
def obter_saldo():
    total_receitas = sum(t.valor for t in transacoes_db if t.tipo == "receita")
    total_despesas = sum(t.valor for t in transacoes_db if t.tipo == "despesa")
    saldo_atual = total_receitas - total_despesas
    return {
        "saldo_atual": round(saldo_atual, 2),
        "total_receitas": round(total_receitas, 2),
        "total_despesas": round(total_despesas, 2),
        "quantidade_transacoes": len(transacoes_db)
    }


# Execução direta com: python main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
