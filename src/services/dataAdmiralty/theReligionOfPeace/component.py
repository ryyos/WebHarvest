import os
import settings
from dotenv import load_dotenv

class TheReligionOfPeaceComponent:
    def __init__(self) -> None:
        load_dotenv()

        self.main_url = 'https://www.thereligionofpeace.com/attacks/attacks.aspx?Yr=Last30'
        self.base_url = 'https://www.thereligionofpeace.com'
        self.base_media_url = 'https://www.thereligionofpeace.com/attacks/'
        self.domain = 'www.thereligionofpeace.com'

        self.topic = os.getenv('TOPIC')

        self.path_all = 'data/kafka/admiralty/theReligionOfPeace/all/json/'
        self.path_stream = 'data/kafka/admiralty/theReligionOfPeace/stream/json/'
        self.path_custom = 'data/kafka/admiralty/theReligionOfPeace/customize/json/'
        ...