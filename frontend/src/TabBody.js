
// hardcode relevant data for each table based on name
const data = {
    Volunteers: {
        queries: [
            "<option key={0} value={0}>Select all volunteers.</option>",
            "<option key={1} value={1}>Select volunteers by name.</option>",
            "<option key={2} value={2}>Add a volunteer.</option>"
        ]
    },
    Jobs: {
        queries: [
            "<option key={0} value={0}>Select all jobs.</option>",
            "<option key={1} value={1}>Select job by name.</option>",
            "<option key={2} value={2}>Add a job.</option>"
        ]
    }
}

function runQuery() {
    alert(1)
}

function TabBody({name}) {
    return (
        <div>
            <div className={"tabHeader"}>
                <form>
                    <select name={"query"} id={"query"}>
                        {data[name]["queries"]}
                    </select>
                    <input type={"submit"} onSubmit={runQuery}/>
                </form>
            </div>
            <div className={"tabOutput"}>

            </div>
        </div>
    );
}

export default TabBody;