import json
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    # create a bucket
    print(json.dumps(event, default=str))
    s3.create_bucket(Bucket=event.get('name'))


    response = s3.list_buckets()
    # print(response)
    
    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
        
    return json.dumps(response, default=str)