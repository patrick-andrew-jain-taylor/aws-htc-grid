# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Licensed under the Apache License, Version 2.0 https://aws.amazon.com/apache-2-0/

LAMBDA_AGENT_IMAGE_NAME=awshpc-lambda
LOCAL_AGENT_IMAGE_NAME=awshpc-local
TAG=mainline
ACCOUNT_ID?=$(shell aws sts get-caller-identity | jq -r '.Account')
REGION=eu-west-1
DOCKER_REGISTRY=$(ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com
CONTEXT_DIR=../../../..
SRCS=agent.py

.PHONY: all lambda local push-lambda build-lambda build-local push-local

all: lambda
lambda: build-lambda push-lambda
local: build-local push-local

build-lambda: Dockerfile.Lambda
	docker build $(CONTEXT_DIR) -t $(DOCKER_REGISTRY)/$(LAMBDA_AGENT_IMAGE_NAME):$(TAG) -f ./Dockerfile.Lambda

push-lambda: build-lambda
	docker push $(DOCKER_REGISTRY)/$(LAMBDA_AGENT_IMAGE_NAME):$(TAG)

build-local: Dockerfile.Local
	docker build $(CONTEXT_DIR) -t $(DOCKER_REGISTRY)/$(LOCAL_AGENT_IMAGE_NAME):$(TAG) -f ./Dockerfile.Local

push-local: build-local
	docker push $(DOCKER_REGISTRY)/$(LOCAL_AGENT_IMAGE_NAME):$(TAG)

test: $(SRCS)
	flake8  --ignore  E501,W503 --statistic --exclude build $(SRCS)