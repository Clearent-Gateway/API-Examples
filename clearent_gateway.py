import requests


class GatewayError(Exception):
    pass


class ClearentGateway:

    def __init__(self, base_url: str, api_key: str) -> None:
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cache-Control": "no-cache",
            "api-key": api_key,
        }

    def post_transaction(self, transaction: dict) -> dict:
        resp = requests.post(
            self.base_url, data=transaction, headers=self.headers, timeout=5
        )
        if resp.status_code not in range(200, 300) and resp.status_code not in range(
            400, 500
        ):
            raise GatewayError(f"Error: {resp.status_code} ({resp.content!r})")
        resp_data = resp.json()
        return resp_data

    def get_transaction(self, transaction_id: str) -> dict:
        url = f"{self.base_url}?id={transaction_id}"
        resp = requests.get(url, headers=self.headers, timeout=5)
        if resp.status_code != 200:
            raise GatewayError(f"Error: {resp.status_code} ({resp.content!r})")
        resp_data = resp.json()
        return resp_data[0]
