import subprocess
import os
import boto3



if __name__ == "__main__":

    # list of stack names using boto3
    boto3.setup_default_session(region_name='eu-west-1')
    client = boto3.client('s3')
    # list buckets
    response = client.list_buckets()
    bucket_names = []
    for bucket in response['Buckets']:
        bucket_names.append(bucket['Name'])
        
        if "dmh" not in bucket['Name']:
            # delete objects in bucket
            paginator = client.get_paginator('list_objects_v2')
            for result in paginator.paginate(Bucket=bucket['Name']):
                if 'Contents' in result:
                    for key in result['Contents']:
                        client.delete_object(
                            Bucket=bucket['Name'],
                            Key=key['Key']
                        )
            try:
                client.delete_bucket(
                    Bucket=bucket['Name']
                )
                print(bucket)
            except Exception as e:
                print(e)
                continue    