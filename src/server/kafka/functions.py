
import json
import settings
import os

from icecream import ic
from dotenv import load_dotenv

from src.utils import Stream, File
from .connection import ConnectionKafka

class Kafkaa:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Kafkaa, cls).__new__(cls)
            cls._connection = ConnectionKafka()
        return cls._instance
    
    @classmethod
    def send(cls, _data_: dict, _topic_: str = None) -> None:
        cls()
        _topic_: str = _topic_ if _topic_ else settings.KAFKA_CONFIGURATIONS.get('topic')
        cls._connection.send(_topic_=_topic_, _value_=str.encode(json.dumps(_data_)))
        Stream.shareKafka(_topic_)

    @classmethod
    def local2kafka(cls, _source_: str) -> None:
        cls()
        for root, _, files in os.walk(_source_.replace('\\', '/')):
            for file in files:
                if file.endswith('json'):
                    file_path = os.path.join(root, file).replace('\\', '/')
                    Stream.shareKafka(file_path)
                    data: dict = File.read_json(file_path)
                    cls._connection.send(data)