// Description: This script is used to make a request to the server to perform an operation

const runOperation = async (op) => {
    if (op === "sum" || op === "sub" || op === "mul" || op === "div" || op === "mod" || op === "pow" || op === "intdiv" || op ==="pythag") {
        let num1 = parseFloat(document.getElementById("num1").value);
        let num2 = parseFloat(document.getElementById("num2").value);
        const url = `http://192.168.12.161:5000/${op}?num1=${num1}&num2=${num2}`;
        
        try {
            let res = await axios.get(url);
            let data = res.data;
            document.getElementById("system_response").innerHTML = "Result: " +  data.result;
        } catch (err) {
            document.getElementById("system_response").innerHTML = "Error: " + err;
        }
    } else {
        document.getElementById("system_response").innerHTML = "Invalid operation!";
    }
};

const sayHello = async () => {
    try {
        let res = await axios.get("http://192.168.12.161:5000/hello")
        let data = res.data
        document.getElementById("system_response").innerHTML = data.message;
    } catch (err) {
        document.getElementById("system_response").innerHTML = "Error: " + err;
    }
}