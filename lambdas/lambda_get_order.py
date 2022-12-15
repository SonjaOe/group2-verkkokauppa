import json
import boto3
import os

def lambda_handler(event, context):
  client = boto3.client('dynamodb')
  response = client.get_item(
    Key={
        'type': {
            'S': 'order',
        },
        'id': {
            'N': event['pathParameters']['id'],
        },
    },
    TableName=os.environ['TableName'],
)

  response = {
      'statusCode': 200,
      'body': json.dumps(response),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response