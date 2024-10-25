import subprocess
import os
import boto3


def deploy_cloudformation(stack_name, template_file, s3_bucket, region):
    cmd = f"sam deploy --template-file {template_file} --stack-name {stack_name} --s3-bucket {s3_bucket}" + \
        " --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --region {region} --no-fail-on-empty-changeset"
    subprocess.check_call(cmd, shell=True)

if __name__ == "__main__":

    #stack_name = "dmh-aws-vpc-multi-tier"
    #template_file = os.getcwd().replace('\\','/') + "/aws-vpc-multi-tier/template.yaml"
    stack_name = ["dmh-aws-lake-initial-setup",
                  "dmh-aws-lake-datadomain-dev",
                  "dmh-aws-lake-foundations-dev"]
    
    template_file = ["aws-lake-formation/initial-setup.yaml",
                     "aws-lake-formation/datadomain-datalake-dev.yaml",
                     "aws-lake-formation/foundations-datalake-dev.yaml"]
    #s3_bucket = "dmh-default-bucket"
    #region = "eu-west-1"

    #deploy_cloudformation(stack_name, template_file, s3_bucket, region)
    print(os.getcwd())

    
    s3_bucket = "dmh-default-bucket"
    region = "eu-west-1"
    
    # Check file exists
    
    for i in range(len(stack_name[:1])):
        if os.path.isfile(template_file[i]):
            print("File exists")
        else:
            print("File does not exist")
            exit(1)
        deploy_cloudformation(stack_name[i], template_file[i], s3_bucket, region)