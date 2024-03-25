import io
import os

import boto3

bucket = os.environ["TARGET_BUCKET"]

def upload_img_to_s3(filename, contents):
    try:
        client = boto3.client("s3")

        data = io.BytesIO(contents)

        response = client.put_object(
            Body = data,
            Bucket = bucket, 
            Key = ("generated/" + filename)
        )

        path = "https://" + bucket + "s3.amazonaws.com/generated/" + filename
    except Exception as e:
        print("broken af> " + str(e))
        return False
    
    return path
