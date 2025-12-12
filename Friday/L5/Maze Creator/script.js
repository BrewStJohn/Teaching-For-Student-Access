console.log("test");

// 2) Draw a square to the canvas. This should be 
// what you want your point to look like
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// 3) Create an object constructor for a Point.
// It should contain the following:
// --> Two parameters for where you want the point
// to exist on the canvas (x and y)
function Point(x, y){
    // Properties: its x and y coordinates
    this.x = x;
    this.y = y;
    // Method: Draw
    this.draw = function(){
        ctx.fillStyle = "red";
        ctx.fillRect(this.x, this.y, 5, 5);
    }
}
// TO TEST: Create a point with your object constructor
// and draw it to the canvas

const testPoint = new Point(400, 400);
testPoint.draw()
const testPoint2 = new Point(300, 300);
testPoint2.draw()
const testPoint3 = new Point(500, 500);
testPoint3.draw()
// testPoint.x = 100;
// testPoint.y = 100;
// testPoint.draw();

// CHALLENGE: Make 1 row of points, 
// from end to end on the canvas
// HINT: Create an array, put the points in the array,
// then for every point in the array, call its draw method

// 4) Create a method called 'initialise' that fills the
// board with Points. All the points should be stored in a
// 2D Array called 'grid'