import json

print('Loading function')

def lambda_handler(event, context):
    #1. parse out query string params
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print('transactionId=' + transactionId)
    print('transactionType=' + transactionType)
    print('transactionAmount=' + transactionAmount)

    #2. construct body of response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'This is Simplified Insurance, we read you'

    #3. construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    #4. return response object
    return responseObject