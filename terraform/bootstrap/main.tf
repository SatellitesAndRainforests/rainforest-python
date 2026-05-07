
# import Terraform +  AWS provider version.

terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }

}

# use London AWS region.
provider "aws" {
  region = "eu-west-2"
}



# get the current AWS account ID  (for a unique S3 bucket name).
data "aws_caller_identity" "current" {}

# reusable project name.
locals {
  project_name = "rainforest-python"
}



# S3 bucket for storing Terraform remote state.
resource "aws_s3_bucket" "terraform_state" {
  bucket        = "${local.project_name}-tf-state-${data.aws_caller_identity.current.account_id}"
  force_destroy = true

  tags = {
    Name    = "${local.project_name}-tf-state"
    Project = local.project_name
  }

}

# block public access to the Terraform state bucket.
resource "aws_s3_bucket_public_access_block" "terraform_state_public_access" {
  bucket = aws_s3_bucket.terraform_state.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Keep previous versions of the Terraform state file.
resource "aws_s3_bucket_versioning" "terraform_state_versioning" {
  bucket = aws_s3_bucket.terraform_state.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Encrypt the Terraform state file at rest.
resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state_encryption" {
  bucket = aws_s3_bucket.terraform_state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}



# dynamoDB table used to lock Terraform state during apply/destroy.
resource "aws_dynamodb_table" "terraform_lock" {
  name         = "${local.project_name}-tf-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name    = "${local.project_name}-tf-lock"
    Project = local.project_name
  }
}



# Print the S3 bucket name for terraform/app/backend.tf.
output "s3_bucket" {
  value = aws_s3_bucket.terraform_state.bucket
}

# Print the DynamoDB lock table name for terraform/app/backend.tf.
output "dynamodb_table" {
  value = aws_dynamodb_table.terraform_lock.name
}


