import os
from dotenv import *
from json import dumps
from icecream import ic

from src.utils import Stream
from .connection import ConnectionS3

class S3:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._connection = ConnectionS3()
            return cls._instance

    @classmethod
    def upload_json(cls, destination: str, body: dict, send: bool = True) -> int:
        cls()
        if send: 
            response: dict = cls._connection.s3.put_object(
                Bucket=cls._connection.bucket, 
                Key=destination, 
                Body=dumps(body, indent=2, ensure_ascii=False)
                )
            Stream.s3(destination, response['ResponseMetadata']['HTTPStatusCode'])
            return response['ResponseMetadata']['HTTPStatusCode']
        ...
    @classmethod
    def upload_file(cls, path: str, destination: str, send: bool = True) -> int:
        cls()
        if send: 
            response: dict = cls._connection.s3.put_object(
                                Bucket=cls._connection.bucket,
                                Key = destination, 
                                Body = open(path, 'rb')
                            )
            Stream.s3(destination, response['ResponseMetadata']['HTTPStatusCode'])
            return response['ResponseMetadata']['HTTPStatusCode']
        ...
    @classmethod
    def upload(cls, body: any, destination: str, send: bool = True) -> int:
        cls()
        if send: 
            response: dict = cls._connection.s3.put_object(
                                Bucket=cls._connection.bucket,
                                Key = destination, 
                                Body = body
                            )
            Stream.s3(destination, response['ResponseMetadata']['HTTPStatusCode'])
            return response['ResponseMetadata']['HTTPStatusCode']
        ...
    @classmethod
    def local2s3(cls, source: str) -> None:
        for root, dirs, files in os.walk(source.replace('\\', '/')):
            for file in files:
                file_path = os.path.join(root, file).replace('\\', '/')
                
                Stream.share(file_path)

                S3.upload_file(
                    path=file_path,
                    destination=file_path,
                )
