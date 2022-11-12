import Web3 from 'web3';
// require('dotenv').config();
import InsertToDB from './dbUtill.js';
const web3 = new Web3(new Web3.providers.WebsocketProvider(WSSRPCURL));

// 해당 주소에서 발생하는 topic 정보만 가져온다
function Subscribe(contract_address, topic, type) {
  // 가져올 형식 정의
  web3.eth.subscribe(
    'logs',
    {
      addres: contract_address,
      topics: [topic],
    },
    (err, result) => {
      if (err) {
        console.error(error);
      } else {
        console.log('--------------------------------------');
        console.log('New Transaction Event');
        console.log(type);
        getReceiptFindTransfer(result.transactionHash, type);
      }
    }
  );
}
// 실제 어떤 토큰 정보가 전송되는지
async function getReceiptFindTransfer(txid, type) {
  // 토큰명과 컨트랙트 명이 없는 경우가 있음 -> 다른 이벤트에 달려있는 경우가 있음
  web3.eth.getTransactionReceipt(txid).then((result) => {
    let logs = result.logs;
    for (let log of logs) {
      let topics = log.topics;
      // 0번째가 Transfer인 경우
      if (
        topics[0] ==
        '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
      ) {
        console.log('******************');
        console.log('Find Transfer Log');
        let token_id = topics[3];
        let new_owner = topics[2];
        let before_owner = topics[1];
        let contract_address = log.address;
        token_id = web3.utils.hexToNumberString(token_id);
        InsertToDB(contract_address, token_id, type, before_owner, new_owner);
      }
    }
  });
}

export default Subscribe;
