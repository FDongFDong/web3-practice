from dotenv import load_dotenv
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware  # poa를 처리해주기 위함
from eth_account import Account
import json

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
# 이더리움 전송하기
signedTransacton = w3.eth.account.sign_transaction(

    dict(
        #  nonce를 시작하는 이유는 사용자가 논스를 몇번을 썼는지 확인해야지 이중지불 문제를 막아줄 수 있다. 똑같은 트랜잭션을 두번보낸게 아니라는 것을 알림
        nonce=w3.eth.getTransactionCount(account.address),
        gas=100000,
        maxFeePerGas=3000000000,
        maxPriorityFeePerGas=3000000000,
        to="0x4EBbD4881a45B836bAc17EA52F1BcEF72b787B0e",
        value=w3.toWei(0.001, 'ether'),
        data=b'first Transction From Web3py',
        # goerli chainid = 5
        chainId=5,
        type=2
    ), private_key)

print(signedTransacton)

# rawTransaction값만 네트워크에 전송한다.
w3.eth.sendRawTransaction(signedTransacton.rawTransaction)
# 서버측에서 확인하기 위함
print(w3.eth.waitForTransactionReceipt(signedTransacton.hash, 500))
