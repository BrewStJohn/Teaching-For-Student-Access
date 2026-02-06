// Getting canvas element
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

const change_x = Math.floor(Math.random()*10)-5;
const change_y = Math.floor(Math.random()*10)-5;

let x = 50;
let y = 50;
const size = 10;

function ballMove(){
    ctx.clearRect(0,0,500,500)
    x -= change_x;
    y -= change_y;
    ctx.beginPath();
    ctx.arc(x, y, size, 0, Math.PI * 2);
    ctx.fillStyle = "red";
    ctx.fill();
    ctx.closePath();
}

setInterval(ballMove, 10);

// TASK: Get your ball to bounce
// NEED TO ACCOUNT FOR THE BALLS SIZE
// if ball touching top or bottom border 
    // reverse y speed
// if ball touching left or right border
    // reverse x speed