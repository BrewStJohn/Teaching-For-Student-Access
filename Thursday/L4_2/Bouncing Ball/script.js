// 0) CHALLENGE: Print to the console 1. Then after one second, 
// print to the console the number 2. 
// Continue this for 1 minute. HINT: Interval

const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
console.log("testing..")
// 05/21

// 1) Create a function that, when called, draws
// a circle to the screen. 
// CHALLENGE: give this function a parameter for colour.
// draw different coloured balls.

// 2) Create an object called 'ball' with the following 
// properties:
// a) dx and dy (speed)
// b) x and y coordinates
// c) size
// d) color
// CHALLENGE: Create multiple different balls and draw
// them to the canvas.

const ball = {
    dx:0.5,
    dy:0.25,
    x:50,
    y:50,
    size:20
}

function circle(){
    // make a circle
    ctx.beginPath();
    ctx.arc(ball.x,ball.y,ball.size,0,2*Math.PI);
    ctx.stroke();
}

function drawing(){
    update();
    // clear off the board
    ctx.clearRect(0,0, canvas.width, canvas.height);
    circle();
}

function update(){
    // Why is there this visual issue?
    ball.x += ball.dx;
    ball.y += ball.dy;
    // TASK: Make the ball bounce off the sides
    // HINT: canvas.height, canvas.width, if
    
    // a) how can I detect if the ball is at an edge?
    
    // if ball is on right edge:
    if (ball.x + ball.size == canvas.width){
        // change speed
        ball.dx *= -1;
    }
    
    // if ball is on left edge
        // change speed
    
    // if ball is on bottom edge
        // change speed
    
    // if ball is on top edge
        // change speed
}

setInterval(drawing, 10);

