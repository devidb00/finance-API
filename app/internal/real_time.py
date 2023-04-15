from urllib import request, response
import json


class RealTime:
    def __init__(
        self,
        symbols: str,
        formatted: bool = True,
        crumb: str = "hfAZiODHqYR",
        lang: str = "en-US",
        region: str = "US",
        cors_domain: str = "finance.yahoo.com",
        prefix_path: str = "https://query2.finance.yahoo.com/v7/finance/quote",
        fields: str = "messageBoardId%2ClongName%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2Cuuid%2CregularMarketOpen%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2CtoCurrency%2CfromCurrency%2CtoExchange%2CfromExchange%2CcorporateActions",
    ) -> None:
        self.symbols = symbols
        self.formatted = formatted
        self.crumb = crumb
        self.lang = lang
        self.region = region
        self.fields = fields
        self.cors_domain = cors_domain
        self.prefix_path = prefix_path

    def fetch_data(self) -> response:
        url = f"{self.prefix_path}?symbols={self.symbols}&formatted={self.formatted}&region={self.region}&lang={self.lang}&crumb={self.crumb}&corsDomain={self.cors_domain}&fields={self.fields}"
        with request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return data
