import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    print(event)
    eventbody=(json.loads(event.get("body")))
    # eventbody = event.get("body")
    table = dynamodb.Table('myDynamoTable')
    
    # print(type(eventbody))
    print(eventbody)
    # put item into table
    table.put_item(Item=eventbody)
    
    #get item from table
    itemresponse = table.get_item(
    Key=eventbody
    )
    # item = response['Item']
    response={}
    response["body"] = json.dumps(itemresponse, default=str)
    response["statusCode"] = 200

    return response