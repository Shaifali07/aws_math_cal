import json
import math
import boto3
from time import gmtime, strftime


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('power_of_math')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())


def lambda_handler(event, context):
   
    base = int(event['base'])
    operation=str(event['operation'])
    exponent=int(event['exponent'])
    
    if operation == "+":
            mathResult = base + exponent
    elif operation == "-":
            mathResult = base - exponent
    elif operation == "*":
            mathResult = base * exponent
    elif operation == "/":
            if exponent != 0:
                mathResult = base / exponent
            else:
                 mathResult ="Error: Division by zero"
    elif operation == "^":
            mathResult = math.pow(base, exponent)
    else:
             mathResult = "Invalid argument: Operation not recognized"

    response = table.put_item(
        Item={
            'id': str(now)+str(base)+str(exponent)+str(operation),
            'Number1': str(base),
            'Number2': str(exponent),
            'operation': str(operation),
            'result': str(mathResult)
       
            })


    return {
    'statusCode': 200,
    'body': json.dumps(str(mathResult))
    }