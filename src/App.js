import { useState } from "react";
import logo from "./logo.svg";
import { readCount, getBalance, whoOwnedWhatTokens } from "./api/UseCaver";
import "./App.css";
import QRCode from "qrcode.react";
import * as KlipAPI from "./api/UseKlip";

const onPressButton = (_balance, _setBalance) => {
  _setBalance(_balance);
};

const DEFAULT_QR_CODE = "DEFAULT";

function App() {
  const [balance, setBalance] = useState("0");
  const [qrvalue, setQrvalue] = useState(DEFAULT_QR_CODE);
  readCount();

  let MYADDRESS;
  const onClickGetAddress = () => {
    MYADDRESS = KlipAPI.getAddress(setQrvalue);
  };

  const onClickSetCount = () => {
    KlipAPI.setCount(2000, setQrvalue); // setQrvalue함수를 넘겨줌
  };

  return (
    <div className="App">
      <header className="App-header">
        <button
          onClick={() => {
            onClickGetAddress();
          }}
        >
          주소 가져오기
        </button>
        <br />
        <button
          onClick={() => {
            onClickSetCount();
          }}
        >
          카운트 값 변경
        </button>
        <br />
        <QRCode value={qrvalue} />
        <br></br>
        <p>{balance}</p>
        <button
          onClick={() => {
            whoOwnedWhatTokens({ MYADDRESS });
          }}
        >
          내 소유 토큰 보기
        </button>
      </header>
    </div>
  );
}

export default App;
