import json
import os
from pathlib import Path
from typing import Any

import requests


class Secrets:
    __FILE_PATH = Path(__file__)
    __SECRETS_FILE_PATH: str = str(__FILE_PATH.parent / 'secrets.json')

    __SECRETS: dict = dict()
    if __SECRETS_FILE_PATH.startswith('http'):
        r = requests.get(__SECRETS_FILE_PATH)
        if r.status_code == 200:
            __SECRETS = json.loads(r.content)
        else:
            raise RuntimeError('Cannot download secrets from the requested url')
    else:
        if __SECRETS_FILE_PATH:
            __SECRETS = json.load(open(__SECRETS_FILE_PATH))

    def __class_getitem__(cls, key: str) -> Any:
        return cls._get_secret(key)

    @staticmethod
    def _get_secret(key: str) -> Any:
        if key not in Secrets.__SECRETS or not Secrets.__SECRETS[key]:
            Secrets.__SECRETS[key] = Secrets._get_secret_from_env(key)
        return Secrets.__SECRETS[key]

    @staticmethod
    def name_of_id(id: int) -> str:
        known_id = Secrets['known_id']
        id = str(id)
        if id in known_id:
            return known_id[id]
        return id

    @staticmethod
    def _get_secret_from_env(key: str) -> str:
        return os.environ[key] if key in os.environ else ''
