from typing import List, Optional
from pydantic import BaseModel
from decimal import Decimal


class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: Decimal
    id_categoria: int


class Produto(ProdutoBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True