import os
import json
import settings

from icecream import ic
from dotenv import load_dotenv
from kafka import KafkaProducer

class ConnectionKafka:
    def __init__(self, bootstrap: str) -> KafkaProducer:
        try:
            self.__bootstrap_servers: dict = settings.BOOTSTRAP_SERVERS
            self.kafka_produser = KafkaProducer(bootstrap_servers=self.__bootstrap_servers[bootstrap])
        except Exception as err:
            ic(err)
            ...
        ...
