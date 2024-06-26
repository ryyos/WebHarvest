import json
import os

from typing import List
from .directory import Dir


class File:

    @staticmethod
    def write_json(path: str, content: any) -> None:
        try:
            Dir.create_dir(Dir.basedir(path))
            with open(path, 'w', encoding= "utf-8") as file:
                json.dump(content, file, ensure_ascii=False, indent=2, default=str)

        except Exception as err:
            Dir.create_dir(Dir.basedir(path))
            with open(path, 'w') as file:
                json.dump(content, file, indent=2, default=str)
        ...

    @staticmethod
    def write_str(path: str, content: any) -> None:
        Dir.create_dir(Dir.basedir(path))
        with open(path, 'w', encoding="utf-8") as file:
            file.writelines(content)
        ...

    @staticmethod
    def write(path: str, content: any) -> None:
        Dir.create_dir(Dir.basedir(path))
        with open(path, 'a', encoding="utf-8") as file:
            file.write(content+'\n')
        ...

    @staticmethod
    def write_byte(path: str, media: any) -> None:
        Dir.create_dir(Dir.basedir(path))
        with open(path, 'wb') as file:
            file.write(media)
        ...

    @staticmethod
    def read_json(path: str) -> any:
        Dir.create_dir(Dir.basedir(path))
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
        ...
        
    @staticmethod
    def read(path: str) -> any:
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            
        return html_content
    def read_byte(path: str) -> any:
        with open(path, "rb") as file:
            download_bytes = file.read()
            
        return download_bytes

    @staticmethod
    def read_list_json(path: str):
        Dir.create_dir(Dir.basedir(path))
        if not os.path.exists(path): File.write_json(path, [])
        with open(path) as f:
            data = f.read()
            if not data: data = '[]'
        return json.loads(data)
        ...
    
    @staticmethod
    def list_dir(path: str) -> List[str]:
        return os.listdir(path)
        ...

    @staticmethod
    def get_format(path: str) -> str:
        _, extension = os.path.splitext(path)
        return extension.replace('.', '')
        ...

    @staticmethod
    def name_file(path: str) -> str:
        return os.path.basename(path)
        ...
        

