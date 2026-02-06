const canvas = document.getElementById("myCanvas");
const canvasLeft = canvas.offsetLeft + canvas.clientLeft;
const canvasTop = canvas.offsetTop + canvas.clientTop;
const ctx = canvas.getContext("2d");
const balls = [];
let explosion = {};

// 1: Draw a ball onto the canvas.
// IVE MOVED THIS CODE, YOULL HAVE TO START YOURSELF

// 2) Next, we are going to setup the factory line
// for creating multiple balls at a time
function buildBalls(number){
    // 2a): Create ball objects (for however many balls you want to make) 
    // that store the following properties:
    // x coordiante, y coordiante, x speed, y speed, size, colour
    // ^^^ store all of these balls in an array called 'balls'
    for (let i = 0; i < number; i++){
        const ball = {
            x: Math.floor(Math.random()* canvas.width),
            y: Math.floor(Math.random()* canvas.height),
            x_speed: 2,// random number
            y_speed: 2,// random number
            size: 10,
            color: "black"
        }
        balls.push(ball);
    }
}
// TO TEST: call build balls and look at the balls array. 
// Does it have stuff in it?
buildBalls(10);
// console.log(balls);

// 3) Create a function called 'drawObject' that takes in
// a ball as a parameter 
// and draws it to its x and y coordinate on your canvas

// create function draw object with parameter ball
function drawObject(ball){
// --> The parameter ball is one of those balls i made in build balls 
    // console.log(ball);
    // take the steps from part 1 and draw the ball to the screen
    // HOWEVER: when I make a ball, its x and y coordinates need
    // to change! How do I do that? I take a look at the parameter
    // ball. It has x and y coordinates!
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, 10, 0, 2 * Math.PI)
    ctx.fillStyle = "black";
    ctx.fill();
    ctx.closePath();
}

// 4) Create a function called 'drawBalls' that
// For every ball in the balls array, draw that ball 
// to the screen
function drawBalls(){
    // need to access the balls inside of the balls,
    // specifically their x and y coordinates
    
    for (let i = 0; i < balls.length; i++){
        updateBall(balls[i]);
        drawObject(balls[i]);
    }
}

function drawExplosion(){
    
}

function gameLoop(){
    ctx.clearRect(0,0,canvas.width, canvas.height);

    drawBalls();
    drawExplosion();
}

// 5) For each ball object, move it along the screen based 
// on its x y speeds using the SetInterval window method

function updateBall(ball){
    ball.x += ball.x_speed;
    ball.y += ball.y_speed;
    // NEXT: REFLECT OFF WALLS!
}

setInterval(gameLoop, 1000);

// 6) Print to the console the coordinates on the canvas
// of wherever you clicked. THIS IS GONNA BE HARD,
// You will need to investigate more than just w3schools.
// HINTS: MouseEvents, Events, onclick,
// offSetLeft & offSetRight. Maybe a good quality
// google search will have your answer.

canvas.addEventListener('click', function(event){
    let x = event.pageX - canvasLeft;
    let y = event.pageY - canvasTop;

    console.log(x, y);
    explosion.x = x;
    explosion.y = y;

    // NEXT: Create a circle where you click. Have it expand
    // slowly over time.
});