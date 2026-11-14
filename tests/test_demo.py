"""Tests for the read-only sandbox."""
import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from demo.server import GatewayHandler

class SandboxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), GatewayHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def test_health(self):
        with urlopen(self.base + "/v1/health") as response:
            data = json.load(response)
        self.assertTrue(data["ok"])
        self.assertEqual(data["mode"], "sandbox")
        self.assertFalse(data["live_trading"])

    def test_simulated_balance(self):
        with urlopen(self.base + "/v1/balances?account=paper-main") as response:
            data = json.load(response)
        self.assertTrue(data["simulated"])

    def test_order_write_disabled(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(Request(self.base + "/v1/orders", data=b"{}", method="POST"))
        self.assertEqual(error.exception.code, 405)

if __name__ == "__main__":
    unittest.main()
