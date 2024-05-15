from fastapi import APIRouter
from models.cliente import Cliente
from config.database import cliente_table

router = APIRouter(
    prefix="/cliente",
    tags=["cliente"]
)

# GET Request Method
@router.get("/")
async def get_clientes():
    response = cliente_table.scan()
    clientes = response['Items']
    return clientes

# POST Request Method
@router.post("/")
async def post_cliente(cliente: Cliente):
    response = cliente_table.put_item(Item=dict(cliente))
    return response
