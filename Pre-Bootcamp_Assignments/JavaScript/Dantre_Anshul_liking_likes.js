console.log("In");

var count1 = 9;
var count2 = 12; 
var count3 = 9; 
var user1LikesCounter = document.querySelector("#txt1");
var user2LikesCounter = document.querySelector("#txt2");
var user3LikesCounter = document.querySelector("#txt3");

console.log(userLikesCounter);

function incrementLike1() {
    count1++;
    user1LikesCounter.innerText = count1 + ' like(s)';
}

function incrementLike2() {
    count2++;
    user2LikesCounter.innerText = count2 + ' like(s)';
}

function incrementLike3() {
    count3++;
    user3LikesCounter.innerText = count3+ ' like(s)';
}