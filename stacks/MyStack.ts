import { StackContext, Api } from "sst/constructs";

export function API({ stack }: StackContext) {
  const api = new Api(stack, "api", {
    routes: {
      "POST /badge": "packages/functions/src/handler.py",
    },
  });

  stack.addOutputs({
    ApiEndpoint: api.url,
  });
}
