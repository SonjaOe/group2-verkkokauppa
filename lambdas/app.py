import json
import boto3

def lambda_handler(event, context):
  data = boto3.client('dynamodb').scan(TableName=process.env.DatabaseTable)

  response = {
      'statusCode': 200,
      'body': json.dumps(data['Items']),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response