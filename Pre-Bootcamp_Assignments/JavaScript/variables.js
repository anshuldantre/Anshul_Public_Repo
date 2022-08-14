// var count=5;
// var message = "hello world";
// var likesJS = true;

// count = 'Variable changed from number to string'

// console.log(count)
// console.log(message)
// console.log(likesJS)

// console.log(5+3.54141611)
// console.log ('The addition of 5 and 3 is ' + 5+3)

// var total = 10
// total *= 5;
// console.log(total)

// function addition(num1, num2) {
    // var num1 = 5;
    // var num2 = 4;
    // var num3 = num1 + num2;
    // console.log(num3)

//     return num1+num2;

// }

// var z = addition(5,8);
// console.log(z);


function createArray(num) {
    var newArrary = []
    for (var i=0; i<=num; i++) {
        newArrary.push(i);
    }
    return newArrary;
}

var z = createArray(5);
console.log(z);
