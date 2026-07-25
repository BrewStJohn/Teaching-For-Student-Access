// 0) How do you access the cells of the table
// in Javascript? Save 1 row of cells into an array.
console.log(document.getElementById("myTable").rows[0].cells[0])
grid = []

for (row = 0; row < 5; row++){
    grid[row] = [];
    for (col=0; col < 5; col++){
        grid[row][col] = document.getElementById("myTable").rows[row].cells[col]
    }
}

console.log(grid)

// 1) When you click on a cell, write to the console 
// b) what row its on and what column its on
// HINT: 2D Arrays, DOM

// 2) What functions will we need to write?
// - Make the squares clickable
// --> when the squares are left clicked, 
// displaying the correct number of mines nearby
// --> When right clicked, create a note 
// that says a mine is there
// --> Place mines randomly on squares



