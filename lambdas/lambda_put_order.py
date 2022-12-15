import json
import boto3
import os

#lambda for putting order to dynamoDB
def lambda_handler(event, context):
    # data = boto3.client('dynamodb').put_item(TableName=os.environ['TableName'], Item=event['body'])
    response = {
        'statusCode': 200,
        'body': event,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    return response