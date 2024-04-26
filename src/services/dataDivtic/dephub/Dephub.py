
from pyquery import PyQuery
from requests import Response
from typing import List, Dict
from .dependency import DephubLibs

class Dephub(DephubLibs):
    def __init__(self) -> None:
        super().__init__()
        ...
        
    def mapping(self, data: Dict[str, any]) -> Dict[str, any]:
        response: Response = self.api.get(self.row_url+data["IDpel"])
        html: PyQuery = PyQuery(response.text)
        
        
        ...
        
    def main(self) -> None:
        list_table: List[dict] = self.get_list_table(self.target_url)
        for row in list_table:
            
            ...
        ...