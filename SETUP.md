# WebAPI Bridge — repository setup

## Local sandbox

Requires Python 3.10+; no third-party dependencies.

```bash
python -m unittest discover -s tests -v
python -m demo.server
```

In another terminal:

```bash
python -m demo.example_bot
```

The sandbox is read-only, binds to 127.0.0.1 and sends **no requests to real exchanges**.

## Publishing and demand validation

This GitHub repository is currently **private**. External developers cannot see its README or submit Issues unless you grant them access. To collect public interest, create a separate public showcase repository with documentation and an early-access contact link; keep proprietary connectors private.

When available, replace the early-access Issue CTA with your real Telegram handle. Do not publish credentials or accept payment for unavailable features.

## Suggested next steps

- Add your Telegram contact to the README.
- Verify the license and legal conditions for each proposed connector.
- Test live connectors only in authorized environments, and add reliable order reconciliation before live deployment.
- Publish a separate, accurately labeled public product showcase when ready to measure demand.
