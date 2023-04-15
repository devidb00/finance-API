from pydantic import BaseSettings


class AppSettings(BaseSettings):
    app_title: str = "Yahoo Finance API"
    version: str = "0.0.1"
    contact_info: dict = {
        "name": "Tarik ID BELLOUCH",
        "email": "tarikidb.dev@gmail.com",
    }
