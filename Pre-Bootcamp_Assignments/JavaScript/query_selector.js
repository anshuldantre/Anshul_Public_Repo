console.log("We are IN");

var count = 1;
var countElement = document.querySelector("h1");

console.log(countElement);

function add1() {
    count++;
    countElement.innerText = "The running counter is " + count;

}

function minus1() {
    count--;
    countElement.innerText = "The running counter is " + count;
}