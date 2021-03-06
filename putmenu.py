import boto3
import json

print('Loading function')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    print("Received event: " + json.dumps(event, indent=2))



    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')

    table = dynamodb.Table('menu')
    
    try :
        response = table.update_item(
        Key={
            'menu_id': event['menu_id']
        },
        UpdateExpression="set selection = :val",
        ExpressionAttributeValues={
            ':val': event['selection']
        }
        )
        print("UpdateItem succeeded:")
        #print(json.dumps(response, indent=4))
        return "Success"
    except Exception:
        return "Exception on Update"

