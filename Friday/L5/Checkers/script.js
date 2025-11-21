const columns = 8;
const rows = 8;

$(document).ready(function(){
    // console.log("test");
    let parent;
    let selected;
    let pid;
    const options = [];
    function init(){
        for (let j = 0; j < rows; j++){
            for (let i = 0; i < columns; i++){
                if((i+j) % 2 == 0){ 
                    $("#board").append("<div class='white square'></div>");   
                }else{
                    id = j + "_" + i;
                    // console.log("#"+id);
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

    $(".white.piece").click(function(){
        // console.log("clicked on a white piece");
        optionHelper(this);
    });

    $(".black.piece").click(function(){
        // console.log("clicked on a black piece");
        optionHelper(this);
    });

    function clearOptions(){
        for (let i = options.length -1; i >= 0; i--){
            options[i].css("background-color", "red");
            options.splice(i, 1);
        }
    }

    function getOptions(color, row, col){
        // we are figuring out which squares we want to make highlighted to show as options
        // to the player.
        
        // create a variable to store the squares you wil highlight (options)
        // if the color is black (black piece),
            // add to options the two pieces. Selected these pieces with jQuery
        // if the color is white (white piece),
            // add to options the two pieces. Selected these pieces with jQuery

        // for every option in your list
            // make its background colour yellow
    }

    function optionHelper(clickedPiece){
        selected = clickedPiece; // we'll return to this later
        clearOptions();
        parent = selected.parent(); // this gets the square the piece is on
        pid = parent.attr("id").split("_");
        getOptions(selected.css("background-color"), parseInt(pid[0]), ParseInt(pid[1]));
    }

    // OPTIONAL IDEA:
    // $(".piece").click(function(){
    //     optionHelper(this);
    // });

    // TASK: Setup the board!
    // a) When the user clicks the start game button, fill in the board.
    // HINTS: jQuery events
    // b) Hide the start game button
    // HINT: jQuery Hide
    // c) Create a text the shows which players turn it is
    // HINT: jQuery Add

    // TASK 2: When you click on a piece, print something to the console.
    
})