var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
canvas.width = 400;
canvas.height = 400;

var centerX = canvas.width / 2;
var centerY = canvas.height / 2;
var numberOfLines = 225;
var colors = ['#000000','#080808','#101010','#181818','#202020','#282828','#303030','#383838','#404040','#484848','#505050','#585858','#606060','#686868','#707070','#787878','#808080','#888888','#909090','#989898','#A0A0A0','#A8A8A8','#B0B0B0','#B8B8B8','#C0C0C0','#C8C8C8','#D0D0D0 ','#D8D8D8','#E0E0E0','#E8E8E8','#F0F0F0','#F8F8F8','#FFFFFF'];
for(var i = 0; i < numberOfLines; i++)
{
  drawLine(getRandomInt(1,canvas.width), getRandomInt(1,canvas.height),getRandomInt(1,canvas.width),getRandomInt(1,canvas.height), colors[getRandomInt(0,colors.length-1)], 2);
}

// Drawing Functions
// Draw line function
function drawLine(startX, startY, endX, endY, color, lineWidth) {
  if (color === undefined) {
    color = "black";
  }
  if (lineWidth === undefined) {
    lineWidth = 10;
  }
  ctx.beginPath();
  ctx.moveTo(endX, endY);
  ctx.lineTo(startX, startY);
  ctx.strokeStyle = color;
  ctx.lineWidth = lineWidth;
  ctx.stroke();
}

// Function to draw a rectangle
function drawRect(startX, startY, width, height, color, lineWidth, lineColor) {
  if (lineColor === undefined) {
    lineColor = "black";
  }
  if (lineWidth === undefined) {
    lineWidth = 10;
  }
  ctx.beginPath();
  ctx.rect(startX, startY, width, height);
  ctx.strokeStyle = lineColor;
  ctx.fillStyle = color;
  ctx.lineWidth = lineWidth;
  ctx.fill();
  ctx.stroke();
}

// Function to draw a circle
function drawCircle(centerX, centerY, radius, color) {
  ctx.beginPath();
  ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = 1;
  ctx.fill();
  ctx.stroke();
}

/*
Helper method to generate a random integer 
*/
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}