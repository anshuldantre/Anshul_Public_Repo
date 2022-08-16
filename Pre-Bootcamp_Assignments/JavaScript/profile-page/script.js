console.log("page loaded...");

var totalConnections = document.querySelector("#totalconns");
var newConnRequest = document.querySelector("#connreq");
var username = document.querySelector("#username");


function replaceName(element) {
    username.innerText = "Changed Name";
}

function accept(id) {
    var element = document.querySelector(id);
    element.remove();
    totalConnections.innerText++;
    newConnRequest.innerText--;
}

function ignore(id) {
    var element = document.querySelector(id);
    element.remove();
    newConnRequest.innerText--;
}
