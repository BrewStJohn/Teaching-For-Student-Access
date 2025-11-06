const columns = 8;
const rows = 8;


$(document).ready(function(){
    console.log("test");

    function init(){
        for (let j = 0; j < rows; j++){
            for (let i = 0; i < columns; i++){
                if((i+j) % 2 == 0){ 
                    $("#board").append("<div class='white square'></div>");   
                }else{
                    id = j + "_" + i;
                    console.log("#"+id);
                    $("#board").append("<div class='red square' id="+id+"></div>");
                    if (j < 3){
                        $("#"+id).append("<div class='white piece'></div>");
                    } 
                    else if (j >= rows-3){
                        $("#"+id).append("<div class='black piece'></div>");
                    }
                }
            }
        }
    }

    init();
    // TASK: Setup the board!
    // a) When the user clicks the start game button, fill in the board.
    // HINTS: jQuery events
    // b) Hide the start game button
    // HINT: jQuery Hide
    // c) Create a text the shows which players turn it is
    // HINT: jQuery Add

    // TASK 2: When you click on a piece, print something to the console.
    
})