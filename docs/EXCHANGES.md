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

## Exchange candidate matrix

Legend: **API candidate** means a future adapter target, not a built integration. **Review required** means the exact availability, account eligibility or policy permission must be verified. **Not publicly offered** means a standard trading API is not currently established for that venue from the information being used; this is not a permanent claim.

| Exchange | Official API route | Web Session route |
|---|---|---|
| Binance | API candidate | Review required |
| Bybit | API candidate | Review required |
| OKX | API candidate | Review required |
| Bitget | API candidate | Review required |
| Gate.io | API candidate | Review required |
| KuCoin | API candidate | Review required |
| MEXC | API candidate | Review required |
| BingX | API candidate | Review required |
| Phemex | API candidate | Review required |
| WEEX | API candidate | Review required |
| Bitunix | API candidate | Review required |
| Toobit | API candidate | Review required |
| BloFin | API candidate | Review required |
| CoinEx | API candidate | Review required |
| XT.COM | API candidate | Review required |
| WhiteBIT | API candidate | Review required |
| CoinW | API candidate | Review required |
| OrangeX | API candidate | Review required |
| Tapbit | API eligibility review | Review required |
| Zoomex | API candidate | Review required |
| Pionex | Access-conditions review | Review required |
| BTCC | Current API status review | Review required |
| KCEX | No publicly offered trading API confirmed | Review required |
| AlphaX | API availability review | Review required |

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
