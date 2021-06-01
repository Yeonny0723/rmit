import Caver from "caver-js";
import CounterABI from "../abi/CounterABI.json";
import CounterABI2 from "../abi/CounterABI2.json";
import {
  CHAIN_ID,
  COUNT_CONTRACT_ADDRESS,
  NFTSIMPLE_CONTRACT_ADDRESS,
} from "../constants";
const option = {
  headers: [
    {
      name: "Authorization",
      value:
        "Basic S0FTSzJERlNCU0lWRzJDN0NQMDg4UEpQOlNwQWxGZGYySU9NM3N3OEVWQ0VXamVYUHJyTzZKN3NJMUxCenFnNWU=",
    },
    {
      name: "x-chain-id",
      value: CHAIN_ID,
    },
  ],
};
const caver = new Caver(
  new Caver.providers.HttpProvider(
    "https://node-api.klaytnapi.com/v1/klaytn",
    option
  )
);

const CountContract = new caver.contract(CounterABI, COUNT_CONTRACT_ADDRESS);

export const readCount = async () => {
  const _count = await CountContract.methods.count().call();
  console.log(_count);
};

export const getBalance = (address) => {
  caver.rpc.klay.getBalance(address).then((res) => {
    const balance = caver.utils.convertFromPeb(
      caver.utils.hexToNumberString(res)
    );
    console.log(balance);
    return balance;
  });
};

export const setCount = async (newCount) => {
  try {
    // 사용할 account address 설정.
    // 근데 이게 문제야...이 코드는 누구나 확인할 수 있는데 Privatekey가 너무 대놓고 있잖아...
    const privatekey = "";
    const deployer = caver.wallet.keyring.createFromPrivateKey(privatekey);
    caver.wallet.add(deployer);
    // 실행 input 블록체인으로 날리기
    // 결과 확인
    const receipt = await CountContract.methods.setCount(newCount).send({
      from: deployer.address, // transaction을 하려는 놈 address
      gas: "0x4bfd200", // 수수료
    });
    console.log(receipt);
  } catch (e) {
    console.log(`[Error_SET_COUNT]${e}`);
  }
};

const NFTSimpleContract = new caver.contract(
  CounterABI2,
  NFTSIMPLE_CONTRACT_ADDRESS
);

export const whoOwnedWhatTokens = async () => {
  const _tokens = await NFTSimpleContract.methods.whoOwnedWhatTokens().call();
  console.log(_tokens);
};
