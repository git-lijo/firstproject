import json
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    # create a bucket
    print(json.dumps(event.get("body"), default=str))
    eventbody = event.get("body")
    
    s3ob = (s3.create_bucket(Bucket=json.loads(eventbody).get("name")))

    
    listbucket_response = s3.list_buckets()
    # print(response)
    # response = {"msg"}
    response={}
    response["body"] = json.dumps(listbucket_response, default=str)
    response["statusCode"] = 200
    print(response)
    print(s3ob)
    
    
    # Output the bucket names
    # print('Existing buckets:')
    # for bucket in response['Buckets']:
    #     print(f'  {bucket["Name"]}')
    
    # print(json.dumps(response, default=str))
    
        
    return (response)