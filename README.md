# Sentence Embedding Deployment

## Build

```bash
sam build --use-container
```

## Local Test

Test with a single invoke.

```bash
sam local invoke HelloWorldFunction --event events/event.json
```

Test with a local endpoint.

```bash
sam local start-api
curl http://localhost:3000/getemb/
```

## Deploy

```bash
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 342474125894.dkr.ecr.ap-southeast-1.amazonaws.com

docker tag getembeddingfunc:python3.7-v1 342474125894.dkr.ecr.ap-southeast-1.amazonaws.com/getembeddingfunc:latest

docker push 342474125894.dkr.ecr.ap-southeast-1.amazonaws.com/getembeddingfunc:latest

sam deploy --guided
```

## AWS ECR

The repo name should match the CFN template logical id (lowercase), `getembeddingfunc` in this case.

## Enable API Gateway (Optional)

Include the following in template.

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /getemb
            Method: get
```

## Clean up

```bash
aws cloudformation delete-stack --stack-name sam-app
```
