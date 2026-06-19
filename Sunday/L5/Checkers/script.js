$(document).ready(function() {
    $("#start").click(function(){
        let options = []
        $(this).hide();
        // need to finish filling in the gameboard
        // make 1 row
        for (let row = 0; row<8; row++){
            for (let col = 0; col<8; col++){
                if ((row+col) % 2 == 1){
                    let id = row +"_" + col
                    $("#squares").append("<div class='red square' id=" + id + "></div>")
                    if (row < 3){
                        // add piece
                        $("#"+id).append("<div class='white piece'></div>")
                    } else if(row > 4){
                         $("#"+id).append("<div class='black piece'></div>")
                    }
                } else{
                    $("#squares").append("<div class='square'></div>")
                }
            }
        }
        // NEXT: When you click on a piece, log something
        // to the console
        // does it matter what piece I click?
        $(".piece").click(function(){
            // what needs to be considered when I click a piece?
            // - its parents
            // --> highlight the squares the piece can go to
            // - whos turn it is
            // - remove previous highlighted options
            optionHelper($(this));
        });

        function getOptions(piece_color, piece_row, piece_col){
            console.log(piece_color, piece_row, piece_col)
            // for every valid option (based on the row and col
            // of the piece selected), change the css of the 
            // valid options to yellow.
            if (piece_color == "rgb(255, 255, 255)"){
                // highlighting squares below it
                option1 = $("#"+(piece_row+1)+"_"+(piece_col-1))
                if (options.includes(option1)){
                    console.log("test")
                }
                else{
                    option1.css("background-color", "yellow")
                    options.push(option1)
                    console.log(options)
                }
            } else {
                // black, highlighting squares above it
            }
            
        }

        function clearOptions(value, index, array){
            // change the colour back to red
            // remove this item from the list (it is no longer an option)
        }

        function optionHelper(clickedPiece){
            // get its parent
            // console.log(clickedPiece);
            parent = clickedPiece.parent();
            pid = parent.attr("id").split("_");
            // Clear out previous options
            options.forEach(clearOptions);
            // get parents row and column
            getOptions(clickedPiece.css("background-color"), Number(pid[0]), Number(pid[1]));
        }

    });
});

