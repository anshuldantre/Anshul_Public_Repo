function displayContactInfo ()
{
    var auntContactInfo = ["Paula","Smith","1234 ain Street", "St. Louis", "MO", 12345];
    console.log(auntContactInfo);
}
displayContactInfo();

function displayGrocerylist() {
    var produce = ["apples", "oranges"];
    var frozen = ["broccoli", "ice cream"];
    frozen.push("hashbrowns");
    console.log(frozen);
}
displayGrocerylist();

var movieLibrary = ["Bambi", "E.T.", "Toy Story"];
movieLibrary.push("Zoro");
movieLibrary[1] = "Beetlejuice";
console.log(movieLibrary);