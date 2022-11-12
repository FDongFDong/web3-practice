from web3 import Web3
from web3.middleware import geth_poa_middleware  # poa를 처리해주기 위함
import json
from hexbytes import HexBytes


class HexJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HexBytes):
            return obj.hex()
        return super().default(obj)


w3 = Web3(Web3.HTTPProvider(
    ''))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)
# 연결이 되었는지 확인하는 함수
print(w3.isConnected())
# 블록 조회
print("Get Last Block")
latestBlock = w3.eth.get_block('latest')
print(json.dumps(dict(latestBlock), cls=HexJsonEncoder))
