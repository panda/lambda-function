import json
import urllib
import boto3

def lambda_handler(event, context):

    # Init aws
    s3 = boto3.client('s3')
    
    # Get bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']

    # Get file name (key)
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        # Fetch
        response = s3.get_object(Bucket=bucket, Key=key)

        # deserialize
        text = response["Body"].read().decode()
        data = json.loads(text)

        # print
        print(data)

        # Parse
        transactions = data['transactions']
        for record in transactions:
            print(record['transType'])
        return 'We are done boys'

    except Exception as e:
        print(e)
        raise e
    # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }