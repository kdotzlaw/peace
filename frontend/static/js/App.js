import React, { Component } from "react";
import {render} from "@testing-library/react";
//CSS imports
import './static/App.css';
//Component imports
import Login from "./Login.js";


/*class App extends React.Component{
    constructor(props) {
        super(props);
        console.log("App constructor");
    }
  render(){
       return(
            <Login />
       );
  }
}
export default App;
*/

class App extends React.Component{
    render(){
        return(
            <div>
                <Login />
             </div>
        );
    }
}
export default App;

