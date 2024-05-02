import os
import settings
from src.utils import Time

class TheReligionOfPeaceComponent:
    def __init__(self) -> None:

        # self.main_url = 'https://www.thereligionofpeace.com/attacks/attacks.aspx?Yr=Last30'
        self.main_url = 'https://www.thereligionofpeace.com/attacks/attacks.aspx?Yr=2024'
        self.base_url = 'https://www.thereligionofpeace.com'
        self.base_media_url = 'https://www.thereligionofpeace.com/attacks/'
        self.domain = 'www.thereligionofpeace.com'


        self.path_all = 'data/kafka/admiralty/theReligionOfPeace/all/json/'
        self.path_stream = 'data/kafka/admiralty/theReligionOfPeace/stream/json/'
        self.path_custom = 'data/kafka/admiralty/theReligionOfPeace/customize/json/'
        self.path_log = f'logs/theReligionOfPeace/theReligionOfPeace.log'
        ...