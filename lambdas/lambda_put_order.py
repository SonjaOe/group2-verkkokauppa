import json
import boto3
import os

#lambda for putting order to dynamoDB
def lambda_handler(event, context):
    data = boto3.client('dynamodb').put_item(TableName=os.environ['TableName'], Item=json.loads(event['body']))
    message_to_send = json.dumps(event['body'])
    client = boto3.client('sns')
    response = client.publish(TopicArn = os.environ['TopicArn'], Message = message_to_send, Subject = 'Your magic carpet order')
    response = {
        'statusCode': 200,
        'body': json.dumps(event['body']),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    return response