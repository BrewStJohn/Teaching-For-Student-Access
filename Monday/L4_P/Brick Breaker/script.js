// What comes next?
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");


ctx.beginPath();
ctx.arc(100, 100, 20, 0, Math.PI * 2);
ctx.fillStyle = "red";
ctx.fill();
ctx.closePath();






function draw(){
    console.log("drawing...")
}

function update(){
    console.log("updating")
}

function erase(){
    console.log("erase")
}

// function main(){
//     draw()
//     update()
//     erase()
// }

// main()
// main()
// main()
// main()
// main()

draw()
update()
erase()
draw()
update()
erase()
draw()
update()
erase()
draw()
update()
erase()
draw()
update()
erase()
draw()
update()
erase()
draw()
update()
erase()
draw()
update()
erase()