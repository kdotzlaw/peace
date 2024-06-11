/*
 * Changes the current tab to
 */
function switchtab(name) {
    console.log(name)
}

/*
 *
 */
function Tab(name) {
    return (
        <div className="homeNavTab">
            <button className="homeNavTabButton" onClick=switchtab{name}>{name}</button>
        </div>
    );
}

function HomeBody() {
    return (
        <div className="homeBody">
            <p>This is the home body</p>
        </div>
    );
}

/*
 * Takes an array of tab names, returns a series of tabs
 */
function buildTabs(arr) {
    // start fragment
    let ret = "<>"
    for(let i = 0; i < arr.length; i++){
        ret.push(<Tab name={arr[i]}/>)
    }
    // end fragment
    ret.push("</>")
    return ret;
}

/*
 * Creates tab nav bar
 * Takes array of strings -> tab/table names
 */
function Nav(arr) {

  return (
      <div className="homeNav">
          {buildTabs(arr)}
      </div>
  );
}

/*
 * Creates Home page elements for use after login
 */
export default function Home(arr) {
  return (
    <div className="home">
        <Nav arr={arr}></Nav>
        <HomeBody></HomeBody>
    </div>
  );
}
