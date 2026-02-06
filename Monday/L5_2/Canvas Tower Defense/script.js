// 2) Draw a circle to your canvas

// Working: made a circle
// to work on: start making the background with the paths
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

let testEnemy = new Enemy(20, 120);


// 6) Create some helper functions
// for calculating distance and speed vectors

// a) Create a function called 'getDistance'
// that takes in four parameters: x1, y1, x2, y2
// and returns the distance between x1, y1 and
// x2, y2

// i.e. getDistance(50, 50, 150, 150)
// == sqrt((150-50)^2 + (150-50)^2)

// 3) Create a function that draws the outline of your
// tower defence, including a path for your enemies to travel 
// along and any background things.
function drawTrack(){
    // Create background
    ctx.fillStyle ="green";
    ctx.fillRect(0,0,canvas.width,canvas.height);
    // Create track
    ctx.fillStyle ="brown";
    ctx.fillRect(0,100,200,40);
    ctx.fillRect(200,100,40,340);
    ctx.fillRect(200,400,175,40);
    ctx.fillRect(375,100,40,340);
    ctx.fillRect(375,100,250,40);
}

// 4) Create an object constructor for an Enemy. It 
// should include the following:
// properties for: x, y, dx, dy
// methods for: 
// a) drawing it to the canvas 
// b) updating its position on the canvas
// MAKE SURE TO TEST!

function Enemy(x, y){
    this.x = x;
    this.y = y;
    this.dx = 2;
    this.dy = -2;
    this.draw = function(){
        ctx.beginPath();
        ctx.arc(this.x, this.y, 10, 0, 2*Math.PI);
        ctx.fillStyle = "orange";
        ctx.fill();
        ctx.lineWidth = 1;
        ctx.strokeStyle = "black";
        ctx.stroke();
        ctx.closePath();
    };
    this.updatePosition = function(){
        this.draw();
        this.x += this.dx;
        this.y += this.dy;
    };
}


setInterval(updateGame, 100);

// This function updateGame is how the drawing actually works.
// I: draw the track, draw my enemy, and repeat.
function updateGame(){
    drawTrack();
    testEnemy.updatePosition();
}

// BONUS: Create a function called 'Create enemies'
// that generates a new enemy to go on the track.
// Store that enemy in an array called 'enemies'
// BE SURE TO CALL THIS FUNCTION IN UPDATEGAME

// How can you create enemies on an interval?
// --> set interval
// --> put them in an array

// How do I draw all the enemies I wanna make? 
// for every enemy in our array, draw that enemy

// How would I store that information?
// --> in an array

