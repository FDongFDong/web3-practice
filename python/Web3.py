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
    'https://goerli.infura.io/v3/622e714bb19a49f2b2966ccb88137353'))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)
# 연결이 되었는지 확인하는 함수
print(w3.isConnected())
# 최근 블록 정보 조회
latestBlock = w3.eth.get_block('latest')
print(json.dumps(dict(latestBlock), cls=HexJsonEncoder))
# 트랜잭션 처리(블록 안에있는 모든 트랜잭션 id 값들을 가져올 수 있다.)
txList = latestBlock.transactions
for tx in txList:
    print("---------------------------------")
    print(Web3.toHex(tx))  # tx id를 16진수로 출력
    txDetail = w3.eth.getTransaction(Web3.toHex(tx))
    print(json.dumps(dict(txDetail), cls=HexJsonEncoder))
