import boto3
import csv

def handle(event):
    # List all files in bucket
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    
    # get_csv_data_from_bucket
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket = bucket, Key = key)
    data = s3_object['Body'].read().decode('utf-8')
    csv_data = csv.reader(data.splitlines())
    print(csv_data)
