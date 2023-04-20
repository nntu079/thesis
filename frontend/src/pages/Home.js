import '../App.css';
import React, { useState } from 'react';
import { Link } from 'react-router-dom'

const axios = require('axios');

function Home() {
   
 
  return (
    <div className="App">

        <div style={{marginTop:30}}>

        <Link to="/inputsentence"  >
                  <img src={`${process.env.PUBLIC_URL}/bert.png`} style={{width:400, height:200}}/> 
                  
        </Link>

        <Link to="/inputfile"  >
                  <img src={`${process.env.PUBLIC_URL}/text-mining.jpg`} style={{width:400, height:200}} /> 
        </Link>

        </div>
        

    </div>
  );
 
}

export default Home;