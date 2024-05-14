
import json
import settings
import os

from time import sleep
from icecream import ic
from dotenv import load_dotenv

from src.utils import Stream, File
from .connection import ConnectionKafka

class Kafkaa:
    _instance = None
    _connection = None

    def __new__(cls, bootstrap: str):
        if cls._instance is None or cls._connection is None:
            cls._instance = super().__new__(cls)
            cls._connection = ConnectionKafka(bootstrap)
        return cls._instance
    
    @classmethod
    def send(cls, data: dict, topic: str, bootstrap: str) -> None:
        cls(bootstrap)
        cls._connection.kafka_produser.send(topic=topic, value=str.encode(json.dumps(data)))
        Stream.shareKafka(topic)

    @staticmethod
    def local2kafka(source: str, topic: str, bootstrap: str) -> None:
        for root, _, files in os.walk(source.replace('\\', '/')):
            for file in files:
                if file.endswith('json'):
                    file_path = os.path.join(root, file).replace('\\', '/')
                    Stream.shareKafka(topic)
                    data: dict = File.read_json(file_path)
                    Kafkaa.send(data, topic, bootstrap)