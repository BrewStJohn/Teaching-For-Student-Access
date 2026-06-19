$(document).ready(function(){
    // 3) Use the jQuery (Javascript but simpler) 
    // get method to print to the console:
    // a) The title of your film/tv show
    // b) the year it was released
    // c) A link to a poster for the film/tv show
    // HINT: jQuery AJAX get
     $.get("https://www.omdbapi.com/?s=Lord+of+the+Rings&apikey=af5dd467", function(data, status){
        console.log(data['Search'][0]['Title']);
        $("tbody").append('<tr><td>' + data["Search"][0]["Title"] + '</td></tr>'
        );

    });

    // 4) Add a paragraph element to the page with the title 
    // of the film. How can we create a table and add rows to 
    // it with the information provided in the JSON? 
    // HINT: jQuery Add Elements
});

