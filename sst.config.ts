import { SSTConfig } from "sst";
import { Api, Function } from "sst/constructs";
import { Bucket } from "aws-cdk-lib/aws-s3";
import { RemovalPolicy } from "aws-cdk-lib/core";

export default {
  config(_input) {
    return {
      name: "ServerlessDays-SocialBadge",
      region: "us-east-1",
    };
  },
  stacks(app) {
    app.stack(function Site({ stack }) {
      const badgeBucket = new Bucket(stack, "badgeBucket", {
        removalPolicy: RemovalPolicy.DESTROY,
      });

      const badgeFunction = new Function(stack, "badgeFunction", {
        handler: "src/handler.handler",
        timeout: 20,
        memorySize: 1024,
        runtime: "python3.11",
        environment: {
          "TARGET_BUCKET": badgeBucket.bucketName,
        },
        permissions: [
          badgeBucket,
        ],
      })

      const api = new Api(stack, "api", {
        routes: {
          "POST /badge": badgeFunction,
        }
      });
      
      stack.addOutputs({
        ApiEndpoint: api.url,
        BadgeBucket: badgeBucket.bucketArn,
      })
    });
  }
} satisfies SSTConfig;
