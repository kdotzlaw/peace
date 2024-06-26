import logo from './logo.svg';
import './App.css';
import Home from "./Home";

const tables = [
          { id: 0, name: "Volunteers", focused: true, queries: []},
          { id: 1, name: "Jobs", focused: false, queries: []}
      ];

function App() {
  return (
    <div className="App">
      <Home tabdata={tables}/>
    </div>
  );
}

export default App;
