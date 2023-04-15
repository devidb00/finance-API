from urllib import request, response
import json


class Profile:
    def __init__(
        self,
        ticker: str,
        formatted: bool = True,
        crumb: str = "rbdOZqfFGVY",
        lang: str = "en-US",
        region: str = "US",
        cors_domain: str = "finance.yahoo.com",
        prefix_path: str = "https://query2.finance.yahoo.com/v10/finance/quoteSummary",
        modules: str = "assetProfile%2CsecFilings",
    ) -> None:
        self.ticker = ticker
        self.formatted = formatted
        self.crumb = crumb
        self.lang = lang
        self.region = region
        self.modules = modules
        self.cors_domain = cors_domain
        self.prefix_path = prefix_path

    def fetch_data(self) -> response:
        url = f"{self.prefix_path}/{self.ticker}?formatted={self.formatted}&region={self.region}&lang={self.lang}&crumb={self.crumb}&corsDomain={self.cors_domain}&modules={self.modules}"
        with request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return data['quoteSummary']['result'][0]['assetProfile']
