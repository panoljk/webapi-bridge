"""Example bot connection using sandbox account data only."""
from demo.client import WebAPIBridgeClient


def main():
    gateway = WebAPIBridgeClient()
    print("Gateway:", gateway.health())
    print("Accounts:", gateway.accounts())
    print("Balance:", gateway.balance(account="paper-main"))
    print("Positions:", gateway.positions(account="paper-main"))


if __name__ == "__main__":
    main()
