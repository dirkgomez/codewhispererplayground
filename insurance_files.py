import boto3


class InsuranceFiles:

    bucket_name = 'insurance-files'
    s3_resource = boto3.resource('s3')
    def __init__(self):
        pass

    # read item from s3 bucket
    def read_item(self, key):
        s3_resource.Object(self.bucket_name, key).get()

