from web3 import Web3
from dotenv import load_dotenv
import os


class EthereumConnector:
    infura_api_key = None
    infura_url = None
    web3_instance = None

    def __init__(self):
        load_dotenv()
        infura_api_key = os.getenv('INFURA_API_KEY')
        infura_url = 'https://mainnet.infura.io/v3/' + str(infura_api_key)
        web3_instance = Web3(Web3.HTTPProvider(infura_url))

    @staticmethod
    def create_transaction(smart_contract_address, address_sending, gas_limit, gas_price, function_data):
        transaction = {
            'to': smart_contract_address,
            'from': address_sending,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'data': function_data
        }
        return transaction

    def sign_transaction(self, web3_instance, transaction):
        return web3_instance.eth.account.signTransaction(transaction, self.infura_api_key)

    def send_transaction(self, web3_instance, signed_transaction):
        return web3_instance.eth.sendRawTransaction(signed_transaction.rawTransaction)

    def wait_for_transaction_receipt(self, web3_instance, transaction_hash):
        return web3_instance.eth.waitForTransactionReceipt(transaction_hash)
