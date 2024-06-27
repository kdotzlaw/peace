/*import React from 'react';
import ReactDOM from 'react-dom/client';
import './static/index.css';
//import App from './App.js';
import Login from './Login.js';


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(


<Login />);*/


import React from 'react';
import ReactDOM from 'react-dom/client';
//import Login from './Login.js';
import App from './App.js';
ReactDOM.createRoot(document.querySelector("#root")).render(
<React.StrictMode>
    <App />
</React.StrictMode>
);


