import '../App.css';
import React, { useState } from 'react';

const axios = require('axios');

function InputSentence() {
  const [text,setText]= useState("")

  const [resultText,setResultText] = useState([])
  const [resultMer,setResultMer]  = useState([])
  const [resultMen,setResultMen]  = useState([])

  const [currentToken,setCurrentToken]= useState("")
  const [currentMen,setCurrentMen] = useState("")

  const handleChange = (e)=> {
    setText(e.target.value)
  } 

  const handleSubmit = () =>{
    const formData = new FormData();
    
    formData.append("text",text)
    
    axios.post('http://127.0.0.1:5000/mer-and-men', formData ).then( res => {
      
      //console.log(res.data['text'])
      setResultText(res.data['text'])
      setResultMer(res.data['mer'])
      setResultMen(res.data['men'])
      
      //console.log(resultText)

    })
    
  }

  const displayMen = (key) =>{
    setCurrentToken(resultText[key])
    setCurrentMen(resultMen[key])
  }

  const test = () =>{
    setCurrentToken("")
    setCurrentMen("")
  }
 
  return (
    <div className="App">
       <label>Input sentence : </label>
       <br/>
        <textarea style={{width:500, height:100}}
          onChange={ (e)=> handleChange(e)}
        />
        <br/>

        <button onClick={handleSubmit}>
          submit
        </button>
        <br></br>

        
        {
          <div>{
            resultText.map((item,index)=>{
              return (
                
                <>
                  {
                    resultMer[index]=='O'
                    ? <span key={index} 
                    onMouseEnter   = {()=>displayMen(index)} 
                    onMouseLeave   = {()=>test()} 
                    >
                      {item +' '} 
                    </span>

                    : <span style={{background:'yellow'}} 
                    key={index} 
                    onMouseEnter   = {()=>displayMen(index)}
                    onMouseLeave   = {()=>test()} 
                    > {item + ' '} 
                    </span>
                  }
                </>
                
              )})}
          </div>
        }

        <div>
            {
              currentMen != "" &&
              <div>
              {currentToken} ' : ' {currentMen}
              </div>
            }
        </div>


    </div>
  );
 
}

export default InputSentence;