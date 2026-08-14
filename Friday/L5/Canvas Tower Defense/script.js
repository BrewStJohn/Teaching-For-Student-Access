// 2) Draw the stationary elements 
// using the canvas
let canvas = document.getElementById("game");
let ctx = canvas.getContext("2d");

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

function updateGame(){
    drawTrack();
}

setInterval(updateGame,30);

// 3) Create a class/object constructor 
// for a Ball

// CALCULATING SPEED (diagonal paths):
// 1) Where are we starting, where are we ending
// --> have a 2D Array filled with coordinates of 
// where the enemies will make turns
// 2) Find length of vector (find the value of c)
// 3) Find unit vector (distance between points --> x2 - x1
// divided by length of the vector)
// 4) Multiply by how fast you want it to go (speed)
