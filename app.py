import os
import os.path
import tempfile
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import boto3

s3 = boto3.resource('s3')
BUCKET_NAME = os.environ['S3_BUCKET']
BIND_ADDRESS = os.environ.get('BIND_ADDRESS', '0.0.0.0')
PORT = int(os.environ.get('PORT', '21'))
FTP_USERNAME = os.environ['FTP_USERNAME']
FTP_PASSWORD = os.environ['FTP_PASSWORD']

def upload_to_s3(filename):
    s3.Object(BUCKET_NAME, os.path.basename(filename)).put(Body=open(filename, 'rb'))

class S3FtpUploadHandler(FTPHandler):
    passive_ports = range(5000, 5010)
    def on_file_received(self, filename):
        upload_to_s3(filename)

def run_server():
    tempdir = tempfile.mkdtemp()
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USERNAME, FTP_PASSWORD, tempdir, perm="elradfmw")
    handler = S3FtpUploadHandler
    handler.authorizer = authorizer
    server = FTPServer((BIND_ADDRESS, PORT), handler)
    server.serve_forever()

if __name__ == '__main__':
    run_server()
