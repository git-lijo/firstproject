aws cloudformation package --template lambdatemplate.yml --s3-bucket lijobucket --output-template lambdatemplate-export.yml
aws cloudformation deploy --template-file lambdatemplate-export.yml --stack-name awsdemo1 --s3-bucket lijobucket