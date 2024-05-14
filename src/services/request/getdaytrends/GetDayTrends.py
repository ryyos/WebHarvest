import json
from loguru import logger
from time import sleep
from typing import Dict
from icecream import ic
from pyquery import PyQuery
from requests import Response

from src.utils import Time, File
from .dependency import GetDayTrendsLibs

class GetDayTrends(GetDayTrendsLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options)
        ...
        
    def main(self) -> None:
        for url in self.target_urls:
            response: Response = self.api.get(url)
            html: PyQuery = PyQuery(response.text)
            
            for keyword in self.collect_keyword(html):
                logger.info(f'KEYWORD [ {keyword} ]')
                self.beanstalk.put(json.dumps(keyword))
                File.write(self.path_done, f'[ {Time.now()} ] :: KEYWORD [ {keyword["keyword"]} ]')
        ...