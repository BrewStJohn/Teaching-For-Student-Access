// 2) Draw a square to the canvas. This should be 
// what you want your point to look like
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
const grid = [];
const paths = [];
const ptsStack = [];

initialise();
setInterval(drawMaze, 10);

// 3) Create an object constructor for a Point.
// It should contain the following:
// --> Two parameters for where you want the point
// to exist on the canvas (x and y)
function Point(x, y){
    // Properties: its x and y coordinates
    this.x = x;
    this.y = y;
    this.visited = false;

    this.drawX = (x+1) * 10;
    this.drawY = (y+1) * 10;
    this.neighbours = [];

    this.checkUnvisited = function(){
        // for all of our neighors in our neighbors list
            // if one of them is visited
                // remove it from the list

        // select a random unvisited neighbor (if there is any)
        // if there is no random unvisited neighbor, return false
    }

    // Method: Draw
    this.draw = function(){
        ctx.fillStyle = "red";
        ctx.fillRect(this.drawX-2, this.drawY-2, 5, 5);
    }
}

// 4) Create a method called 'initialise' that fills the
// board with Points. All the points should be stored in a
// 2D Array called 'grid'
function initialise(){
    for (let i = 0; i < 60; i++){
        const row = [];
        for (let j = 0; j < 60; j++){
            let newPoint = new Point(j,i);
            newPoint.draw();

            // 4b) Give your points a neighbours property, which
            // will be an array of points that are its neighbours.
            // Then, inside of initialise, give every point a neighbour
            // When theyre made.

            if (j > 0){
                newPoint.neighbours.push(row[j-1]);
                row[j-1].neighbours.push(newPoint);
            }

            if (i > 0){
                newPoint.neighbours.push(grid[i-1][j]);
                grid[i-1][j].neighbours.push(newPoint);
            }

            // console.log(newPoint);
            row.push(newPoint);
        }
        // console.log(row);
        grid.push(row);
    }
    // console.log(grid);

    let random_choice_row = Math.floor(Math.random()*60)
    let random_choice_column = Math.floor(Math.random()*60)

    // add random point to pointStack
    ptsStack.push(grid[random_choice_row][random_choice_column]);
}

// 5) Create an object constructor for a Path 
// (white rectangle between points). It should have
// a property deciding whether it is vertical or horizontal.
function Path(p1, p2, color){
  this.p1 = p1;
  this.p2 = p2;
  
  this.vertical = p1.drawX == p2.drawX;
  
  this.color = color
  this.draw = function(){
    ctx.strokeStyle = this.color;
    ctx.lineWidth = 4;
    ctx.beginPath();
    if (this.vertical){
      // how can we draw this better?
      // this code makes the corners look nice :)
      ctx.moveTo(p1.drawX,Math.min(p1.drawY,p2.drawY)-2);
      ctx.lineTo(p2.drawX,Math.max(p1.drawY,p2.drawY)+2);
    }
    else{
      ctx.moveTo(p1.drawX, p1.drawY);
      ctx.lineTo(p2.drawX, p2.drawY);
    }
    // how can we make our path look nicer on the corners?
    
    ctx.stroke();
    ctx.closePath();
  }
}

function drawMaze(){
    let curr = ptsStack[0];
    // FUTURE: change from curr.neighbours[0] to curr.getUnvisited()
    let next_point = curr.neighbours[Math.floor(Math.random()*4)];
    // drew path
    let newPath = new Path(curr, next_point, "black");
    newPath.draw();
    ptsStack.splice(0,0,next_point);
}

// testPath = new Path(grid[0][0], grid[0][1], "black");
// testPath.draw();

// DRAWING THE MAZE:
// LAST TIME WE DISCUSSED:
// At the beginning:
// 1) Select a random point to start
// 2) select a random neighbor from that point
// 3) draw a path to it 
// repeat 2 - 3

// will this work? What are some potential 
// shortfalls? Consider our program so far.

// --> consider overlaps (we are not keeping
// track of where we have made paths to so far,
// as a result, paths can be drawn back ontop 
// of places paths have already been made).

// run into deadend OR edge of the map
// --> if we have run out of neighbours that we 
// can draw paths to, draw paths to neighbours 
// who have not had paths drawn to them
// --> then, we should go back in time (?)

// Stack WILL CONTAIN POINTS
// How do I draw my paths?
// place path in paths array and draw all the paths