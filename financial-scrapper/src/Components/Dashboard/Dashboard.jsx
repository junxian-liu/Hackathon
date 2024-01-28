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
const{PythonShell} = require('python-shell')
let options = {
  scriptPath: 'E:/hackathon',
  args: [Ticker],
};
PythonShell.run('main.py', options, (err, res) => {
  if (err) console.log(err);
  if (res) console.log(res)
})