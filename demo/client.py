"""Minimal Python client for the local read-only API sandbox."""
import json
from urllib.parse import urlencode
from urllib.request import urlopen

class WebAPIBridgeClient:
    def __init__(self, base_url="http://127.0.0.1:8787"):
        self.base_url = base_url.rstrip("/")

    def get(self, path, **params):
        url = self.base_url + path
        if params:
            url += "?" + urlencode(params)
        with urlopen(url, timeout=5) as response:
            return json.load(response)

    def health(self):
        return self.get("/v1/health")

    def accounts(self):
        return self.get("/v1/accounts")

    def balance(self, account="paper-main"):
        return self.get("/v1/balances", account=account)

    def positions(self, account="paper-main"):
        return self.get("/v1/positions", account=account)
