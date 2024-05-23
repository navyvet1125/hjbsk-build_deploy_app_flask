// Description: This script is used to make a request to the server to perform an operation

const OPS_OPTIONS = ["sum", "sub", "mul", "div", "mod", "pow", "intdiv", "pythag"];


const runOperation = async (op) => {
    if (OPS_OPTIONS.includes(op)) {
        let num1 = parseFloat($("#num1").val());
        let num2 = parseFloat($("#num2").val());
        const url = `http://192.168.12.161:5000/${op}?num1=${num1}&num2=${num2}`;
        
        try {
            let res = await axios.get(url);
            let result = res.data.result;
            $("#system_response").append(`<li>Result: ${result} </li>`);
        } catch (err) {
            let result = err.response.data.result;
            $("#system_response").append(`<li class='alert alert-danger'>Error: ${result} </li>`);
        }
    } else {
        $("#system_response").append("<li class='alert alert-danger'> Invalid operation! </li>");
    }
    $("#clearButton").show();
};

const sayHello = async () => {
    try {
        let res = await axios.get("http://192.168.12.161:5000/hello")
        let data = res.data
        $("#system_response").append(`<li> ${data.message} </li>`);
    } catch (err) {
        $("#system_response").append(`<li>Error: ${err} </li>`);
    }
    $("#clearButton").show();
}

// Clear system response
const clearResponse = () => {
    $("#system_response").html("");
    $("#clearButton").hide();
}