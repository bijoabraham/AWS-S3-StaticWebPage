def lambda_handler(event, context):
    message = "Message from server : {} {}!".format("You searched for - ",event["queryStringParameters"]['search'] ) 
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": message
    }    
    return resp