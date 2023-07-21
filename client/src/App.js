
import React, { useState } from 'react';
import './App.css';

function App() {
  const [result, setResult] = useState({
    "基准值最高可能性区间": "",
    "取值最优区间": " "
  })
  const [form, setForm] = useState({
    bidsNum: "",
    bidsRangeLow: "",
    bidsRangeHigh: ""
  })
  const handleInputChange = (e) => {
    setForm({
      ...form,
      [e.target.id]: e.target.value
    })
  };


  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://10.140.0.3:8888/bidding", {
      method: "POST",
      headers: {"Content-Type": "application/json",
                "Access-Control-Allow-Origin": '*'},
      body: JSON.stringify({
        "bidsNum": form.bidsNum,
        "bidsRangeLow": form.bidsRangeLow,
        "bidsRangeHigh": form.bidsRangeHigh
      
      })  
    })
    .then(response => response.json())
    .then((data) => {
      setResult({
      "基准值最高可能性区间": data["confidenceInterval"],
      "取值最优区间": data["bestInterval"]
    })})
    .catch(err => console.log(err))
      
  }



  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>竞标数量（可变竞标价数量）
          <input type="text" placeholder="竞标价数量" id="bidsNum" value={form.bidsNum} onChange={handleInputChange}/>
        </label>
        <label> 最低可能报价
          <input type="text" placeholder="最低可能报价" id="bidsRangeLow" value={form.bidsRangeLow} onChange={handleInputChange}/>
        </label>
        <label> 最高可能报价
          <input type="text" placeholder="最高可能报价" id="bidsRangeHigh" value={form.bidsRangeHigh} onChange={handleInputChange}/>
        </label>
        <button className="button" type="submit">Submit  </button>
      </form>
      <div className='result'>
        <h1> 统计上竞标基准值有95% 可能性存在于此范围：</h1>
        <span>{result["基准值最高可能性区间"]}</span>
        <h1> 报价区间</h1>
        <span>{result["取值最优区间"]}</span>
      </div>
    </div>
  );
}

export default App;
