// 3) Use the jQuery get method to print to the console:
// a) The title of your film/tv show
// b) the year it was released
// c) Who stars in it (actors)
// d) A link to a poster for the film/tv show
// HINT: jQuery AJAX get

$(document).ready(function(){
    $.get("https://www.omdbapi.com/?t=Harry+Potter+and+the+Sorcerer%27s+Stone&y=2001&apikey=af5dd467", function(data, status){
        console.log(data.Plot);
        console.log(status);
        txt1 = $("<p></p>").text(data.Plot);
        $("#brief-view").append(txt1);
    });
});

// 4) Use jQuery to add table rows to the brief view
// and, for every film/tv show, add an entry
// to the table
// BONUS: Use Bootstrap to decorate it
// HINT: jQuery Add