import json
from classes.quote_summary import QuoteSummary
from urllib import request, response


class Holders(QuoteSummary):
    def __init__(
        self,
        ticker: str,
        crumb: str = "rbdOZqfFGVY",
        modules: str = "institutionOwnership%2CfundOwnership%2CmajorDirectHolders%2CmajorHoldersBreakdown%2CinsiderTransactions%2CinsiderHolders%2CnetSharePurchaseActivity",
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
        return data['quoteSummary']['result'][0]
