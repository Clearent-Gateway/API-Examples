import argparse
import logging

from clearent_gateway import ClearentGateway

SANDBOX_URL = "https://gateway-sb.clearent.net/rest/v2/transactions"


def demo_sale(api_key: str) -> None:

    gateway = ClearentGateway(SANDBOX_URL, api_key)

    # set up a sale
    transaction = {
        "type": "SALE",
        "amount": "25.00",
        "card": "4111111111111111",
        "exp-date": "1219",
    }
    resp = gateway.post_transaction(transaction)
    print(resp)


def demo_authorization(api_key: str) -> None:

    gateway = ClearentGateway(SANDBOX_URL, api_key)

    # set up an authorization
    transaction = {
        "type": "AUTH",
        "amount": "25.00",
        "card": "4111111111111111",
        "exp-date": "1219",
    }
    resp = gateway.post_transaction(transaction)
    print(resp)


def demo_capture(api_key: str) -> None:

    gateway = ClearentGateway(SANDBOX_URL, api_key)

    # set up a capture
    transaction = {"type": "CAPTURE", "amount": "25.00", "id": "12345"}
    resp = gateway.post_transaction(transaction)
    print(resp)


def demo_forced_sale(api_key: str) -> None:

    gateway = ClearentGateway(SANDBOX_URL, api_key)

    # set up a forced sale
    transaction = {
        "type": "FORCED SALE",
        "amount": "25.00",
        "card": "4111111111111111",
        "exp-date": "1219",
        "order-id": "123456",
        "authorization-code": "APPC10",
    }
    resp = gateway.post_transaction(transaction)
    print(resp)


def demo_refund(api_key: str) -> None:

    gateway = ClearentGateway(SANDBOX_URL, api_key)

    # set up a refund
    transaction = {
        "type": "REFUND",
        "amount": "25.00",
        "card": "4111111111111111",
        "id": "12345",
    }
    resp = gateway.post_transaction(transaction)
    print(resp)


def demo_void(api_key: str) -> None:

    gateway = ClearentGateway(SANDBOX_URL, api_key)

    # set up a void
    transaction = {"type": "SALE", "id": "12345"}
    resp = gateway.post_transaction(transaction)
    print(resp)


if __name__ == "__main__":

    available_demos = {
        "sale": demo_sale,
        "authorization": demo_authorization,
        "capture": demo_capture,
        "forcedsale": demo_forced_sale,
        "refund": demo_refund,
        "void": demo_void,
    }

    parser = argparse.ArgumentParser(description="Clearent payment gateway demo")
    parser.add_argument("demo", choices=available_demos.keys(), help="Demo to run")
    parser.add_argument(
        "-k",
        "--key",
        dest="api_key",
        required=True,
        help="Clearent API key",
    )
    parser.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        help="Enable debug logging",
    )

    args = parser.parse_args()

    logging.basicConfig()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    available_demos[args.demo](args.api_key)
