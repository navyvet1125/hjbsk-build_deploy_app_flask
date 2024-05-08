// Description: This script is used to make a request to the server to perform an operation

let runOperation = (op) => {
    if (op === "sum" || op === "sub" || op === "mul" || op === "div" || op === "mod" || op === "pow" || op === "intdiv") {
        let num1 = parseFloat(document.getElementById("num1").value);
        let num2 = parseFloat(document.getElementById("num2").value);
        const url = `http://localhost:5000/${operator}?num1=${num1}&num2=${num2}`;
        fetch(url)
        .then(response => response.json())
        .then(res => document.getElementById("system_response").innerHTML = "Result: " + res.result)
        .catch(err => document.getElementById("system_response").innerHTML = "Error: " + err);    
    } else {
        document.getElementById("system_response").innerHTML = "Invalid operator";
    }
};