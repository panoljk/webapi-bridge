# Exchange integrations & connection modes

**24 integration targets. One local API. Two possible connection methods.**

WebAPI Bridge is designed to let users select a connection method **per exchange account**, rather than assigning every exchange to a permanently fixed "API" or "Web" group.

## How the connection picker works (planned interface)

1. Select an exchange (for example, MEXC, Bybit or KCEX).
2. Enter an account alias, such as `mexc_main`.
3. Choose `Official API` or `Web Session` **only if available and permitted for that venue**.
4. Supply the appropriate credentials locally; the licensing service never needs exchange keys.
5. Connect the trading bot to the same local Gateway endpoint irrespective of the route.

| Mode | Intended authentication | Status rules |
|---|---|---|
| **Official API** | Exchange-issued API key/secret, and passphrase if required | Offered only where the exchange publishes or grants a trading API |
| **Web Session** | Authorized customer-owned website session | Offered only after security, venue-policy and legal review |
| **Hybrid** (future) | Selected data routes and one explicit trading route | Must never blindly retry a possibly executed order via another route |

### Product interface concept

```text
Add Exchange Connection

Exchange         [ MEXC                    v ]
Account name     [ main                      ]

Connection type
(*) Official API      ( ) Web Session

[ Connect exchange ]
```

`Official API` is the preferred default where it supports the operation. An unavailable mode must appear **disabled with the reason**, never as a working option.

## Exchange selection — interface preview

The table below presents the **connection methods that the product interface is intended to represent**, not a production-support matrix.

| Exchange | Official API | Web Session |
|---|---|---|
| Binance | 🔑 API Key | 🌐 Web Session |
| Bybit | 🔑 API Key | 🌐 Web Session |
| OKX | 🔑 API Key | 🌐 Web Session |
| Bitget | 🔑 API Key | 🌐 Web Session |
| Gate.io | 🔑 API Key | 🌐 Web Session |
| KuCoin | 🔑 API Key | 🌐 Web Session |
| MEXC | 🔑 API Key | 🌐 Web Session |
| BingX | 🔑 API Key | 🌐 Web Session |
| Phemex | 🔑 API Key | 🌐 Web Session |
| WEEX | 🔑 API Key | 🌐 Web Session |
| Bitunix | 🔑 API Key | 🌐 Web Session |
| Toobit | 🔑 API Key | 🌐 Web Session |
| BloFin | 🔑 API Key | 🌐 Web Session |
| CoinEx | 🔑 API Key | 🌐 Web Session |
| XT.COM | 🔑 API Key | 🌐 Web Session |
| WhiteBIT | 🔑 API Key | 🌐 Web Session |
| CoinW | 🔑 API Key | 🌐 Web Session |
| OrangeX | 🔑 API Key | 🌐 Web Session |
| Tapbit | 🔑 API Key | 🌐 Web Session |
| Zoomex | 🔑 API Key | 🌐 Web Session |
| Pionex | 🔑 API Key | 🌐 Web Session |
| BTCC | 🔑 API Key | 🌐 Web Session |
| KCEX | — | 🌐 Web Session |
| AlphaX | — | 🌐 Web Session |

This is a conceptual list. **The included repository demo does not implement live exchange connections.** The UI must only enable methods confirmed to be available, lawful and permitted by the applicable exchange. For KCEX a publicly offered trading API is not confirmed, while AlphaX's official API status is unclear.

### Proposed connection configuration (illustrative, **not implemented**)

```json
{
  "account_alias": "mexc_main",
  "exchange": "mexc",
  "connection_mode": "official_api"
}
```

```json
{
  "account_alias": "mexc_session",
  "exchange": "mexc",
  "connection_mode": "web_session"
}
```

The bot calls `GET /v1/balances?account=mexc_main` regardless of the selected integration. Changing account routing affects how the Gateway authenticates but not the local client protocol. **Never switch an uncertain order execution to a second route automatically.**

## Contact / requests

For access inquiries and exchange priorities, **[message @trusty_kyc_manager on Telegram](https://t.me/trusty_kyc_manager)**. Please share the exchange name, desired route, your bot language and the methods you need. **Do not send credentials or session tokens.**

**Current implementation:** this repository provides a working simulated-data sandbox only. None of the listed production adapters is included, and not all modes may ultimately be permissible for every venue.
