import json
from urllib import request, response
from classes.quote_response import QuoteResponse


class RealTime(QuoteResponse):
    def __init__(
        self,
        symbols: str,
        crumb: str = "hfAZiODHqYR",
        fields: str = "messageBoardId%2ClongName%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2Cuuid%2CregularMarketOpen%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2CtoCurrency%2CfromCurrency%2CtoExchange%2CfromExchange%2CcorporateActions",
    ) -> None:
        super().__init__(
            symbols=symbols,
            crumb=crumb,
            fields=fields
        )

    def fetch_data(self) -> response:
        url = f"{self.prefix_path}?symbols={self.symbols}&formatted={self.formatted}&region={self.region}&lang={self.lang}&crumb={self.crumb}&corsDomain={self.cors_domain}&fields={self.fields}"
        with request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return data['quoteResponse']['result'][0]
