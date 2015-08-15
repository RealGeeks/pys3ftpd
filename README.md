# pys3ftpd

A FTP server that just uploads to S3.  Really only supports uploads.

# Configuration

All configuration is through environment variables.  Set the following variables:

  * AWS_ACCESS_KEY_ID
  * AWS_SECRET_ACCESS_KEY
  * S3_BUCKET
  * FTP_USERNAME
  * FTP_PASSWORD

Optional variables:

  * BIND_ADDRESS (default is 127.0.0.1)
  * PORT (default is 21)

# Running

Start app.py with the environment variables set.  Make sure that your IAM user has permissions to write to the bucket.
