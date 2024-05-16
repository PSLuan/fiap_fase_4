from fastapi import APIRouter
from models.pedido import PedidoCompleto
from config.database import pedido_table
from pydantic import BaseModel
from boto3.dynamodb.conditions import Attr

router = APIRouter(
    prefix="/pedido",
    tags=["pedido"]
)

class UpdateStatusRequest(BaseModel):
    id: str
    status: str

# GET Request Method
@router.get("/")
async def get_pedidos():
    response = pedido_table.scan()
    pedidos = response['Items']
    return pedidos

# GET Request Method Based On Status
@router.get("/{status}")
async def get_pedidos(status: str):
    response = pedido_table.scan(
        FilterExpression=Attr('status').eq(status)
    )
    pedidos = response.get('Items', [])
    return pedidos

# POST Request Method
@router.post("/")
async def post_pedido(pedido: PedidoCompleto):
    pedido_dict = pedido.dict()
    pedido_dict['cliente'] = pedido.cliente.dict()
    pedido_dict['produtos'] = [produto.dict() for produto in pedido.produtos]
    pedido_dict['_id'] = str(pedido_dict['id'])
    pedido_table.put_item(Item=pedido_dict)    
    return pedido_dict

# PATCH Request Method
@router.patch("/")
async def update_pedido_status(request: UpdateStatusRequest):
    response = pedido_table.update_item(
        Key={'_id': request.id},
        UpdateExpression="set #s = :status",
        ExpressionAttributeNames={
            '#s': 'status'
        },
        ExpressionAttributeValues={
            ':status': request.status
        },
        ReturnValues="UPDATED_NEW"
    )
    return response