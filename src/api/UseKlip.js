import axios from "axios";
import {
  COUNT_CONTRACT_ADDRESS,
  NFTSIMPLE_CONTRACT_ADDRESS,
} from "../constants";

// ---- how to execute Smart Contract using API

// 여러번 쓸 constant는 따로 빼줘
const A2A_API_PREPARE_URL = "https://a2a-api.klipwallet.com/v2/a2a/prepare";
const APP_NAME = "KLAY_MARKET";

// setCount 함수
export const setCount = (count, setQrvalue) => {
  axios
    .post(A2A_API_PREPARE_URL, {
      bapp: {
        name: APP_NAME,
      },
      type: "execute_contract",
      transaction: {
        to: COUNT_CONTRACT_ADDRESS,
        abi: '{ "constant": false, "inputs": [{ "name": "_count", "type": "uint256" }], "name": "setCount", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }',
        // set count를 실행할거야 라는 설명서를 넣어줌.
        value: "0",
        params: `[\"${count}\"]`, // 새로운 값을 이곳에
      },
    })
    .then((res) => {
      const { request_key } = res.data;
      const qrcode = `https://klipwallet.com/?target=/a2a?request_key=${request_key}`;

      setQrvalue(qrcode);

      let timerId = setInterval(() => {
        axios
          .get(
            `https://a2a-api.klipwallet.com/v2/a2a/result?request_key=${request_key}`
          )
          .then((res) => {
            if (res.data.result) {
              // status가 success일 때, 즉 완료되었을 때에만 결과를 출력해.
              if (res.data.result.status === "success") {
                console.log(`[Result] ${JSON.stringify(res.data.result)}`);
                clearInterval(timerId);
              }
            }
          });
      }, 1000);
    });
};

export const getAddress = (setQrvalue) => {
  axios
    .post(A2A_API_PREPARE_URL, {
      bapp: {
        name: APP_NAME,
      },
      type: "auth",
    })
    .then((res) => {
      const { request_key } = res.data;
      const qrcode = `https://klipwallet.com/?target=/a2a?request_key=${request_key}`;

      setQrvalue(qrcode);

      let timerId = setInterval(() => {
        axios
          .get(
            `https://a2a-api.klipwallet.com/v2/a2a/result?request_key=${request_key}`
          )
          .then((res) => {
            if (res.data.result) {
              console.log(`[Result] ${JSON.stringify(res.data.result)}`);
              clearInterval(timerId);
              return JSON.stringify(res.data.result);
            }
          });
      }, 1000);
    });
};
