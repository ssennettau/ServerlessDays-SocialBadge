import json

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

import slsdaysbadge
import s3
import utils

logger = Logger()

@logger.inject_lambda_context
def handler(event: dict, context: LambdaContext):
    print(event) #TODO: DEBUG

    # Parse out the event
    data = utils.parse_multipart(event["body"])
    hash = utils.hash_request(data)

    # Check if it's already been created
    exists = s3.check_img_exists(hash)
    if exists:
        # If exists, pass back the URL
        upload = exists
    else:
        # If not, create the badge
        badge = slsdaysbadge.build_badge(
            in_headshot = data["headshot"],
            in_name = data["name"],
            in_title = data["title"],
        )

        # Upload to S3
        upload = s3.upload_img_to_s3(
            (hash + ".png"),
            badge,
        )

    logger.info({
        "name": data["name"],
        "title": data["title"],
        "path": upload,
        "cache": exists,
    })

    return {
        "statusCode": 200,
        "headers": utils.cors_headers,
        "body": json.dumps({
            "uri": upload,
        }),
    }
