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

  * BIND_ADDRESS (default is 0.0.0.0)
  * PORT (default is 21)

# Running

Start app.py with the environment variables set.  Make sure that your IAM user has permissions to write to the bucket.

You will need to forward some ports.  Obviously, port 21, but if you want passive mode to work, you'll need to forward ports 5000 to 5010.  These are hardcoded for now, but feel free to send a pull request to add a configuration variable for them if it matters for your use case.


```bash
docker run -d -e S3_BUCKET=testbucket -e AWS_ACCESS_KEY_ID=AKIAJASDIFJAISD -e AWS_SECRET_ACCESS_KEY=AIDADISAIOHAOIDD -e FTP_USERNAME=hello -e FTP_PASSWORD=world -p 21:21 -p 5000-5100:5000-5100 realgeeks/pys3ftpd
```
