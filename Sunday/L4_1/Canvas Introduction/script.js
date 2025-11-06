// 1) Draw a line

var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.moveTo(0, 0);
ctx.lineTo(200, 100);
ctx.stroke();

// 2) Draw a shape (rectangle, circle)
// 3) Create a function that draws your shape
// in a specific location
// EXAMPLE:
// drawCircle(200, 200) --> draws a circle at x 200, y 200
// Our end objective with today is to make some art, so once youve finished
// these three be as creative as you'd like?