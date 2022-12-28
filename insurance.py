import boto3


class Insurance:

    tableName = 'insurance'

    def getitems(self):
        client = boto3.resource('dynamodb')
        table = client.Table(self.tableName)
        response = table.scan()
        return response['Items']

    def getitem(self, id):
        client = boto3.resource('dynamodb')
        table = client.Table(self.tableName)
        response = table.get_item(Key={'id': id})
        return response['Item']

    def putitem(self, item):
        client = boto3.resource('dynamodb')
        table = client.Table(self.tableName)
        response = table.put_item(Item=item)
        return response

    def queryitem(self, id):
        client = boto3.resource('dynamodb')
        table = client.Table(self.tableName)
        response = table.query(KeyConditionExpression=Key('id').eq(id))
        return response['Items']
