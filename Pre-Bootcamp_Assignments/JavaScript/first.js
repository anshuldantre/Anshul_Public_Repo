var z

function myfunction(question) {
    if (question === 'Addition')
    return 'a+b'
    else if (question === 'Substraction')
    return 'a-b'
    else if (question === 'Multiplication')
    return 'a*b'
    else (question === 'Division')
    return 'a/b'
}

z = myfunction ('Substraction');
console.log(z);

var name=["Anshul", "shradha", "Rosesh"]

function myfunction(array) {
    for (i=0;i<array.length;i++)
    {
    console.log(i)
    console.log(array[i])
    }
}

myfunction(name)
