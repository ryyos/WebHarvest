import patoolib
import os
import tempfile
import shutil

from icecream import ic
from typing import List
from rarfile import RarFile

from src.server import S3
from src.utils import Stream, Funct

class Zip:

    @staticmethod
    def unzip_rar(source: str, destination: str, password: str = None) -> str:
        try:
            patoolib.extract_archive(source, outdir=destination, password=password)
        except Exception:
            ...
        finally:
            Stream.zip_stream('UNZIP', source, destination, password)
        return destination
        ...

    @staticmethod
    def unzip_items_rar(source: str, destination: str, password: str = None, s3: bool = False) -> List[str]:
        S3.upload_file(path=source, destination=destination+source.split('.')[-1]+'/'+source.split('/')[-1], send=s3)
        path_items: List[str] = [destination+source.split('.')[-1]+'/'+source.split('/')[-1]]

        temp_dir: str = tempfile.mkdtemp()
        try:
            temp_dir_file: str = patoolib.extract_archive(source, outdir=temp_dir.replace('\\', '/'), password=password)
        except Exception:
            ...
        finally:
            Stream.zip_stream('UNZIP', source, temp_dir_file, password)

        for root, dirs, files in os.walk(temp_dir_file):
            for file in files:
                file_path = os.path.join(root, file).replace('\\', '/')

                _, extension = os.path.splitext(file_path)

                S3.upload_file(path=file_path, destination=destination+extension.replace('.', '')+'/'+file_path.split('/')[-1], send=s3)
                new_path: str = Funct.copy(source=file_path, destination=destination+extension.replace('.', '')+'/'+file_path.split('/')[-1])
                Stream.zip_stream('COPY', file_path, new_path, password)
                path_items.append(new_path.replace('\\', '/'))

        shutil.rmtree(temp_dir.replace('\\', '/'))
        return path_items
