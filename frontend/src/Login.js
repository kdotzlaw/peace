import React from 'react';
import {useState} from "react";
import ReactDOM from "react-dom/client";

/*
Component: Login
- Handles the login form
 */

function Login(){
    //Define initial state for form variables
    const [inputs, setInputs] = useState({});

    //Handle Change
    const handleChange=(event)=>{
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values=>({...values,[name]:value}));
    }

    //Handle form submit
    const handleSubmit =(event)=>{
        event.preventDefault();
        //send to api
        alert("Submit");
    }
    //Return and render
    return(
        <form onSubmit={handleSubmit}>
            <label>Enter A2Hosted admin username:
                <input
                    type="text"
                    name="username"
                    value={inputs.username || ""}
                    onChange={handleChange}

                />
            </label>
            <label> Enter A2Hosted admin password:
                <input
                    type="text"
                    name="password"
                    value={inputs.password || ""}
                    onChange={handleChange}

                />
            </label>
            <label> Enter host ip address:
                <input
                    type="text"
                    name="host"
                    value={inputs.host || ""}
                    onChange={handleChange}

                />
            </label>
            <label>Enter database name:
                <input
                    type=""
                    name="db"
                    value={inputs.db || ""}
                    onChange={handleChange}
                />
            </label>
            <input type="submit"/>

        </form>
    )
}
export default Login;
