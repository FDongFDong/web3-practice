import Web3 from 'web3';
// require('dotenv').config();
import Subscribe from './subscribe.js';

const web3 = new Web3(new Web3.providers.WebsocketProvider(WSSRPCURL));

const foundatation_token_address = '0x3B3ee1931Dc30C1957379FAc9aba94D1C48a5405';
const foundatation_market_address =
  '0xcDA72070E455bb31C7690a170224Ce43623d0B6f';

// 특정한 이벤트만 가져오기

// 직접 컨트랙트로 가져오기
const transfer_topic =
  '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef';

const market_list_topic = web3.utils.sha3(
  'ReserveAuctionCreated(address, address, uint256, uint256, uint256  uint256, uint256)'
);
const market_sold_topic = web3.utils.sha3(
  'ReserveAuctionFinalized (uint256, address, address, uint256, uint256, uint256)'
);

Subscribe(foundatation_token_address, transfer_topic, 'TRANSFER');
Subscribe(foundatation_market_address, market_list_topic, 'TRANSFER');
Subscribe(foundatation_market_address, market_sold_topic, 'TRANSFER');
