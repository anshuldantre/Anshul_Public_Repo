console.log("we are in");

function removeButton (element) {
    element.remove();
}

function changeText(element) {
    if (element.innerText == "LOGIN") 
    {
        element.innerText = "LOGOUT"
    }
    else {
        element.innerText = "LOGIN"
    }
}

function alertMsg () {
    alert("Ninja was liked");
}