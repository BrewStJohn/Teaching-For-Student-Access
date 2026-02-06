// Set up canvas
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
canvas.width = 480;
canvas.height = 320;

// Getting elements
var scoreText = document.getElementById("score");
var livesText = document.getElementById("lives");
var restartButton = document.getElementById("restart");
restartButton.onclick = initialize;

// Setting up global variables
var ball = {
  radius: 10,
  x: canvas.width / 2,
  y: canvas.height - 50,
  speed: 5,
  dx: 3,
  dy: -4
};

var paddle = {
  width: 75,
  height: 10,
  x: 0,
  y: 0
};

var bricks = [];
var rowCount = 3;
var colCount = 6;
var offsetTop = 30;
var offsetLeft = 15;
var lives;
var score;
var numBricks;

// Set up key listeners
var rightPressed = false;
var leftPressed = false;
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

// Call function to update game every 30 ms
initialize();
setInterval(updateGame, 30);

// Function to setup starting parameters
function initialize() {
  // Set up lives and score
  lives = 3;
  livesText.innerHTML = lives;
  score = 0;
  scoreText.innerHTML = score;
  numBricks = 0;

  // Set up ball and paddle
  reset();

  // Set up bricks
  var colors = ["red", "orange", "lime"]
  for (var c = 0; c < colCount; c++) {
    bricks[c] = []
    for (var r = 0; r < rowCount; r++) {
      var brick = {
        width: 70,
        height: 20,
        padding: 5,
        x: 0,
        y: 0,
        color: colors[r],
        status: 1
      };
      bricks[c][r] = brick;
      numBricks += 1;
    }
  }
}

// Draw ball
function drawBall() {
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
  ctx.fillStyle = "white";
  ctx.fill();
  ctx.closePath();
}

// draw paddle
function drawPaddle() {
  ctx.beginPath();
  ctx.rect(paddle.x, paddle.y, paddle.width, paddle.height);
  ctx.fillStyle = "blue";
  ctx.fill();
  ctx.closePath;
}

// draw bricks
function drawBricks() {
  for (var c = 0; c < colCount; c++) {
    for (var r = 0; r < rowCount; r++) {
      var brick = bricks[c][r];
      if (brick.status == 1) {
        brick.x = (c * (brick.width + brick.padding)) + offsetLeft;
        brick.y = (r * (brick.height + brick.padding)) + offsetTop;

        ctx.beginPath();
        ctx.rect(brick.x, brick.y, brick.width, brick.height);
        ctx.fillStyle = brick.color;
        ctx.fill();
        ctx.closePath();
      }
    }
  }
}

// detect if ball hit brick
function collision() {
  for (var c = 0; c < colCount; c++) {
    for (var r = 0; r < rowCount; r++) {
      var brick = bricks[c][r];
      if (brick.status == 1) {
        if (ball.x + ball.radius > brick.x && ball.x - ball.radius < brick.x + brick.width && ball.y + ball.radius > brick.y && ball.y - ball.radius < brick.y + brick.height) {
          ball.dy *= -1;
          brick.status = 0;
          score += 1;
          scoreText.innerHTML = score;
          numBricks -= 1;
          if (numBricks == 0) {
            alert("You Won!");
            ball.dx = 0;
            ball.dy = 0;
          }
        }
      }
    }
  }
}

// reset ball and paddle position
function reset() {
  ball.x = canvas.width / 2;
  ball.y = canvas.height - 50;
  ball.dx = 3;
  ball.dy = -4;

  paddle.x = (canvas.width - paddle.width) / 2;
  paddle.y = canvas.height - paddle.height * 2;
}

// handle key presses
function keyDownHandler(e) {
  if (e.keyCode == 39) {
    rightPressed = true;
  } else if (e.keyCode == 37) {
    leftPressed = true;
  }
}

function keyUpHandler(e) {
  if (e.keyCode == 39) {
    rightPressed = false;
  } else if (e.keyCode == 37) {
    leftPressed = false;
  }
}

// Update screen to reflect state of game.
function updateGame() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawBricks();
  drawBall();
  drawPaddle();

  // bounce off edges and paddles
  if (ball.x + ball.dx > canvas.width - ball.radius 
      || ball.x + ball.dx < ball.radius) {
    ball.dx *= -1;
  }
  if (ball.y + ball.dy < ball.radius) {
    ball.dy *= -1;
  } else if (ball.y + ball.dy > paddle.y - ball.radius) {
    if (ball.x + ball.radius > paddle.x 
        && ball.x - ball.radius < paddle.x + paddle.width) {
      // calculate angle of ball from where it hits the paddle
      var angle = (Math.PI / 2) * 
          (paddle.x + (paddle.width / 2) - ball.x) / (paddle.width / 2);
      ball.dx = -1 * (Math.sin(angle) * ball.speed);
      ball.dy = -1 * (Math.cos(angle) + ball.speed);
    } else {
      lives -= 1;
      livesText.innerHTML = lives;
      reset();
      if (lives < 1) {
        alert("Game Over!")
        ball.dx = 0;
        ball.dy = 0
      }
    }
  }

  // update paddle
  if (rightPressed && paddle.x < canvas.width - paddle.width) {
    paddle.x += 7;
  } else if (leftPressed && paddle.x > 0) {
    paddle.x -= 7;
  }

  // update ball position
  ball.x += ball.dx;
  ball.y += ball.dy;

  // check for collisions
  collision();
}