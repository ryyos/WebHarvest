
from typing import Dict, Generator
from ApiRetrys import ApiRetry
from pyquery import PyQuery

from src.server import Beanstalk
from src.utils import Time
from .component import GetDayTrendsComponent

class GetDayTrendsLibs(GetDayTrendsComponent):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()
        
        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        self.beanstalk = Beanstalk(options["beanstalk_host"], options["beanstalk_port"], options["beanstalk_tube"])
        ...
        
    def collect_keyword(self, html: PyQuery) -> Generator[Dict[str, any], None, None]:
        for keyword in html.find('#trends td a'):
            yield {
                "keyword": PyQuery(keyword).text(),
                "cache": True,
                "since": Time.today()
            }
        ...
        