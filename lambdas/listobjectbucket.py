import json, boto3

def lambda_handler(event, clusters):

    s3 = boto3.client('s3')
    eventbody = event.get("body")
    response = s3.list_objects(Bucket = json.loads(eventbody).get("name"))

    response={'body' : json.dumps(response, default = str),'statusCode' : 200}

    return response