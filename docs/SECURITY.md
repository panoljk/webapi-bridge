# Security and integration policy

- Do not post access tokens, cookies, passwords, exchange API keys or private keys in Issues.
- The current demo listens only on loopback (`127.0.0.1`) and never contacts an exchange.
- A production implementation should keep all exchange credentials on the customer's device and avoid withdrawal permissions.
- Local credentials must be scoped; license verification must remain separate from trading.
- Web-session connectors are only considered for permitted use; no defeating authentication, rate limits, blocklists or platform security controls.
- Ambiguous order responses require reconciliation before retries.
- Nothing here guarantees trading performance or access to any venue.
