# API reference

WebAPI Bridge is designed to offer one local API contract across supported trading connectors. The working repository demo is **read-only and simulated**.

## Sandbox endpoints (implemented)

| Method | Path | Description |
|---|---|---|
| GET | `/v1/health` | Gateway health |
| GET | `/v1/accounts` | Simulated accounts |
| GET | `/v1/balances?account=paper-main` | Paper balance |
| GET | `/v1/positions?account=paper-main` | Empty simulated positions |

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
