import requests

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
    ) -> dict:
        PATH_PREFIX = "https://query1.finance.yahoo.com/v8/finance/chart"
        return requests.get(
            f"""
                {PATH_PREFIX}
                    /{ticker}
                    ?interval={interval}
                    &region={region}
                    &lang={lang}
                    &range={range}
                    &.tsrc={tsrc}
                    &useYfida={use_y_fida}
                    &includePrePost={include_pre_post}
                    &corsDomain={cors_domain}
            """
        )

    def to_json(self) -> dict:
        return self.json