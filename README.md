# Sentence Embedding Deployment

Start an EC2 with at least 200GB EBS volume.

Permission:

- ECR full access
- Cloudformation full access

```text
denied: User: arn:aws:sts::376167692487:assumed-role/Dev-Data-Science/i-0cea44f01316d9eb6 is not authorized to perform: ecr:InitiateLayerUpload on resource: arn:aws:ecr:ap-southeast-2:376167692487:repository/getembeddingfunc

Error: Failed to create managed resources: An error occurred (AccessDenied) when calling the CreateChangeSet operation: User: arn:aws:sts::376167692487:assumed-role/Dev-Data-Science/i-0cea44f01316d9eb6 is not authorized to perform: cloudformation:CreateChangeSet on resource: arn:aws:cloudformation:ap-southeast-2:376167692487:stack/aws-sam-cli-managed-default/*

```

## Download model

```bash
NAME="distilbert-base-nli-stsb-mean-tokens"
wget https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/v0.2/${NAME}.zip -O model.zip
mkdir -p src/model
mv model.zip src/model
cd src/model; unzip model.zip
```

## Build

Run this on project root directory.

```bash
sam build --use-container
```

## Local Test

Do a local test to check if the model is returning embeddings.

```bash
sam local invoke GetEmbeddingFunc --event events/event.json
```

## Deploy

Get credential to AWS container registry.
`376167692487.dkr.ecr.ap-southeast-2.amazonaws.com/embedding` has already been created.

```bash
aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 376167692487.dkr.ecr.ap-southeast-2.amazonaws.com

docker tag getembeddingfunc:python3.7-v1 376167692487.dkr.ecr.ap-southeast-2.amazonaws.com/getembeddingfunc:latest

docker push 376167692487.dkr.ecr.ap-southeast-2.amazonaws.com/getembeddingfunc:latest

sam deploy --guided
```

## AWS ECR

The repo name should match the CFN template logical id (lowercase), `getembeddingfunc` in this case.

## Clean up

```bash
aws cloudformation delete-stack --stack-name sam-app
```
