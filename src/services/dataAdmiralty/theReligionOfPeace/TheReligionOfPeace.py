
from icecream import ic
from requests import Response
from pyquery import PyQuery
from typing import List, Dict
from dekimashita import Dekimashita

from .dependency import TheReligionOfPeaceLibs

from src.utils import *
from src.server import Kafkaa

class TheReligionOfPeace(TheReligionOfPeaceLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options)

        ic(options)

        self.all: bool = options.get('all')
        self.__save: bool = options.get('save')
        self.__kafka: bool = options.get('kafka')
        self.__customize: bool = options.get('custom')
        self.__year: str = options.get('year')
        self.__url: str = options.get('url')
        ...

    def extract(self, url: str, year: str, stream: bool) -> None:
        response: Response = self.api.get(url=url, max_retries=30)
        html = PyQuery(response.text)

        tables: List[dict] = self.extract_table(html, stream=stream, customize=self.__customize)

        for table in tables:
            Stream.found(
                process='STREAM',
                message='new date',
                total=table.get('Date')
            )
            results = {
                "link": url,
                "domain": self.domain,
                "tags": [self.domain],
                "topic_kafka": self.topic,
                "crawling_time": Time.now(),
                "crawling_time_epoch": Time.epoch(),
                "title": html.find('h2[class="h3-DarkSlate"]').text().replace('\n', ''),
                "year": self.to_int(year),
                "url_media": [self.base_url+PyQuery(img).attr('src').replace('\\', '/') for img in html.find('table[class="quran-table"] img')],
                "descriptions": self.filter(html),
                "jihad_report": self.extract_jihad(html),
                **table
            }

            if stream:
                path: str = self.path_stream+year
                path: str = f'{Dir.create_dir(path)}/{Time.epoch()}.json'

            elif self.__customize:
                path: str = self.path_custom+year
                path: str = f'{Dir.create_dir(path)}/{str(Time.epoch_ms())}.json'

            else:
                path: str = self.path_all+year
                path: str = f'{Dir.create_dir(path)}/{str(Time.epoch_ms())}.json'



            if self.__save:
                File.write_json(path, results)
            if self.__kafka:
                Kafkaa.send(results)

        Stream.found(
            process='STREAM',
            message='DATA FOUND',
            total=len(tables)
        )
        ...


    def main(self) -> None:

        if self.__customize:
            self.extract(self.__url, self.__year, False)

        else:
            for year, url in self.collect_year(self.main_url):
                self.extract(url=url, year=year, stream=bool(not self.all))

                if not self.all: break
                ...