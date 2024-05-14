from fastapi import APIRouter
from models.pedido import PedidoCompleto
from config.database import pedido_table
#from schema.schemas import pedido_list_serial

router = APIRouter(
    prefix="/pedido",
    tags=["pedido"]
)

# GET Request Method
@router.get("/")
async def get_pedidos():
    response = pedido_table.scan()
    pedidos = response['Items']
    return pedidos

# POST Request Method
@router.post("/")
async def post_pedido(pedido: PedidoCompleto):
    pedido_dict = pedido.dict()
    pedido_dict['cliente'] = pedido.cliente.dict()
    pedido_dict['status'] = pedido.status.dict()
    pedido_dict['produtos'] = [produto.dict() for produto in pedido.produtos]
    pedido_dict['_id'] = str(pedido_dict['id'])
    response = pedido_table.put_item(Item=pedido_dict)
    return response