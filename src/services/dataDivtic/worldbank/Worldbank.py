import json
import pandas
from requests_html import requests
from requests import Response
from pyquery import PyQuery
from pandas import DataFrame
from time import sleep
from requests import Response
from icecream import ic
from typing import Dict, List
from src.drivers import Page, BrowserContext
from.dependency import WorldbankLibs

class Worldbank(WorldbankLibs):
    def __init__(self, options: Dict[str, any]) -> None:
        super().__init__()
        
        self.__save: bool = options.get('save')
        self.__s3: bool = options.get('s3')
        self.__mode: str = options.get('mode')
        
        
    def collect_table(self, url: str) -> List[Dict[str, any]]:
        page: Page = self.browser.new_page()
        page.goto(url)
        
        html: PyQuery = PyQuery(page.content())
        return self.extract_table(html)
        ...
        
    def ldom(self) -> None:
        csv: DataFrame = pandas.read_csv(self.csv_path)
        csv_json: dict = self.convert_to_json(csv)[-7]
        
        clear_world: dict = self.sorted_world(csv_json)
        clear_table: List[dict] = self.collect_table('https://data.worldbank.org/indicator/CM.MKT.LDOM.NO')
        ic(clear_table)
        ...
        
    def totl(self) -> None:
        ...
        
    def datacatalog(self) -> None:
        ...
        
    def main(self) -> None:
        match self.__mode:
            case "ldom":
                self.ldom()
            case "totl":
                self.totl()
            case "datacatalog":
                self.datacatalog()
        ...