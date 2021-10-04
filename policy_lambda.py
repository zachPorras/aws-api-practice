import json

print('Loading function')

def lambda_handler(event, context):
    #1. parse out query string params
    transactionID = event['queryStringParameters']['transactionID']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print('transactionID=' + transactionID)
    print('transactionType=' + transactionType)
    print('transactionAmount=' + transactionAmount)

    #2. construct body of response object
    