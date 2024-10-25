import subprocess
import os
import boto3



if __name__ == "__main__":

    # list of stack names using boto3
    boto3.setup_default_session(region_name='eu-west-1')
    client = boto3.client('cloudformation')
    response = client.list_stacks(
        StackStatusFilter=[
            'CREATE_COMPLETE',
            'UPDATE_COMPLETE',
            'ROLLBACK_COMPLETE'
        ]
    )
    stack_names = []
    for stack in response['StackSummaries']:
        stack_names.append(stack['StackName'])
        try:
            if "sdlf" in stack['StackName'] :
                client.delete_stack(
                    StackName=stack['StackName']
                )
                print(stack)
            if "dmh" in stack['StackName'] :
                client.delete_stack(
                    StackName=stack['StackName']
                )
                print(stack)
                
            
        except Exception as e:
            print(e)
            continue