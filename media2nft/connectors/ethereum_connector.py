from web3 import Web3
from dotenv import load_dotenv
import os


class EthereumConnector:
    api_key = None
    url = None
    web3_instance = None
    latest_block = None

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('ALCHEMY_API_KEY')
        self.url = os.getenv('ALCHEMY_API_URL_HTTPS')
        self.web3_instance = Web3(Web3.HTTPProvider(self.url))
        self.latest_block = self.get_latest_block_number()

    def is_connected(self):
        return self.web3_instance.is_connected(show_traceback=True)

    def create_eth_account(self):
        return self.web3_instance.eth.account.create()

    def create_transaction(self, smart_contract_address, address_sending, gas_limit, gas_price, function_data):
        # Check address checksum
        if not self.web3_instance.to_checksum_address(smart_contract_address.lower()):
            raise ConnectionError('Bad receiving address provided.')

        transaction = {
            'to': smart_contract_address,
            'from': address_sending,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'data': function_data
        }
        transaction_data = transaction.get('data')
        if isinstance(transaction_data, str):
            transaction['data'] = transaction_data.encode('utf-8').hex()
            return transaction
        else:
            return transaction

    def sign_transaction(self, transaction):
        if self.is_connected():
            return self.web3_instance.eth.sign_transaction(transaction, self.api_key)
        else:
            raise ConnectionError('Could not connect to the Ethereum net.')

    def send_transaction(self, signed_transaction):
        if self.is_connected():
            return self.web3_instance.eth.send_raw_transaction(signed_transaction.rawTransaction)
        else:
            raise ConnectionError('Could not connect to the Ethereum net.')

    def wait_for_transaction_receipt(self, transaction_hash):
        if self.is_connected():
            return self.web3_instance.eth.wait_for_transaction_receipt(transaction_hash)
        else:
            raise ConnectionError('Could not connect to the Ethereum net.')

    def get_latest_block_number(self):
        return self.web3_instance.eth.get_block("latest")
