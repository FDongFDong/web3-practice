// getBalance.js
// infura는 뭐하는 곳?
const Web3 = require('web3');
const rpcURL = 'https://ropsten.infura.io/v3/622e714bb19a49f2b2966ccb88137353';
const web3 = new Web3(rpcURL);

const account = '0x4EBbD4881a45B836bAc17EA52F1BcEF72b787B0e';

web3.eth
  .getBalance(account) // 지갑의 잔액을 확인하는 함수
  .then((balance) => {
    console.log(`지갑 ${account}의\n 잔액은 ${balance} wei`); // 화폐 단위가 wei이다.
    return web3.utils.fromWei(balance, 'ether'); //  wei 단위를 다른 화폐 단위로 변환하는 함수
  })
  .then((eth) => {
    console.log(`이더 단위로는 \n${eth} ETH 입니다.`);
  });
