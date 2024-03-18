import requests
from icecream import ic
from requests import Response

from src.utils import Dir
class Down:

    @staticmethod
    def curl(url: str, path: str, headers: dict = None, cookies: dict = None) -> Response:
        response = requests.get(url=url, headers=headers, cookies=cookies)
        with open(path, 'wb') as f:
            f.write(response.content)

        return response
    
    @staticmethod
    def curlv2(path: str, response: Response) -> Response:
        Dir.create_dir(paths='/'.join(path.split('/')[:-1]))
        with open(path, 'wb') as f:
            f.write(response.content)

    
