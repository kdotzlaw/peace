// hold current tab id
let current = 0

/*
 * Changes the current tab to 'name' if not already the current tab
 */
function switchtab(name, id) {
    if(id !== current){
        current = id;
        // get all components with  class == 'focused'
        var toUnfocus = document.getElementsByClassName("focused")
        // set 'focused' -> 'unfocused'
        while(toUnfocus.length > 0){
            toUnfocus[0].classList.add("unfocused")
            toUnfocus[0].classList.remove("focused")
        }
        // get all components with a class == 'name'
        var toFocus = document.getElementsByClassName("unfocused ".concat(name))
        // set 'unfocused' -> 'focused'
        while(toFocus.length > 0){
            toFocus[0].classList.add("focused")
            toFocus[0].classList.remove("unfocused")
        }
    } // else, stay on same tab
}

/*
 *
 */
function Tab({name, focus, id}) {
    /*let classes = "homeNavTab " + name
    if(focus){
        classes += " focused"
    } else {
        classes += " unfocused"
    }*/
    return (
        <div className={focus ? "homeNavTab " + name + " focused": "homeNavTab " + name + " unfocused"}>
            <button className={focus ? "homeNavTabButton " + name + " focused": "homeNavTabButton " + name + " unfocused"}
                    onClick={(event) => switchtab(name, id)}>{name}</button>
        </div>
    );
}

function HomeBody({name, focus}) {
    let f;
    if(focus){
        f = " focused ".concat(name)
    } else {
        f = " unfocused ".concat(name)
    }
    return (
        <div className={"homeBody".concat(f)}>
            <p>This is the home body for {name}</p>
        </div>
    );
}

/*
 * Takes an array of tab names, returns a series of tabs
 */
function buildTabs(tabdata) {

    const tablist = tabdata.map(t => <Tab name={t.name} focus={t.focused} id={t.id}/>)
    // return fragment
    return <>{tablist}</>;
}

/*
 * Creates tab nav bar
 * Takes array of strings -> tab/table names
 */
function Nav({tabdata}) {
    return (
        <div className="homeNav">
            {buildTabs(tabdata)}
        </div>
    );
}

/*
 * Creates Home page elements for use after login
 */
export default function Home({tabdata}) {
    return (
        <div className="home">
            <Nav tabdata={tabdata}></Nav>
            <HomeBody name={tabdata[0].name} focus={tabdata[0].focused}></HomeBody>
            <HomeBody name={tabdata[1].name} focus={tabdata[1].focused}></HomeBody>
        </div>
    );
}
