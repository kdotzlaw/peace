import React, { Component } from "react";
import './static/App.css';
import { Login } from "./Login.js";
import {render} from "@testing-library/react";

class App extends React.Component{
    constructor(props) {
        super(props);
    }
  render(){
       return(
       <div>
            <Login />
       </div>

       );
  }
}

export default App;
