document.addEventListener('DOMContentLoaded', domloaded, false);
function domloaded() {
    function fizzBuzz() {
        out_array = [];
        out = "";

        for (i = 1; i <= 100; i++) {
            out = "";
            if (i % 3 == 0) {
                out += "fizz";
            }
            if (i % 5 == 0) {
                out += "buzz";
            }
            if (out == "") {
                out = i   
            }
            out_array.push(out);
        }

        table = document.createElement("table");
        for (i = 0; i < out_array.length; i++) {
            if (i % 10 == 0) {
                row = table.insertRow();
            }
            cell = row.insertCell();
            cell.innerHTML = out_array[i];
            
        }
        document.getElementById("FizzBuzz").appendChild(table)
    }

    fizzBuzz();
}