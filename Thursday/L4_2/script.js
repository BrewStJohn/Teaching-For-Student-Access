const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

const ball = {
    dx : 0.5,
    dy : 0.5 ,
    x : 61,
    y : 61,
    size : 60,
    dx2 : 1,
    dy2 : 1 ,
    x2: 45,
    y2 : 45,
    size2 : 30
}




function color(){
    ctx.fillStyle = "red";

    console.log("hi");
    
ctx.beginPath();
ctx.arc(ball.x,ball.y,ball.size,0,2*Math.PI);
ctx.stroke();

ctx.beginPath();
ctx.arc(ball.x2,ball.y2,ball.size2,0,2*Math.PI);
ctx.stroke();

}

function drawing(){
    update();
    
    ctx.clearRect(1,1,5000,5000)
    color();
   
    

}

function update(){
    ball.x += ball.dx
    ball.y += ball.dy
    ball.x2 += ball.dx2
    ball.y2 += ball.dy2

    if(ball.x + ball.size == canvas.width){
        ball.dx *= -1;
    }
    if(ball.x2 + ball.size2 == canvas.width){
        ball.dx2 *= -1;
    }
    if(ball.x - ball.size == 0){
        ball.dx *= -1;
    }
    if(ball.x2 - ball.size2 == 0){
        ball.dx2 *= -1;
    }
    if(ball.y - ball.size == 0){
        ball.dy *= -1;
    }
    if(ball.y2 - ball.size2 == 0){
        ball.dy2 *= -1;
    }
    if(ball.y + ball.size == canvas.height){
        ball.dy *= -1;
    }
    if(ball.y2 + ball.size2 == canvas.height){
        ball.dy2 *= -1;
    }
}


setInterval(drawing, 1);


