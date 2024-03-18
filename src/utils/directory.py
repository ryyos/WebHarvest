import os
from dekimashita import Dekimashita
from icecream import ic


class Dir:

    @staticmethod
    def create_dir(paths: str, create: bool = True) -> str:
        try: 
            if create: os.makedirs(paths)
        except Exception as err: ...
        finally: return paths
        ...

    @staticmethod
    def convert_path(path: str) -> str:
        path = path.split('/')
        path[1] = 'data_clean'
        return '/'.join(path)
        ...
