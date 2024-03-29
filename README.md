- [Python](#Python)
  - [web3](#web3)
  - [트랜잭션 처리(이더리움 전송)](#트랜잭션-처리---이더리움-전송)
  - [컨트랙트와 연동 및 이더리움 전송](#컨트랙트와-연동-및-이더리움-전송)
- [JS](#Javascript)
  - [특정 컨트랙트에서 특정 이벤트 발생 시 정보 가져오기 - NFT 거래소](#특정-컨트랙트에서-특정-이벤트-발생-시-정보-가져오기---NFT-거래소)
## Python

### web3

> [web3.py](https://github.com/FDongFDong/web3-practice/blob/main/python/Web3.py)

- 연결 확인
  - true/false 값 반환
- 블록 정보 조회
  - ![image](https://user-images.githubusercontent.com/20445415/201458656-f5710fc5-b6ea-4b4c-ac2b-e3e40b89bf2d.png)

- 트랜잭션 조회
  - ![image](https://user-images.githubusercontent.com/20445415/201458665-dc4c147c-ac38-4800-9b80-6f0f6963d901.png)
___
### 트랜잭션 처리 - 이더리움 전송
> [transaction.py](https://github.com/FDongFDong/web3-practice/blob/main/python/transaction.py)

- 결과
 ![image](https://user-images.githubusercontent.com/20445415/201459560-89f730e6-0a95-40e8-b942-5277c11e79a9.png)
- Etherscan 결과
 ![image](https://user-images.githubusercontent.com/20445415/201459540-cfe4e23b-c68d-4ba8-9726-07cc98cf0472.png)

___

### 컨트랙트와 연동 및 이더리움 전송


#### 사전 필요한 작업
> [contract.py](https://github.com/FDongFDong/web3-practice/blob/main/python/contract.py)
- 리믹스를 통한 ERC20 토큰 배포 후 배포된 네트워크 주소
  - [ERC20.sol](https://github.com/FDongFDong/solidity_practice/blob/main/contracts/Mint.sol)
- ABI 
  - [ERC20.json](https://github.com/FDongFDong/web3-practice/blob/main/python/ERC20.json)

- 결과
 ![image](https://user-images.githubusercontent.com/20445415/201461463-bef0e7bf-5694-4a65-8688-d83a18ed9f52.png)

- Etherscan 결과
 ![image](https://user-images.githubusercontent.com/20445415/201461437-af74b14e-d914-4f10-b2ec-58342387c215.png)

## Javascript

### 특정 컨트랙트에서 특정 이벤트 발생 시 정보 가져오기 - NFT 거래소
> [web3.Js](https://github.com/FDongFDong/web3-practice/tree/main/JS/web3Js)

- index.js
- subscribe.js 
  - 특정 이벤트를 비동기적으로 체크
- dbUtill.js
  - sqlite3에 데이터 저장

![image](https://user-images.githubusercontent.com/20445415/201467883-508a3441-3004-46a9-a211-e6d1a760c092.png)
