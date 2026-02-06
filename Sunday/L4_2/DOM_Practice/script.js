var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");

ctx.fillRect(10,10,150,100);

// Detect when the user press the right, left up or down
// arrow keys. When they press these keys, print out which
// key they pressed in the console.

document.addEventListener("keydown", function(event){
    console.log("hi");
});