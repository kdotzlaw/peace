import React from 'react';
import {useState} from "react";
import "./Login.css";

import ReactDOM from "react-dom/client";

/*
Component: Login
- Handles the login form
 */

function Login(){
    //Define initial state for form variables
    const [inputs, setInputs] = useState({});

    /*
        handleChange:
        INPUT: on change event from form input
        OUTPUT: the value of form input with [name] is changed to [name:value]
     */
    const handleChange=(event)=>{
        const name = event.target.name;
        const value = event.target.value;
        //sets inputs for each name to the value with matching name
        setInputs(values=>({...values,[name]:value}));
    }


    //Return and render
    return(
    <div id="main">
        <div id="container" className="focused">
            <h1>Peace DB Interface</h1>
            <form id="form-login" action="../login" method="POST" >
                <label>Enter A2Hosted admin username:
                    <input
                        className="input-item"
                        type="text"
                        name="username"
                        value={inputs.username || ""}
                        onChange={handleChange}

                    />
                </label>
                <label> Enter A2Hosted admin password:
                    <input
                        className="input-item"
                        type="text"
                        name="password"
                        value={inputs.password || ""}
                        onChange={handleChange}

                    />
                </label>
                <label> Enter host ip address:
                    <input
                        className="input-item"
                        type="text"
                        name="host"
                        value={inputs.host || ""}
                        onChange={handleChange}
                    />
                </label>
                <label>Enter database name:
                    <input
                        className="input-item"
                        type=""
                        name="db"
                        value={inputs.db || ""}
                        onChange={handleChange}
                    />
                </label>
               <input
                    className="input-item"
                    id ="btn-submit"
                    type="submit"
               />
            </form>
        </div>
    </div>
    )
}
export default Login;
