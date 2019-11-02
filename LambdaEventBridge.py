import json
import boto3

def lambda_handler(event, context):
    print("[lambda_handler] Start :", event)
    response = {}
    try:
        client = boto3.client('events')
        
        if event.get('api') is None:
            return getReqiredErrorMessage('Null', 'api')
        
        if event['api'] == 'listRules':
            if event.get('name') is None:
                response = client.list_rules()
            else:
                response = client.list_rules(NamePrefix=event['name'])
        elif event['api'] == 'describeRule':
            if event.get('name') is None:
                response = getReqiredErrorMessage(event['api'], 'name')
            else :
                response = client.describe_rule(Name=event['name'])
        elif event['api'] == 'enableRule':
            if event.get('name') is None:
                response = getReqiredErrorMessage(event['api'], 'name')
            else :
                response = client.enable_rule(Name=event['name'])
        elif event['api'] == 'disableRule':
            if event.get('name') is None:
                response = getReqiredErrorMessage(event['api'], 'name')
            else :
                response = client.disable_rule(Name=event['name'])
        else:
            response = getErrorMessage(event['api'])
    except Exception as e:
        raise e
        response = {
            'errorMessage' : e
        }

    print("[lambda_handler] End")
    return response

def getReqiredErrorMessage(api, field):
    return {
        'errorMessage' : '{} - The {} of the rule is Required... : {}(string)'.format(api, field, field)
    }
    
def getErrorMessage(api):
    return {
        'The Reqeust({}) is not supported.'.format(api)
    }