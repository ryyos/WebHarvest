from ApiRetrys import ApiRetry
from requests import Response
from pyquery import PyQuery

from typing import Tuple, List, AsyncGenerator, Dict, Any
from icecream import ic
from dekimashita import Dekimashita
from .component import UnodcComponent
from src.utils import Time, Dir, File, Down
from src.server import S3

class UnodcLibs(UnodcComponent):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()

        self.__save: bool = options.get('save')
        self.__s3: bool = options.get('s3')
        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        
        ...

    def build_path(self, provinsi: str) -> str:
        return f'data/data_raw/Divtik/imdi/{provinsi}/json/{Dekimashita.vdir(provinsi)}.json'
        ...

    async def get_title(self, html: PyQuery) -> str:
        html: PyQuery = html.find('#case-law-content div[class="row"]')
        return html.find('span[class="title"]').text()
        ...

    async def get_country(self, html: PyQuery) -> str:
        html: PyQuery = html.find('#case-law-content div.countryNoHighlight')
        return html.find('h3').text()
        ...

    async def get_fact_summary(self, html: PyQuery) -> str:
        html: PyQuery = html.find('#case-law-content div.factSummary')
        if html: return html.text()
        else: return None
        ...
    
    async def get_commentary_significant_features(self, html: PyQuery) -> str:
        html: PyQuery = html.find('#case-law-content div.commentaryAndSignificantFeatures')
        if html: return html.text()
        else: return None
        ...

    async def get_sentence_date(self, html: PyQuery) -> str:
        html: PyQuery = html.find('#case-law-content div.sentencedDate > div.value')
        if html: return html.text()
        else: return None
        ...

    async def get_cross_cutting_issues(self, html: PyQuery) -> Dict[str, any]:
        
        async def __details(html: PyQuery) -> Dict[str, any]:
            childrens: List[PyQuery] = html.children()
            _results: dict = {}
            for child in childrens:
                child: PyQuery = PyQuery(child)
                if child.is_('h4'):
                    _results.update({
                        Dekimashita.vdir(child.text()): list(map(lambda div: PyQuery(div).text(), child.next('div.containerListElement').children()))
                    })
            return _results
            ...

        parent_childrens: List[PyQuery] = html.find('div[class="cross-cutting"]').children()
        _parent_results: dict = {}
        for child in parent_childrens:
            child: PyQuery = PyQuery(child)
            if child.is_('h4'):
                _parent_results.update({
                    Dekimashita.vdir(child.text()): await __details(child.next('div.containerListElement'))
                })
            ...
        
        return _parent_results
        ...

    async def get_procedural_information(self, html: PyQuery) -> Dict[str, any]:
        _parent_results: dict = {}
        async def __field(html: PyQuery) -> Dict[str, any]:
            return {
                Dekimashita.vdir(html.find('div.label').text()): html.find('div.value').text()
            }
            ...

        async def __description(html: PyQuery) -> Dict[str, any]:
            return {
                html.find('div.procedural-history div.proceeding_proceedingDescription h4').text():\
                html.find('div.procedural-history div.proceeding_proceedingDescription div.value').text()
            }
            ...

        _all_field_class: List[PyQuery] = html.find('div.procedural-history div.field')
        for field_class in _all_field_class:
            if not PyQuery(field_class).text(): continue
            _parent_results.update(await __field(PyQuery(field_class)))
        _parent_results.update(await __description(html))

        return _parent_results
        ...

    async def defendants_respondents(self, html: PyQuery) -> List[Dict[str, any]]:
        _parent_results: List[dict] = []
        async def __field(html: PyQuery) -> Dict[str, any]:
            return {
                Dekimashita.vdir(html.find('div.label').text()): html.find('div.value').text()
            }
        
        html: PyQuery = html.find('div.defendantsRespondents')
        for person in html.find('div.person'):
            _field_result: dict = {}
            for field in PyQuery(person).find('div.field'):
                if not PyQuery(field).text(): continue
                _field_result.update(await __field(PyQuery(field)))
                ...
            _parent_results.append(_field_result.copy())
            ...

        return _parent_results
        ...

    async def get_charges_claims_decisions(self, html: PyQuery) -> List[Dict[str, any]]:
        _parent_results: List[dict] = []
        async def __field(html: PyQuery) -> Dict[str, any]:
            return {
                Dekimashita.vdir(html.find('div.label').text()): html.find('div.value').text()
            }
            ...
        
        html: PyQuery = html.find('div.charges')
        for person in html.find('div.person'):
            _field_result: dict = {
                "charges": []
            }

            person: PyQuery = PyQuery(person)
            childrens: List[PyQuery] = person.children()

            for child in childrens:
                _charge_result: dict = {}
                if PyQuery(child).is_('div.charge'):
                    for field in PyQuery(child).find('div.field, div.fieldFullWidth'):
                        if not PyQuery(field).text(): continue
                        _charge_result.update(await __field(PyQuery(field)))
                        ...
                    _field_result['charges'].append(_charge_result.copy())
                    ...

                elif PyQuery(child).is_('div.field, div.fieldFullWidth'):
                    if not PyQuery(child).text(): continue
                    _field_result.update(await __field(PyQuery(child)))
                    ...

            _parent_results.append(_field_result.copy())
            ...

        return _parent_results
        ...

    async def get_court(self, html: PyQuery) -> str:
        return html.find('#case-law-content > div > div').eq(-3).text()
        ...

    async def get_sources_citations(self, html: PyQuery) -> List[str]:
        return list(map(lambda p: PyQuery(p).text(), html.find('div.sources > p')))
        ...

    async def get_attachments(self, html: PyQuery) -> List[str]:
        return list(map(lambda p: self.home_url+PyQuery(p).attr('href'), html.find('div.attachments a')))
        ...

    async def get_path_doc(self, data: Dict[str, any]) -> List[str]:
        return list(map(lambda doc: f'data/data_raw/UNODC/Money laundering/{File.get_format(doc)}/'+File.name_file(doc), data["attachments"]))
        ...

    async def meta_data(self, data: dict) -> str:

        path_json: str = f'data/data_raw/UNODC/Money laundering/json/{Dekimashita.vdir(data["title"])}.json'
        path_document: List[str] = await self.get_path_doc(data)

        data.update({
            "domain": self.domain,
            "tags": [self.domain],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
            "path_data_raw": self.base_path_s3+path_json,
            "path_data_clean": self.base_path_s3+Dir.convert_path(path_json),
            "path_data_documents": [self.base_path_s3+path for path in path_document]
        })

        if self.__save:
            File.write_json(path_json, data)

            for url, path_dest in zip(data["attachments"], path_document):
                response = Down.curl(url, path_dest)
                S3.upload(
                    body=response.content,
                    destination=path_dest,
                    send=self.__s3
                )

        S3.upload_json(
            destination=path_json,
            body=data,
            send=self.__s3
        )
        ...

    async def extract(self, url: str) -> List[Dict[str, any]]:
        response: Response = self.api.get(url)
        html: PyQuery = PyQuery(response.text)

        result = {
            "url": url,
            "title": await self.get_title(html),
            "country": await self.get_country(html),
            "fact_summary": await self.get_fact_summary(html),
            "commentary_and_significant_features": await self.get_commentary_significant_features(html),
            "sentence_date": await self.get_sentence_date(html),
            "cross_cutting_issues": await self.get_cross_cutting_issues(html),
            "procedural_information": await self.get_procedural_information(html),
            "defendants_respondents_in_the_first_instance": await self.defendants_respondents(html),
            "charges_claims_decisions": await self.get_charges_claims_decisions(html),
            "court": await self.get_court(html),
            "sources_citations": await self.get_sources_citations(html),
            "attachments": await self.get_attachments(html)
        }

        await self.meta_data(result)
        ...