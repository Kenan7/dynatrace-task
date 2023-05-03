import unittest
from app.services import (
    calculate_exchange_rate_average,
    calculate_exchange_rate_extremes,
    calculate_exchange_rate_diff
)

class TestCalculateExchangeRate(unittest.TestCase):
    def test_calculate_exchange_rate_average(self):
        data = {
            "table": "A",
            "currency": "bat (Tajlandia)",
            "code": "THB",
            "rates": [
                {
                    "no": "001/A/NBP/2021",
                    "effectiveDate": "2021-01-04",
                    "mid": 0.1266
                }
            ]
        }
        result = calculate_exchange_rate_average(data)
        self.assertEqual(result, 0.1266)

    def test_calculate_exchange_rate_extremes(self):
        data = {
            "table": "A",
            "currency": "bat (Tajlandia)",
            "code": "THB",
            "rates": [
                {
                    "no": "001/A/NBP/2021",
                    "effectiveDate": "2021-01-04",
                    "mid": 0.1266
                },
                {
                    "no": "002/A/NBP/2021",
                    "effectiveDate": "2021-01-05",
                    "mid": 0.1267
                },
                {
                    "no": "003/A/NBP/2021",
                    "effectiveDate": "2021-01-06",
                    "mid": 0.1268
                }
            ]
        }
        result = calculate_exchange_rate_extremes(data)
        self.assertEqual(result, {'max': 0.1268, 'min': 0.1266})

    def test_calculate_exchange_rate_diff(self):
        data = {
            "table": "C",
            "currency": "bat (Tajlandia)",
            "code": "THB",
            "rates": [
                {
                    "no": "001/C/NBP/2021",
                    "effectiveDate": "2021-01-04",
                    "bid": 0.1266,
                    "ask": 0.1268
                },
                {
                    "no": "002/C/NBP/2021",
                    "effectiveDate": "2021-01-05",
                    "bid": 0.1267,
                    "ask": 0.1269
                },
                {
                    "no": "003/C/NBP/2021",
                    "effectiveDate": "2021-01-06",
                    "bid": 0.1268,
                    "ask": 0.1270
                }
            ]
        }
        result = calculate_exchange_rate_diff(data)
        self.assertEqual(result, {'diff': 0.0002})
