class QuoteSummary:
    def __init__(
        self,
        crumb: str,
        ticker: str,
        modules: str,
        region: str = "US",
        lang: str = "en-US",
        formatted: bool = True,
        cors_domain: str = "finance.yahoo.com",
        prefix_path: str = "https://query2.finance.yahoo.com/v10/finance/quoteSummary"
    ) -> None:
        self.ticker = ticker
        self.formatted = formatted
        self.crumb = crumb
        self.lang = lang
        self.region = region
        self.modules = modules
        self.cors_domain = cors_domain
        self.prefix_path = prefix_path
