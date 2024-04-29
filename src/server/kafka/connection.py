import os
import json
import settings

from icecream import ic
from dotenv import load_dotenv
from kafka import KafkaProducer

class ConnectionKafka:
    def __init__(self) -> KafkaProducer:
        try:
            self.__kafka_configuration: dict = settings.KAFKA_CONFIGURATIONS
            self.kafka_produser = KafkaProducer(bootstrap_servers=[b for b in self.__kafka_configuration.values()])
        except Exception as err:
            ic(err)
            ...
        ...
