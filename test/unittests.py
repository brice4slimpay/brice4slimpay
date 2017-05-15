# coding: utf-8

import json
import unittest
import slimpay


class APITest(unittest.TestCase):
    """ Test the bearer we get from the API
        Test the begin of the bearer with the public credentials
    """
    def test_bearer(self):
        should_start_with = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        test_bearer = slimpay.get_bearer()
        self.assertEqual(test_bearer[0:36], should_start_with)

    """ Test the status code from authentication"""
    def test_authentication(self):
        return_code = 200
        test_return_code = slimpay.slimpay_authentication()
        self.assertEqual(test_return_code, return_code)

    """ Test the content from post_header"""
    def test_post_header(self):
        test_header = slimpay.post_header()
        for elements in test_header:
            self.assertIn(elements, ('Content-Type', 'profile', 'Accept', 'Authorization'))

    """ Test the content from get_header"""
    def test_get_header(self):
        test_header = slimpay.get_header()
        for elements in test_header:
            self.assertIn(elements, ('profile', 'Accept', 'Authorization'))

    """ Test the amount of the card_transaction"""
    def test_get_card_transaction(self):
        test_transaction = slimpay.get_card_transactions()
        json_transaction = json.loads(test_transaction)
        self.assertEqual(json_transaction['amount'], '192.50')

    """ Test the return value of the payement scheme from get_orders"""
    def test_get_orders(self):
        test_orders = slimpay.get_orders()
        json_orders = json.loads(test_orders)
        self.assertEqual(json_orders['paymentScheme'], 'SEPA.DIRECT_DEBIT.CORE')

    """ Test the return value of the payement scheme"""
    def test_get_card_aliases(self):
        test_aliases = slimpay.get_card_aliases()
        json_orders = json.loads(test_aliases)
        self.assertEqual(json_orders['id'], 'bb78f52e-5881-11e5-949f-bbda0eef6d56')

    """ Test the return value of the payement scheme from create_orders"""
    def test_create_orders(self):
        test_orders = slimpay.create_orders()
        json_orders = json.loads(test_orders)
        self.assertEqual(json_orders['paymentScheme'], 'SEPA.DIRECT_DEBIT.CORE')


if __name__ == '__main__':
    unittest.main()
