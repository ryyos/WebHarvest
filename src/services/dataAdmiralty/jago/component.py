import settings

class JagoComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.jago.com'
        self.profile_url = 'https://www.jago.com/id/company-info/ajax/profile/boc/'
        self.target_url = 'https://www.jago.com/id/company-info'
        self.domain = 'www.jago.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/jago/json/'
        self.cookies = {
            'holding': 'eyJpdiI6Ik9haFU0OFdPamVCUDNPd1Fpd1U5cnc9PSIsInZhbHVlIjoicnhmYkNPRXFvRGFOU3hNVFVDSlQ2clpOaDN0ek9EbW9lS2tMUnpJYUtJT2FHang2UjRNNXAzNXozdWlxZ3cyZFFrelMzNmltZ3pDQkw5OUdud3hDdEE9PSIsIm1hYyI6IjkyOGM5NWI0NDU2ZjZkYmE3MTA3ZGJlMjk2MTdjYzJjZTcxMjQ5ZGUwYTZkMmE0OTUwYjM0MDQwNmY4NDA1MDkiLCJ0YWciOiIifQ%3D%3D',
            'XSRF-TOKEN': 'eyJpdiI6ImpNdGNGR2ZwUUI4bWk1MVFLczdoQ1E9PSIsInZhbHVlIjoiSzhqWXdNMmtMWTh5dVdRbndxdUxSNW5PRHl4NVNJTWFEaTBZbnpiV20yMVZzTFJudjNhN0N5M0Y4NTVQbFh6VjVISFJRa20vczVycFFqSHAxVXdPOVlhT2VYSlJSbktpRjNlYnFQbGtrcDhFNDdmaVUzRU5tdWtkUWkrbERDL1QiLCJtYWMiOiJmOTZmOTI0NWY5YzBlNGE4YWMyMjA0ZmFjN2E5ODMzYWJmMzJiNWIyMDdhOThkNWJkNTU5OWM4MWRkYjVjNzkyIiwidGFnIjoiIn0%3D',
            'bank_jago_session': 'eyJpdiI6IlpmNExFVm43NWN0dnRDR3FRRzZVcHc9PSIsInZhbHVlIjoiSEVYdnRuOFAraEtZTUZuekpLY25ZV09Fc3VFejVoNGZtbDZaR1YxQnEzRFVXY0s2VkZkYjdKNUlnZ0x6Zzl2R3JqMjQ4UzZPY2hKZENNcjlUSHVMTSt6R1ZGZ2ltb3RlQ1pPL2NZRVJiWU9kMmZ0eVcyQ0x6dWR6YmRnQlQvdisiLCJtYWMiOiIwMjUxNzJkNDE0NjY3OGJjMmE3MDFjYTdlZjhmNWZjYWMyNzQ4MGE1N2FlZjZiYWI3NDQ4NTc3NTBiNzcwMDk5IiwidGFnIjoiIn0%3D',
            '__cf_bm': '9CHGsJt2NH8NEVLAugOGdQbDDzt4LFghDMBoEQzh7.4-1714968867-1.0.1.1-EVBoPwf11LhfnPi34YfbT6udTS2RV7_L0WXXpSnpqLueEGBW_BYKJnh9E7rxM3rCYrk2r1AV5ZQjlgPFrCqnzg',
            '_cfuvid': 's2ZSOqlMy9A4Vdviw9psNxUW0SpnyoC3lvY56WSizlw-1714968867535-0.0.1.1-604800000',
        }
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            # 'Cookie': 'holding=eyJpdiI6Ik9haFU0OFdPamVCUDNPd1Fpd1U5cnc9PSIsInZhbHVlIjoicnhmYkNPRXFvRGFOU3hNVFVDSlQ2clpOaDN0ek9EbW9lS2tMUnpJYUtJT2FHang2UjRNNXAzNXozdWlxZ3cyZFFrelMzNmltZ3pDQkw5OUdud3hDdEE9PSIsIm1hYyI6IjkyOGM5NWI0NDU2ZjZkYmE3MTA3ZGJlMjk2MTdjYzJjZTcxMjQ5ZGUwYTZkMmE0OTUwYjM0MDQwNmY4NDA1MDkiLCJ0YWciOiIifQ%3D%3D; XSRF-TOKEN=eyJpdiI6ImpNdGNGR2ZwUUI4bWk1MVFLczdoQ1E9PSIsInZhbHVlIjoiSzhqWXdNMmtMWTh5dVdRbndxdUxSNW5PRHl4NVNJTWFEaTBZbnpiV20yMVZzTFJudjNhN0N5M0Y4NTVQbFh6VjVISFJRa20vczVycFFqSHAxVXdPOVlhT2VYSlJSbktpRjNlYnFQbGtrcDhFNDdmaVUzRU5tdWtkUWkrbERDL1QiLCJtYWMiOiJmOTZmOTI0NWY5YzBlNGE4YWMyMjA0ZmFjN2E5ODMzYWJmMzJiNWIyMDdhOThkNWJkNTU5OWM4MWRkYjVjNzkyIiwidGFnIjoiIn0%3D; bank_jago_session=eyJpdiI6IlpmNExFVm43NWN0dnRDR3FRRzZVcHc9PSIsInZhbHVlIjoiSEVYdnRuOFAraEtZTUZuekpLY25ZV09Fc3VFejVoNGZtbDZaR1YxQnEzRFVXY0s2VkZkYjdKNUlnZ0x6Zzl2R3JqMjQ4UzZPY2hKZENNcjlUSHVMTSt6R1ZGZ2ltb3RlQ1pPL2NZRVJiWU9kMmZ0eVcyQ0x6dWR6YmRnQlQvdisiLCJtYWMiOiIwMjUxNzJkNDE0NjY3OGJjMmE3MDFjYTdlZjhmNWZjYWMyNzQ4MGE1N2FlZjZiYWI3NDQ4NTc3NTBiNzcwMDk5IiwidGFnIjoiIn0%3D; __cf_bm=9CHGsJt2NH8NEVLAugOGdQbDDzt4LFghDMBoEQzh7.4-1714968867-1.0.1.1-EVBoPwf11LhfnPi34YfbT6udTS2RV7_L0WXXpSnpqLueEGBW_BYKJnh9E7rxM3rCYrk2r1AV5ZQjlgPFrCqnzg; _cfuvid=s2ZSOqlMy9A4Vdviw9psNxUW0SpnyoC3lvY56WSizlw-1714968867535-0.0.1.1-604800000',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }
        ...