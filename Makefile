SHELL := /bin/bash

# Load environment variables from .env file and export them
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python
AWS := $(VENV_DIR)/bin/aws

.PHONY: help install setup-credentials up down clean prepare-data upload-data stream-data

help:
	@echo "Commands:"
	@echo "  install          : Install python dependencies using uv"
	@echo "  setup-credentials: Setup AWS credentials for MinIO"
	@echo "  up               : Start MinIO container"
	@echo "  down             : Stop MinIO container"
	@echo "  clean            : Remove generated files and virtual environment"
	@echo "  prepare-data     : Prepare data for training"
	@echo "  upload-data      : Upload data to MinIO"
	@echo "  stream-data      : Stream data from MinIO"

install:
	@if ! command -v uv &> /dev/null; then \
		echo "uv not found, installing with curl..."; \
		(curl -LsSf https://astral.sh/uv/install.sh | sh) && \
		$$HOME/.cargo/bin/uv venv --python=3.10 && \
		$$HOME/.cargo/bin/uv pip install -r requirements.txt; \
	else \
		uv venv --python=3.10 && \
		uv pip install -r requirements.txt; \
	fi

setup-credentials:
	@if [ ! -f ~/.aws/credentials ]; then \
		mkdir -p ~/.aws && \
		echo "[default]" > ~/.aws/credentials && \
		echo "aws_access_key_id = ${AWS_ACCESS_KEY_ID}" >> ~/.aws/credentials && \
		echo "aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY}" >> ~/.aws/credentials; \
	fi
	@if [ ! -f ~/.aws/config ]; then \
		echo "[default]" > ~/.aws/config && \
		echo "region = us-east-1" >> ~/.aws/config && \
		echo "output = json" >> ~/.aws/config && \
		echo "endpoint_url = ${AWS_ENDPOINT_URL}" >> ~/.aws/config; \
	fi

up:
	@docker compose up -d

down:
	@docker compose down

clean:
	@rm -rf my_optimized_dataset/
	@rm -rf data/
	@rm -rf $(VENV_DIR)

prepare-data:
	@$(PYTHON) prepare_data.py

upload-data:
	@if ! $(AWS) s3api head-bucket --bucket "${MINIO_BUCKET}" 2>/dev/null; then \
		echo "Bucket '${MINIO_BUCKET}' does not exist. Creating..."; \
		$(AWS) s3 mb "s3://${MINIO_BUCKET}"; \
	else \
		echo "Bucket '${MINIO_BUCKET}' already exists."; \
	fi
	@echo "Uploading data to s3://${MINIO_BUCKET}/${OPTIMIZED_DATA_DIR}..."
	@$(AWS) s3 cp --recursive ${OPTIMIZED_DATA_DIR} s3://${MINIO_BUCKET}/${OPTIMIZED_DATA_DIR}

stream-data:
	@$(PYTHON) streaming_dataset.py