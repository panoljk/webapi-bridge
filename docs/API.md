# API reference

WebAPI Bridge is designed to offer one local API contract across supported trading connectors. The working repository demo is **read-only and simulated**.

## Sandbox endpoints (implemented)

| Method | Path | Description |
|---|---|---|
| GET | `/v1/health` | Gateway health |
| GET | `/v1/accounts` | Simulated accounts |
| GET | `/v1/balances?account=paper-main` | Paper balance |
| GET | `/v1/positions?account=paper-main` | Empty simulated positions |

## Proposed account routing (not implemented yet)

Account aliases will select both the exchange and the approved connection method. For example, `mexc-main` could use Official API while `mexc-session` could use an eligible Web Session connector. **The bot calls the same local API in either case**.

Illustrative account configuration:

```json
{
  "account_alias": "mexc-main",
  "exchange": "mexc",
  "connection_mode": "official_api"
}
```

The proposed values are `official_api` and `web_session`. Neither selects a route in the current simulated-data sandbox. The local Gateway must refuse unsupported or unapproved modes; switching routes after an ambiguous order submission is not automatic.

[24 exchange candidates and mode-selection concept](EXCHANGES.md).

## Designed execution endpoints (not implemented yet)

| Method | Path | Description |
|---|---|---|
| POST | `/v1/orders` | Order placement |
| GET | `/v1/orders/{id}` | Order status |
| DELETE | `/v1/orders/{id}` | Order cancellation |
| WS | `/v1/stream` | Real-time order and position updates |

No trade endpoint is active. Writes return HTTP 405.

### Test locally

```bash
python -m demo.server
curl http://127.0.0.1:8787/v1/health
```

Expected: `{"ok":true,"mode":"sandbox","live_trading":false}`.

The eventual live SDK will require scoped local API credentials, duplicate-order protection and contract-aware quantity conversion.
