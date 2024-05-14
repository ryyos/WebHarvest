import settings
class BIComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.bi.go.id'
        
        self.path_dones = 'src/services/dataDivtic/bi/database/paged_dones.json'
        self.path_err = 'src/services/dataDivtic/bi/database/paged_error.json'
        
        self.gambar_uang_url = 'https://www.bi.go.id/id/rupiah/gambar-uang/Default.aspx'
        self.items_url = 'https://www.bi.go.id/id/statistik/ekonomi-keuangan/items/Default.aspx'
        
        self.cookies = {
            'cookie_BIWEB': '!AIrodvCeXBcrJyHt0q10PaN+sDuIGA8ClilbcqhrmOV3VOUbZYCYVAXVdxLj9PxFrqC/0nbMW2mNKg==',
            'TS014171ca': '0199782b6f819d77e3a6fe681deb4c7798fb678f7e60c9f362f49398e75df0156829284528ee110781df845e8177a769931f566d8a',
            'TS0dddebd2027': '08f7caa0deab2000208942d2ec8e265327ad9b88e2866d1175863eb1d7ef90fe52808b0d5243993108211924241130004544b4f0e91533098896387955e8c1314ed1702d34cb9638de53a7c45c50adb06413338983311c339350204d1c6d3f5f',
            'WSS_FullScreenMode': 'false',
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.google.com/',
            'Connection': 'keep-alive',
            # 'Cookie': 'cookie_BIWEB=!AIrodvCeXBcrJyHt0q10PaN+sDuIGA8ClilbcqhrmOV3VOUbZYCYVAXVdxLj9PxFrqC/0nbMW2mNKg==; TS014171ca=0199782b6f819d77e3a6fe681deb4c7798fb678f7e60c9f362f49398e75df0156829284528ee110781df845e8177a769931f566d8a; TS0dddebd2027=08f7caa0deab2000208942d2ec8e265327ad9b88e2866d1175863eb1d7ef90fe52808b0d5243993108211924241130004544b4f0e91533098896387955e8c1314ed1702d34cb9638de53a7c45c50adb06413338983311c339350204d1c6d3f5f; WSS_FullScreenMode=false',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
        }
        ...