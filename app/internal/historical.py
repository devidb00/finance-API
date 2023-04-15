from urllib import request, response
import json

class Metadata:
    def __init__(
        self,
        ticker: str,
        interval: str,
        range: str,
        region: str = "US",
        lang: str = "en-US",
        tsrc: str = "finance",
        use_y_fida: bool = True,
        include_pre_post: bool = True,
        cors_domain: str = "finance.yahoo.com",
        prefix_path: str = "https://query1.finance.yahoo.com/v8/finance/chart"
    ) -> None:
        self.ticker = ticker
        self.interval = interval
        self.range = range
        self.region = region
        self.lang = lang
        self.tsrc = tsrc
        self.use_y_fida = use_y_fida
        self.include_pre_post = include_pre_post
        self.cors_domain = cors_domain
        self.prefix_path = prefix_path

    def fetch_data(self) -> response:
        url = f"{self.prefix_path}/{self.ticker}?interval={self.interval}&region={self.region}&lang={self.lang}&range={self.range}&.tsrc={self.tsrc}&useYfida={self.use_y_fida}&includePrePost={self.include_pre_post}&corsDomain={self.cors_domain}"
        with request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return data