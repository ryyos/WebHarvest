import patoolib
import os
import tempfile
import shutil
import zipfile

from icecream import ic
from typing import List
from rarfile import RarFile

from src.server import S3
from src.utils import Stream, Funct, File

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
        destination_source: str = destination+File.get_format(source)+'/'+File.name_file(source)
        S3.upload_file(path=source, destination=destination_source, send=s3)
        path_items: List[str] = [destination_source]

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

                S3.upload_file(path=file_path, destination=destination+File.get_format(file_path)+'/'+File.name_file(file_path), send=s3)
                new_path: str = Funct.copy(source=file_path, destination=destination+File.get_format(file_path)+'/'+File.name_file(file_path))
                Stream.zip_stream('COPY', file_path, new_path, password)
                path_items.append(new_path.replace('\\', '/'))

        shutil.rmtree(temp_dir.replace('\\', '/'))
        return path_items
    
    @staticmethod
    def unzip_items_zip(source: str, destination: str, password: str = None, s3: bool = False, **kwargs) -> List[str]:
        
        if kwargs.get("send_source"):
            destination_source: str = destination+File.get_format(source)+'/'+File.name_file(source)
            S3.upload_file(path=source, destination=destination_source, send=s3)
            path_items: List[str] = [destination_source]
            
        else:
            path_items: List[str] = []
            
        temp_dir: str = tempfile.mkdtemp()
        
        try:
            with zipfile.ZipFile(source, 'r') as zip_ref:
                zip_ref.extractall(temp_dir.replace('\\', '/'))
                
            ...
        except Exception:
            ...
        finally:
            Stream.zip_stream('UNZIP', source, temp_dir, password)

        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file).replace('\\', '/')

                S3.upload_file(path=file_path, destination=destination+File.get_format(file_path)+'/'+File.name_file(file_path), send=s3)
                new_path: str = Funct.copy(source=file_path, destination=destination+File.get_format(file_path)+'/'+File.name_file(file_path))
                Stream.zip_stream('COPY', file_path, new_path, password)
                path_items.append(new_path.replace('\\', '/'))

        shutil.rmtree(temp_dir.replace('\\', '/'))
        return path_items
        ...