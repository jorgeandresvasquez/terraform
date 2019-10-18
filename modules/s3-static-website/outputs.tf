output "hostname" {
  value       = var.bucket_name
  description = "Bucket name"
}

output "s3_bucket_name" {
  value       = aws_s3_bucket.default.id
  description = "DNS record of website bucket"
}

output "s3_bucket_domain_name" {
  value       = aws_s3_bucket.default.bucket_domain_name
  description = "Name of of website bucket"
}

output "s3_bucket_arn" {
  value       = aws_s3_bucket.default.arn
  description = "Name of of website bucket"
}

output "s3_bucket_website_endpoint" {
  value       = aws_s3_bucket.default.website_endpoint
  description = "The website endpoint URL"
}

output "s3_bucket_website_domain" {
  value       = aws_s3_bucket.default.website_domain
  description = "The domain of the website endpoint"
}

output "s3_bucket_hosted_zone_id" {
  value       = aws_s3_bucket.default.hosted_zone_id
  description = "The Route 53 Hosted Zone ID for this bucket's region"
}

output "bucket_regional_domain_name" {
  value =  aws_s3_bucket.default.bucket_regional_domain_name
  description = "The bucket region-specific domain name.  Used to prevent redirect issues from Cloudfront to S3 origin URL"
}
