$(document).ready(function(){
    console.log(document)
    film_link = "https://www.omdbapi.com/?s=Lord+of+the+Rings&apikey=af5dd467";
    // 3) Use the jQuery get method to print to the console:
    $.get(film_link, function(data, status){
        // console.log("Data: " + data + "\nStatus: " + status);
        console.log(data);
        // a) The title of your film/tv show
        console.log(data['Search'][0]['Title'])
        // b) the year it was released
        // c) A link to a poster for the film/tv show
        // HINT: jQuery AJAX get
        let title = `<tr><td>${data['Search'][0]['Title']}<td></tr>`
        $("tbody").append(title)// paragraph element with the title
    });
});

