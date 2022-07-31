var childHeight = 53;

function displayIfChildIsAbleToRideTheRollerCoaster(num1) {
    
    console.log('Kid height provided ' + num1);
    console.log(num1);
    if (num1 > 52) {
        console.log('Get on that ride, kiddo!');
    } else {
        console.log('Sorry kiddo. Maybe next year.');
    }
}

displayIfChildIsAbleToRideTheRollerCoaster(childHeight);