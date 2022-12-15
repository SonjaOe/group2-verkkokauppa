import json
import boto3
import os

def lambda_handler(event, context):
  data = boto3.client('dynamodb').scan(TableName=os.environ['TableName'], ExpressionAttributeValues={':a': {'S': 'taikamatto',},}, FilterExpression='Artist = :a',)

  response = {
      'statusCode': 200,
      'body': json.dumps(data['Items']),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response