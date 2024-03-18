import os
from dotenv import *
from json import dumps
from icecream import ic

from src.utils import Stream
from .connection import ConnectionS3

connection = ConnectionS3()
class S3:

    @staticmethod
    def upload_json(destination: str, body: dict, send: bool = True) -> int:
        if send: 
            response: dict = connection.s3.put_object(
                Bucket=connection.bucket, 
                Key=destination, 
                Body=dumps(body, indent=2, ensure_ascii=False)
                )
            Stream.s3(destination, response['ResponseMetadata']['HTTPStatusCode'])
            return response['ResponseMetadata']['HTTPStatusCode']
        ...
    @staticmethod
    def upload_file(path: str, destination: str, send: bool = True) -> int:
        if send: 
            response: dict = connection.s3.put_object(
                                Bucket=connection.bucket,
                                Key = destination, 
                                Body = open(path, 'rb')
                            )
            Stream.s3(destination, response['ResponseMetadata']['HTTPStatusCode'])
            return response['ResponseMetadata']['HTTPStatusCode']
        ...
    @staticmethod
    def upload(body: any, destination: str, send: bool = True) -> int:
        if send: 
            response: dict = connection.s3.put_object(
                                Bucket=connection.bucket,
                                Key = destination, 
                                Body = body
                            )
            Stream.s3(destination, response['ResponseMetadata']['HTTPStatusCode'])
            return response['ResponseMetadata']['HTTPStatusCode']
        ...
    @staticmethod
    def local2s3(source: str) -> None:
        for root, dirs, files in os.walk(source.replace('\\', '/')):
            for file in files:
                file_path = os.path.join(root, file).replace('\\', '/')
                
                Stream.share(file_path)

                S3.upload_file(
                    path=file_path,
                    destination=file_path,
                )
