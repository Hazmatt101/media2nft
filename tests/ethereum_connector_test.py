import unittest
from connectors.ethereum_connector import EthereumConnector

class EthereumConnectorTest(unittest.TestCase):

    def test_create_transaction(self):
        eth_connector = EthereumConnector()
        smart_contract_address = ''
        address_sending = ''
        gas_limit = ''
        gas_price = ''
        function_data = ''
        transaction = eth_connector.create_transaction(smart_contract_address, address_sending, gas_limit, gas_price, function_data)