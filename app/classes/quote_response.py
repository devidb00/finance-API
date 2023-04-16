class QuoteResponse:
    def __init__(
        self,
        crumb: str,
        fields: str,
        symbols: str,
        region: str = "US",
        lang: str = "en-US",
        formatted: bool = True,
        cors_domain: str = "finance.yahoo.com",
        prefix_path: str = "https://query2.finance.yahoo.com/v7/finance/quote",

    ) -> None:
        self.symbols = symbols
        self.formatted = formatted
        self.crumb = crumb
        self.lang = lang
        self.region = region
        self.fields = fields
        self.cors_domain = cors_domain
        self.prefix_path = prefix_path
