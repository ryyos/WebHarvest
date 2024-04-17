import json
import pandas

from ApiRetrys import ApiRetry
from pyquery import PyQuery
from pandas import DataFrame
from json import dumps, loads
from time import sleep
from requests import Response
from icecream import ic
from typing import Dict, List

from src.drivers import SyncPlaywright, BrowserContext
from .components import WorldbankComponent

class WorldbankLibs(WorldbankComponent):
    def __init__(self) -> None:
        super().__init__()
        
        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        self.browser = SyncPlaywright(headless=False).start()
        
    def convert_to_json(self, csv: DataFrame) -> Dict[str, any]:
        result_json: list = loads(csv.to_json(orient="records"))
        return result_json
        ...
        
    def sorted_world(self, data: Dict[str, any]) -> Dict[str, any]:
        new_dict: dict = {}
        for key, value in data.items():
            try:
                str_key: str = str(key)
                new_key: int = int(str_key)            
                if value is None:
                    new_dict[new_key] = None
                else:
                    try:
                        new_value: int = int(value)
                        new_dict[new_key] = new_value
                    except ValueError:
                        pass
            except ValueError:
                pass
        return new_dict
        ...
        
    def extract_table(self, html: PyQuery) -> List[Dict[str, any]]:
        tables: List[PyQuery] = html.find('div[class="infinite"] div[class="item"]')
        ic(len(tables))
        results: List[dict] = []
        
        for row in tables:
            row: PyQuery = PyQuery(row)
            results.append({
                "country": row.find('a').text(),
                "most_recent_year": row.find('div').eq(1).text(),
                "most_recent_value": row.find('div').eq(2).text(),
            })
            
        return results
        ...