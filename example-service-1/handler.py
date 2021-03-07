import json

def start(event):
    body = {
        "message": "Your function executed for service 2!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response