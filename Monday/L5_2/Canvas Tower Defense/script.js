// 2) Draw a circle to your canvas
const myCanvas = document.getElementById("myCanvas");
const ctx = myCanvas.getContext("2d");

ctx.beginPath();
ctx.arc(96, 50, 40, 0, 2*Math.PI);
ctx.fillStyle = "orange";
ctx.fill();
ctx.lineWidth = 4;
ctx.strokeStyle = "black";
ctx.stroke();

// Working: made a circle
// to work on: start making the background with the paths

// 3) Create a function that draws the outline of your
// tower defence, including a path for your enemies to travel 
// along and any background things.

// 4) Create an object constructor for an Enemy. It 
// should include the following:
// properties for: x, y
// method for: drawing it to the canvas
// MAKE SURE TO TEST!