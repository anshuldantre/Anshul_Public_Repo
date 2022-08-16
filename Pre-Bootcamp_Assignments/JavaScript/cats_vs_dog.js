console.log("in");

var imag = document.querySelector("#image");
var h1 = document.querySelector("h1");

console.log(imag);

function catImg (element) {
    // console.log (imag.src);
    imag.src = "cat.jpeg";
    h1.innerText = "Cat Wins !";
    console.log(element);
    // element.remove();
    
    element.style.backgroundColor = "black";
    element.style.color = "#fff";

}

function dogImg (element) {
    // console.log (imag.src);
    imag.src = "dog.jpeg";
    h1.innerText = "Dog Wins !";
    console.log(element);
    element.classList.add("butn");
}

function setActive(element) {
    if (element.classList.contains("dark-mode") ) {
        element.innerText = "Switch to light Mode"
        element.ClassList.remove("dark-mode");
    }
    else {
        element.innerText = "Switch to dark Mode"
        element.ClassList.add("dark-mode");
    }
}