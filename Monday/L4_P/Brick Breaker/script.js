// Getting canvas element
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// Setting up canvas height
canvas.width = 480;
canvas.height = 320;

// setting up ball
const ball = {
  radius: 10,
  x: canvas.width / 2,
  y: canvas.height - 30,
  dx: 2,
  dy: -2
};

// setting up paddle
let paddle = {
  width: 75,
  height: 10,
  x: 0,
  y: 0
};

paddle.x = (canvas.width - paddle.width) / 2;
paddle.y = canvas.height - paddle.height;

// setting up key listeners
let rightPressed = false;
let leftPressed = false;

// handle key presses
function keyDownHandler(e) {
  if (e.keyCode == 39) {
    rightPressed = true;
  } else if (e.keyCode == 37) {
    leftPressed = true;
  }
}

function keyUpHandler(e) {
  console.log(e)
  if (e.keyCode == 39) {
    rightPressed = false;
  } else if (e.keyCode == 37) {
    leftPressed = false;
  }
}

document.addEventListener("keydown", keyDownHandler);
document.addEventListener("keyup", keyUpHandler);

// Draw circle
function drawBall() {
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
  ctx.fillStyle = "red";
  ctx.fill();
  ctx.closePath();

  // now paddle!
}

// draw paddle
function drawPaddle() {
  ctx.beginPath();
  ctx.rect(paddle.x, paddle.y, paddle.width, paddle.height);
  ctx.fillStyle = "green";
  ctx.fill();
  ctx.closePath;
}

// was formerly called moveBall
function movement() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawPaddle();
  drawBall();
  ball.x += ball.dx;
  ball.y += ball.dy; 

  // bounce off edges
  if (ball.x + ball.dx > canvas.width - ball.radius || ball.x + ball.dx < ball.radius) {
    ball.dx *= -1;
  }
  if (ball.y + ball.dy > canvas.height - ball.radius || ball.y + ball.dy < ball.radius) {
    ball.dy *= -1;
  }

  // now check paddle && paddle.x > 0
  // update paddle && paddle.x < canvas.width - paddle.width
  if (rightPressed) {
    paddle.x += 7;
    console.log("right");
  } else if (leftPressed) {
    paddle.x -= 7;
    console.log("left");
  }
}

// Call function every 10 ms
setInterval(movement, 10);