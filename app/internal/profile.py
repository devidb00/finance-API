import json
from urllib import request, response
from classes.quote_summary import QuoteSummary


class Profile(QuoteSummary):
    def __init__(
        self,
        ticker: str,
        crumb: str = "rbdOZqfFGVY",
        modules: str = "assetProfile%2CsecFilings",
    ) -> None:
        super().__init__(
            ticker=ticker,
            crumb=crumb,
            modules=modules
        )

    def fetch_data(self) -> response:
        url = f"{self.prefix_path}/{self.ticker}?formatted={self.formatted}&region={self.region}&lang={self.lang}&crumb={self.crumb}&corsDomain={self.cors_domain}&modules={self.modules}"
        with request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return data['quoteSummary']['result'][0]['assetProfile']
