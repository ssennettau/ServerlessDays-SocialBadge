import io
import os

import boto3

BUCKET_NAME = os.environ["TARGET_BUCKET"]
BUCKET_PATH = "https://" + BUCKET_NAME + ".s3.amazonaws.com/generated/"

def check_img_exists(hash):
    filename = hash + ".png"
    resource = boto3.resource("s3")

    try:
        resource.Object(BUCKET_NAME, "/generated/" + filename).load()
    except:
        # Cache Miss
        return False
    # Cache Hit
    return BUCKET_PATH + filename

def upload_img_to_s3(filename, contents):
    try:
        client = boto3.client("s3")

        data = io.BytesIO(contents)

        client.put_object(
            Body = data,
            Bucket = BUCKET_NAME,
            Key = ("generated/" + filename)
        )

        path = BUCKET_PATH + filename
    except Exception as e:
        print("broken af> " + str(e))
        return False
    
    return path
