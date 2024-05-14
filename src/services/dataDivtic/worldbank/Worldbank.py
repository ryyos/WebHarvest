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
from.dependency import WorldbankLibs
from src.drivers import Page, BrowserContext
from src.utils import Time, Dir, Endecode, File, Zip
from src.server import S3
class Worldbank(WorldbankLibs):
    def __init__(self, options: Dict[str, any]) -> None:
        super().__init__(options)
        
        self.__save: bool = options.get('save')
        self.__s3: bool = options.get('s3')
        self.__mode: str = options.get('mode')
        
    def head(self, **kwargs) -> Dict[str, any]:
        return {
            "link": kwargs.get('url'),
            "domain": self.domain,
            "tags": [self.domain],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
            "path_data_raw": self.base_path_s3+kwargs.get('path'),
            "path_data_clean": self.base_path_s3+Dir.convert_path(kwargs.get('path')),
        }
        ...
        
    def collect_table(self, url: str) -> List[Dict[str, any]]:
        browser: BrowserContext = self.browser.start()
        browser.set_default_timeout(120000)
        page: Page = browser.new_page()
        page.goto(url)
        
        html: PyQuery = PyQuery(page.content())
        self.browser.close()
        return self.extract_table(html)
        ...
        
    def ldom(self) -> None:
        
        url = 'https://data.worldbank.org/indicator/CM.MKT.LDOM.NO'
        path = 'data/data_raw/worldbank/domestic_companies/json/{}.json'.format(Endecode.md5_hash(url))
        
        csv: DataFrame = pandas.read_csv(self.csv_path)
        csv_json: dict = self.convert_to_json(csv)[-7]
        
        clear_chart: dict = self.sorted_world(csv_json)
        clear_table: List[dict] = self.collect_table(url)
        
        head: dict = self.head(
            url=url,
            path=path
            
        )
        
        result: dict = {
            **head,
            "chart": clear_chart,
            "table": clear_table
        }
        
        if self.__save:
            File.write_json(path, result)
            
        S3.upload_json(
            destination=path,
            body=result,
            send=self.__s3
        )
        ...
        
    def totl(self) -> None:
        url = 'https://data.worldbank.org/indicator/FI.RES.TOTL.CD'
        path = 'data/data_raw/worldbank/reserves_including_gold/json/{}.json'.format(Endecode.md5_hash(url))
        
        clear_table: List[dict] = self.collect_table(url)
        
        head: dict = self.head(
            url=url,
            path=path
            
        )
        
        result: dict = {
            **head,
            "table": clear_table
        }
        
        if self.__save:
            File.write_json(path, result)
            
        S3.upload_json(
            destination=path,
            body=result,
            send=self.__s3
        )
        
        ...
        
    def datacatalog(self) -> None:
        url = 'https://datacatalogapi.worldbank.org/ddhxext/ResourceListing?dataset_unique_id=0064716&resource_unique_id=DR0092077'
        api = 'https://datacatalogfiles.worldbank.org/ddh-published/0064716/DR0092077'
        base_path = 'data/data_raw/worldbank/sophistication_of_exports/'
        
        response: Response = self.api.get(url)
        path_documents: List[str] = []
        for file in response.json():
            
            name_file: str = File.name_file(file)
            
            response: Response = self.api.get(api+file)
            
            if self.__save or self.__s3:
                File.write_byte(base_path+'zip/{}'.format(name_file), response)
            
            path_csv: List[str] = Zip.unzip_items_zip(
                source=base_path+'zip/{}'.format(name_file),
                destination=base_path,
                s3=self.__s3
            )
            
            path_documents.extend(path_csv)
            ...
            
        head: dict = self.head(
            url=url,
            path=base_path+'json/{}.json'.format(Endecode.md5_hash(url)),
        )
        
        result: dict = {
            **head,
            "path_documents": list(map(lambda path: self.base_path_s3+path, path_documents))
        }
        
        if self.__save:
            File.write_json(base_path+'json/{}.json'.format(Endecode.md5_hash(url)), result)
            
        S3.upload_json(
            destination=base_path+'json/{}.json'.format(Endecode.md5_hash(url)),
            body=result,
            send=self.__s3
        )
        ...
        
    def main(self) -> None:
        match self.__mode:
            case "ldom":
                self.ldom()
            case "totl":
                self.totl()
            case "datacatalog":
                self.datacatalog()
            case "all":
                self.ldom()
                self.totl()
                self.datacatalog()
                
        ...
