import os
import json
import settings

from dotenv import load_dotenv
from kafka import KafkaProducer

class ConnectionKafka:
    def __init__(self) -> KafkaProducer:
        try:
            self.__kafka_configuration: dict = settings.KAFKA_CONFIGURATIONS

            self.kafka_produser = KafkaProducer(bootstrap_servers=[
                self.__kafka_configuration.get('bootstrap_servers_1'), 
                self.__kafka_configuration.get('bootstrap_servers_2'),
                self.__kafka_configuration.get('bootstrap_servers_3')])
            return self.kafka_produser
        except Exception:
            ...

        ...


   
