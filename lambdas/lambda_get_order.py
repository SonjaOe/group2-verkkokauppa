import json
import boto3
import os

#lambda for getting a spesific order from dynamoDB
def lambda_handler(event, context):
    data = boto3.client('dynamodb').get_item(TableName=os.environ['TableName'], Key=json.dump(event['body']))
    response = {
        'statusCode': 200,
        'body': json.dumps(data['Items']),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    return response