#  ERC20 배포 주소
#  0x4CEc03622c4209FDa63de4482d90e7cf34EE65D2
from dotenv import load_dotenv
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware  # poa를 처리해주기 위함
from eth_account import Account
import json
import sha3

load_dotenv(verbose=True)
w3 = Web3(Web3.HTTPProvider(os.getenv("RPCURL")))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

private_key = os.getenv("PRIVATE_KEY")
# print("Private Key : ", private_key)

account = Account.from_key(private_key)
# 주소 확인
print("Account Address : ", account.address)
# 잔액 확인
print("Account Balance : ", w3.eth.getBalance(account.address))

contractAddress = "0x4CEc03622c4209FDa63de4482d90e7cf34EE65D2"
with open('./ERC20.json') as f:
    abi = json.load(f)

fdongtokenCA = w3.eth.contract(address=contractAddress, abi=abi)
print('Contract Address : ', contractAddress)
print('Symbol : ', fdongtokenCA.functions.symbol().call())
print("Owner Balance : ", fdongtokenCA.functions.balanceOf(account.address).call())


# transaction.py에 있는 방법대로 보내는 방법
# txid = fdongtokenCA.function.transfer(
#     "0x4EBbD4881a45B836bAc17EA52F1BcEF72b787B0e", 100000000).transact({"from": account.address})
# w3.eth.waitForTransactionReceipt(txid, 500)

k256 = sha3.keccak_256()
# 트랜잭션 데이터 만들기
k256.update('transfer(address,uint256)'.encode())
method_id = "0x" + k256.hexdigest()
to_hex = "4EBbD4881a45B836bAc17EA52F1BcEF72b787B0e".zfill(64)
value_hex = "{:064}".format(100000000)
data = method_id[:10] + to_hex + value_hex
print('Input data : ', data)
signedTransacton = w3.eth.account.sign_transaction(
    dict(
        #  nonce를 시작하는 이유는 사용자가 논스를 몇번을 썼는지 확인해야지 이중지불 문제를 막아줄 수 있다. 똑같은 트랜잭션을 두번보낸게 아니라는 것을 알림
        nonce=w3.eth.getTransactionCount(account.address),
        gas=100000,
        maxFeePerGas=3000000000,
        maxPriorityFeePerGas=3000000000,
        to=contractAddress,
        value=0,
        # input data에 값 입력
        data=data,
        # goerli chainid = 5
        chainId=5,
        type=2
    ), private_key)
print(signedTransacton)

# rawTransaction값만 네트워크에 전송한다.
w3.eth.sendRawTransaction(signedTransacton.rawTransaction)
# 서버측에서 확인하기 위함
print(w3.eth.waitForTransactionReceipt(signedTransacton.hash, 500))
