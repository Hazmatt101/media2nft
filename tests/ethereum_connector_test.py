import unittest
import os

from media2nft.connectors.ethereum_connector import EthereumConnector
from media2nft.models.gas_limit import GasLimit


class EthereumConnectorTest(unittest.TestCase):

    def test_create_transaction(self):
        eth_connector = EthereumConnector()
        smart_contract_address = os.getenv('TEST_SMART_CONTRACT_ADDRESS')
        address_sending = os.getenv('TEST_ADDRESS_SENDING')
        gas_limit = GasLimit.DEFAULT_TEST_GAS_LIMIT
        gas_price = '0x9184e72a000'
        function_data = 'some function data'
        transaction_result = eth_connector.create_transaction(smart_contract_address, address_sending, gas_limit,
                                                              gas_price, function_data)
        self.assertIsNotNone(transaction_result)
        self.assertEqual(transaction_result, {'to': smart_contract_address,
                                              'from': address_sending, 'gas': '0x1C9C380',
                                              'gasPrice': '0x9184e72a000',
                                              'data': '736f6d652066756e6374696f6e2064617461'})

    def test_sign_transaction(self):
        eth_connector = EthereumConnector()
        smart_contract_address = os.getenv('TEST_SMART_CONTRACT_ADDRESS')
        address_sending = os.getenv('TEST_ADDRESS_SENDING')
        transaction = {'to': smart_contract_address,
                       'from': address_sending,
                       'gas': '0x1C9C380',
                       'gasPrice': '0x9184e72a000',
                       'data': '736f6d652066756e6374696f6e2064617461'}
        signed_transaction_result = eth_connector.sign_transaction(transaction)
        print(signed_transaction_result)
        self.assertIsNotNone(signed_transaction_result)

    def test_get_latest_block_number(self):
        eth_connector = EthereumConnector()
        latest_block_result = eth_connector.get_latest_block_number()
        print('latest block: ', latest_block_result)
        self.assertIsNotNone(latest_block_result)
