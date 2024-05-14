from typing import List, Optional
from models.cliente import Cliente
from models.status import Status
from models.produto import Produto
from pydantic import BaseModel


class PedidoBase(BaseModel):
    codigo: str
    id_cliente: int
    id_status: int
    produtos: List[int]


class Pedido(PedidoBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class PedidoCompleto(Pedido):
    cliente: Cliente
    status: Status
    produtos: List[Produto]