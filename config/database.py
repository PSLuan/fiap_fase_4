import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2', aws_access_key_id='AKIAU6GDWYXJRJD36CER', aws_secret_access_key='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')

pedido_table_name = 'pedido_collection'
cliente_table_name = 'cliente_collection'

pedido_table = dynamodb.Table(pedido_table_name)
cliente_table = dynamodb.Table(cliente_table_name)