
import json
import settings
import os

from icecream import ic
from dotenv import load_dotenv

from src.utils import Stream, File
from .connection import ConnectionKafka

kafka = ConnectionKafka()
connection = kafka.start()

class Kafkaa:

    @staticmethod
    def send(data: dict, topic: str = None) -> None:
        topic: str = topic if topic else settings.KAFKA_CONFIGURATIONS.get('topic')
        connection.send(topic=topic, value=str.encode(json.dumps(data)))
        Stream.shareKafka(topic)

    @staticmethod
    def local2kafka(source: str) -> None:
        for root, _, files in os.walk(source.replace('\\', '/')):
            for file in files:

                if file.endswith('json'):
                    file_path = os.path.join(root, file).replace('\\', '/')
                    
                    Stream.shareKafka(file_path)

                    data: dict = File.read_json(file_path)
                    connection.send(data)