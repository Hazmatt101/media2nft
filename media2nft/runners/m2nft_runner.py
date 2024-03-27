from media2nft.connectors.ethereum_connector import EthereumConnector
from media2nft.converters.file_hasher import FileHasher


class M2NFTRunner:
    eth_connector = None
    file_hasher = None

    def __init__(self):
        self.eth_connector = EthereumConnector()
        self.file_hasher = FileHasher()
    