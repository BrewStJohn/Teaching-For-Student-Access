const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
const balls = [];

// 1: Draw a ball onto the canvas.
ctx.beginPath();
ctx.arc(95, 50, 10, 0, 2 * Math.PI)
ctx.fillStyle = "black";
ctx.fill();
ctx.closePath();

// 2) Next, we are going to setup the factory line
// for creating multiple balls at a time
function buildBalls(number){
    // 2a): Create ball objects (for however many balls you want to make) 
    // that store the following properties:
    // x coordiante, y coordiante, x speed, y speed, size, colour
    // ^^^ store all of these balls in an array called 'balls'
    for (let i = 0; i < number; i++){
        const ball = {
            x: 10,// random number
            y: 10,// random number
            x_speed: 2,// random number
            y_speed: 2,// random number
            size: 10,
            color: "black"
        }
        balls.push(ball);
    }
}
// TO TEST: call build balls and look at the balls array. Does it have stuff in it?
buildBalls(10);
console.log(balls);


// 3) Create a function called 'drawObject' that takes in
// a ball as a parameter and draws it to its x and y coordinate on
// your canvas

// 4) For each ball object, move it along the screen based on its x
// y speeds using the SetInterval window method