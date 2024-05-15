import boto3, os

REGION_NAME=os.getenv("REGION_NAME")
AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")

dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

pedido_table_name = 'pedido_collection'
cliente_table_name = 'cliente_collection'

pedido_table = dynamodb.Table(pedido_table_name)
cliente_table = dynamodb.Table(cliente_table_name)