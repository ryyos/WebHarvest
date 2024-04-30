
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

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._connection = ConnectionKafka()
        return cls._instance
    
    @classmethod
    def send(cls, _data_: dict, _topic_: str = None) -> None:
        cls()
        _topic_: str = _topic_ if _topic_ else settings.KAFKA_CONFIGURATIONS.get('topic')
        cls._connection.kafka_produser.send(topic=_topic_, value=str.encode(json.dumps(_data_)))
        Stream.shareKafka(_topic_)

    @staticmethod
    def local2kafka(_source_: str, _topic_: str = None) -> None:
        for root, _, files in os.walk(_source_.replace('\\', '/')):
            for file in files:
                if file.endswith('json'):
                    file_path = os.path.join(root, file).replace('\\', '/')
                    Stream.shareKafka(_topic_)
                    data: dict = File.read_json(file_path)
                    Kafkaa.send(data, _topic_)