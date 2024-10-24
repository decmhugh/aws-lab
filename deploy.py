import subprocess

def deploy_cloudformation(stack_name, template_file, s3_bucket, region):
    try:
        # Package the CloudFormation template
        package_command = [
            "sam", "package",
            "--template-file", template_file,
            "--output-template-file", "packaged.yaml",
            "--s3-bucket", s3_bucket
        ]
        subprocess.run(package_command, check=True)

        # Deploy the packaged template
        deploy_command = [
            "sam", "deploy",
            "--template-file", "packaged.yaml",
            "--stack-name", stack_name,
            "--capabilities", "CAPABILITY_IAM",
            "--region", region
        ]
        subprocess.run(deploy_command, check=True)

        print(f"Stack {stack_name} deployed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    stack_name = "dmh-aws-lake-formation"
    template_file = "aws-lake-formation/template.yaml"
    s3_bucket = "your-s3-bucket"
    region = "eu-west-1"

    deploy_cloudformation(stack_name, template_file, s3_bucket, region)