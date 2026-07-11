import unittest

from network_tool import summarize_cidr


class NetworkToolTests(unittest.TestCase):
    def test_summarize_cidr(self):
        result = summarize_cidr("192.168.1.0/24")
        self.assertEqual(result["network_address"], "192.168.1.0")
        self.assertEqual(result["broadcast_address"], "192.168.1.255")
        self.assertEqual(result["subnet_mask"], "255.255.255.0")
        self.assertEqual(result["host_count"], 254)
        self.assertEqual(result["usable_range"], "192.168.1.1 - 192.168.1.254")


if __name__ == "__main__":
    unittest.main()
