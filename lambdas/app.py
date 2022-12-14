import json
import boto3


def lambda_handler(event, context):
  data = boto3.client('dynamodb').scan(TableName='Project4Group2Table')

  response = {
      'statusCode': 200,
      'body': json.dumps(data['Items']),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response