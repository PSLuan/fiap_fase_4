from fastapi import FastAPI
from routes import cliente, pedido

app = FastAPI()

app.include_router(cliente.router)
app.include_router(pedido.router)