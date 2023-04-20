import '../App.css';
import React, { useState } from 'react';
import { CSVLink, CSVDownload } from "react-csv";


const axios = require('axios');

function InputFile() {
  
  const [text, setText] = useState("")
  const [result, setResult] = useState([])
  const [userClick,setUserClick] = useState(0)

  const showFile =(e) =>{
    e.preventDefault()
    const reader = new FileReader()

    reader.onload = async (e) => { 
      const text = (e.target.result)
      setText(text)
    };
    reader.readAsText(e.target.files[0])
  }

  const handleInput = async ()=>{
    
    setResult([])
    setUserClick(1)

    let lines =  text.split('\r\n')
    console.log(lines)
    
    lines = lines.join('1712858')

    const formData = new FormData();
    formData.append("text",lines)

    axios.post('http://127.0.0.1:5000/mer-and-men2', formData ).then( res => {

    //console.log(res.data)

      for (const val of res.data) { 
        
        setResult(oldArray => [...oldArray, val['text']]);
        setResult(oldArray => [...oldArray, val['mer'] ]);
        setResult(oldArray => [...oldArray, val['men']]);
        setResult(oldArray => [...oldArray, ['-','-','-','-'] ]);
      }
      setUserClick(0)
     
    })


  }
 
  return (
    <div className="App">  
      <input type="file" accept=".txt" onChange={(e) => showFile(e)} />

      <button onClick={handleInput}>
        Submit
      </button>

      <div>
          {/*
            result.map( (item)=> {return <div>{item} </div>})  
          
          */}

          {/*(result.length)*/}
          
          {result.length != 0 
          && <CSVLink data={result} filename={"result.csv"}>
            Download me
            </CSVLink>}

          {userClick !=0 &&  <div>Waiting ..................</div>}

      </div>
    </div>
  );
 
}

export default InputFile;