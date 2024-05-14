### PEDIDO ###
def pedido_individual_serial(pedido_completo) -> dict:
    return {
        "id": str(pedido_completo["_id"]),
        "cliente": pedido_completo["cliente"],
        "status": pedido_completo["status"],
        "produtos": pedido_completo["produtos"]
    }

def pedido_list_serial(pedidos_completos) -> list:
    return[pedido_individual_serial(pedido_completo) for pedido_completo in pedidos_completos]

###CLIENTE###
def cliente_individual_serial(cliente) -> dict:
    return {
        "id": str(cliente["_id"]),
        "cpf": cliente["cpf"],
        "nome": cliente["nome"],
        "email": cliente["email"]
    }

def cliente_list_serial(clientes) -> list:
    return [cliente_individual_serial(cliente) for cliente in clientes]