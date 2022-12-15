import json
import boto3
import os

def lambda_handler(event, context):
  data = boto3.client('dynamodb').scan(TableName=os.environ['TableName'])

  Items = []

  for item in data['Items']:
    if item['type'] == 'taikamatto':
      Items.append(item)

  response = {
      'statusCode': 200,
      'body': json.dumps(Items),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response