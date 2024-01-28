import React, {useState } from "react";
import './Dashboard.css'

const Ticker = () => {
    const [Ticker, setTicker] = useState ('');

const TickerInput = (event) => {
    setTicker(event.target.value);
  };

  return (
    <div>
      <label>
        Search:
        <input
          type="text"
          value={Ticker}
          onChange={TickerInput}
          placeholder="Enter Ticker..."
        />
      </label>
    </div>
  );
}
export default Ticker;