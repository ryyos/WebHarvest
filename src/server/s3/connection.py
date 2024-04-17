import os
import boto3
import settings

from botocore.config import Config

from dotenv import *
from json import dumps
from icecream import ic
from src.utils import Stream

class ConnectionS3:
    def __init__(self) -> None:
        self.S3_CONFIGURATION = settings.S3_CONFIGURATIONS
        self.BOTO3_CONFIGURATIONS = settings.BOTO3_CONFIGURATIONS

        self.config = Config(retries = self.BOTO3_CONFIGURATIONS)
        self.bucket = self.S3_CONFIGURATION.get('bucket')

        self.s3 = boto3.client(service_name=self.S3_CONFIGURATION.get('service_name'),
                                 aws_access_key_id= self.S3_CONFIGURATION.get('aws_access_key_id'), 
                                 aws_secret_access_key=self.S3_CONFIGURATION.get('aws_secret_access_key'), 
                                 endpoint_url=self.S3_CONFIGURATION.get('endpoint_url'),
                                 config=self.config
                                 )
