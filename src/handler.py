import json

import slsdaysbadge
import s3uploader
import utils

cors_headers = {
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "OPTIONS,POST",
    "Access-Control-Expose-Headers": "X-Amzn-Trace-Id",
}

def handler(event, context):
    print(event) #TODO: DEBUG

    data = utils.parse_multipart(event["body"])
    hash = utils.hash_request(data)

    badge = slsdaysbadge.build_badge(
        in_headshot = data["headshot"],
        in_name = data["name"],
        in_title = data["title"],
    )

    # Upload to S3
    upload = s3uploader.upload_img_to_s3(
        (hash + ".png"),
        badge,
    )

    return {
        "statusCode": 200,
        "headers": cors_headers,
        "body": json.dumps({
            "uri": upload,
            "event": event,
        })
    }
