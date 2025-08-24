from pydantic import BaseModel, Field, field_validator, FieldValidationInfo 
from typing import Optional, Literal
from datetime import datetime


#dicionário com conjuntos de categorias permitidas por tipo (usamos na validação)
CATEGORIAS = {
    "receita": {"Salário", "Freelance", "Vendas", "Outros"},
    "despesa": {"Alimentação", "Transporte", "Lazer", "Contas", "Outros"},
}

#fala quais campos existem e o que cada um precisa obedecer na transação
class TransacaoBase(BaseModel): #herda de BaseModel
    id: Optional[int] = None #opcional
    descricao: str = Field(..., min_length=3, max_length=100) #obrigatorio entre 3 e 100 caracteres
    valor: float = Field(..., gt=0) #obrigatorio e positivo
    tipo: Literal["receita", "despesa"] #só tem essas duas opçções
        #se for receita, pode ser 'salario', 'freelance' 'vendas', 'outros'
        #se for despesa, pode ser 'alimentação', 'transporte', 'lazer', 'contas', 'outros'
    categoria: str
    data_criacao: Optional[datetime] = None
   
   #verifica se a categoria está dentro do conjunto permitido para o tipo
   #se o usuario escrever qualuqer coisa que nao seja 'receita' ou 'tipo' , ele vai barrar , por exemplo
    @field_validator("categoria") 
    @classmethod
    def categoria_compativel(cls, v: str, info: FieldValidationInfo) -> str:
        v = v.strip() 
        tipo = info.data.get("tipo")
        if tipo and v not in CATEGORIAS[tipo]:
            raise ValueError("Categoria inválida para o tipo informado")
        return v

#pydantic valida todos os campos que colocamos em cima; 
#pega o tipo já validado; verifica se a categoria (v) está em categorias(tipo); se nao tiver da erro 

class Transacao(TransacaoBase):
    pass
