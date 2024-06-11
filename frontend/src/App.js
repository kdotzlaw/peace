import './App.css';
import Login from "./Login.js";
import React from "react";
import {render} from "@testing-library/react";

class App extends React.Component{
    constructor(props) {
        super(props);
    }
  render(){
       return(
           <Login/>
       );
  }
}

export default App;
