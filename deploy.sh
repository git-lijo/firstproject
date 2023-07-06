#!/bin/bash

aws cloudformation package --template template.yml --s3-bucket lijobucket --output-template template-export.yml
aws cloudformation deploy --template-file template-export.yml --stack-name awsdemo --s3-bucket lijobucket
