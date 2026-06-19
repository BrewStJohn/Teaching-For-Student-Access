// 2) Create a query to OMDB using jQuery get. 
// You will need to craft your url query first.

$(document).ready(function(){
    console.log("test");
    $.get("https://www.omdbapi.com/?s=Lord+of+the+Rings&apikey=af5dd467", 
        function(data, status){
        
        // what is data? What is status?
        console.log(data);
        // What are these values?
        let poster = data.Search[0].Poster;

        $.get(poster, function(data, status){
            console.log(status)
            // if status is not success
            // then dont load an image, or say image unavailable
            
        });

        let title = data.Search[0].Title;
        let year = data.Search[0].Year;

        // craft my jQuery statement
        let newRow = "<tr><td><img src='" + poster + 
        "'></td><td>" + title + "</td><td>" + year + 
        "</td></tr>"
        
        // what does this do?
        $("table").append(newRow);

        // console.log(d

    });
});