import React from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import InputSentence from './pages/InputSentence';
import InputFile from './pages/InputFile';
import Nav from './components/Nav';
import Home from './pages/Home';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {

    return (
      <Router>
       <Nav />
       <Header/>

      <div className="App">
        <Switch>
          <Route path="/" exact component={Home} />   
          <Route path="/inputsentence" exact component={InputSentence} /> 
          <Route path="/inputfile" exact component={InputFile} />
        </Switch> 
      </div>

      

      <Footer/>
    </Router>

    )
}

export default App;