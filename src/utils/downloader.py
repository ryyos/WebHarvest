import requests
import mimetypes
import tempfile
import shutil

from icecream import ic
from requests import Response
from loguru import logger

from src.server import S3
from .directory import Dir
from .fileIO import File
from playwright.sync_api import Page, ElementHandle
class Down:

    @staticmethod
    def curl(url: str, path: str, headers: dict = None, cookies: dict = None, extension: str = None) -> Response:
        Dir.create_dir(paths='/'.join(path.split('/')[:-1]))
        response = requests.get(url=url, headers=headers, cookies=cookies)
        with open(path, 'wb') as f:
            f.write(response.content)

        return response
    
    @staticmethod
    def curlv2(path: str, response: Response, extension: str = None) -> Response:
        Dir.create_dir(paths='/'.join(path.split('/')[:-1]))
        with open(path, 'wb') as f:
            f.write(response.content)
            
    @staticmethod
    def playwright(page: Page, loc: ElementHandle, base_desctination: str, s3: bool, save: bool) -> str:
        with page.expect_download() as download_info:
            loc.click()
            download = download_info.value
        
        temp_dir: str = tempfile.mkdtemp().replace('\\', '/')
        filename: str = download.suggested_filename
        temp_path = temp_dir+'/'+filename
        
        logger.info(f'DOWNLOAD FILE [ {filename} ]')
        download.save_as(temp_path)
        
        extention: str = filename.split('.')[-1]
        destination_path: str = base_desctination + extention + '/' + filename
        S3.upload(
            body=File.read_byte(temp_path),
            destination=destination_path,
            send=s3
        )
        if save:
            File.write_byte(
                path=destination_path,
                media=File.read_byte(temp_path),
            )
        shutil.rmtree(temp_dir)
        return destination_path

    # def _upload(body: any, destination: str) -> int:
    #     try:
    #         filepath: str = f"{self.BUCKET}/{destination}"
    #         filename: str = Funct.name_file(filepath)
    #         with self.s3.open(filepath, "wb") as f:
    #             for chunk in body:
    #                 if chunk:
    #                     f.write(chunk)
    #         logger.info(f"File {filename} uploaded to S3 successfully.")
    #         return filepath
    #     except Exception as e:
    #         logger.error("Error uploading file to S3:", e)
    #         return ""

    # def _download(url: str, path: str) -> None:
    #     start = perf_counter()
    #     filename: str = Funct.name_file(path)
    #     logger.info(f"PROCESS DOWNLOAD [ {Funct.name_file(path)} ] :: START [ {Time.now()} ]")
    #     chunks = list()
    #     downloaded = 0
        
    #     for index in range(15):
    #         try:
    #             header = {'Range': f'bytes={downloaded}-'}
    #             headers.update(header)
    #             with requests.get(url, headers=headers, stream=True, timeout=600) as r:
    #                 total_size = downloaded + int(r.headers.get('Content-Length', 0))
    #                 r.raise_for_status()
    #                 file_path = path.replace(self.base_path_s3, "")
    #                 with tqdm(total=total_size, unit='B', unit_scale=True, desc='DOWNLOAD', ncols=100, initial=downloaded) as pbar:
    #                     for chunk in r.iter_content(chunk_size=262144):
    #                         if chunk and chunk not in chunks:
    #                             chunks.append(chunk)
    #                             downloaded += len(chunk)
    #                             pbar.update(len(chunk))
    #                 _upload(chunks, file_path)
    #                 break
    #         except Exception as err:
    #             if index+1 == 15: raise Exception(err)
    #             logger.error(f'MESSAGE [ {err} ] TRY AGAIN [ {index} ]')
    #     logger.info(f"DOWNLOAD [ {filename} ] :: TIME REQUIRED [ {'{:.2f}'.format(perf_counter() - start)} ]")

    
