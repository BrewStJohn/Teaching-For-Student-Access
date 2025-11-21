// 3) Use the jQuery get method to print to the console:
// a) The title of your film/tv show
// b) the year it was released
// c) Who stars in it (actors)
// d) A link to a poster for the film/tv show
// HINT: jQuery AJAX get


// OPTION 1: Multiple queries
// links = {
//     "film1": "https://www.omdbapi.com/?t=Harry+Potter+and+the+Sorcerer%27s+Stone&y=2001&apikey=af5dd467"
// }

// links.forEach(getFilm)

// function getFilm(link){
//     $.get(link)
// };

$(document).ready(function(){

    // OPTION 2: Make your query more querious

    // 4) Use jQuery to add table rows to the brief view
    // and, for every film/tv show, add an entry
    // to the table
    // BONUS: Use Bootstrap to decorate it
    // HINT: jQuery Add
    $.get("https://www.omdbapi.com/?s=Harry+Potter&type=Movie&apikey=af5dd467", function(data, status){
        console.log(data);
        console.log(status);

        for (let i = 0; i < data.Search.length; i++){
            poster = "<img src=\"" + data.Search[i].Poster + "\"></img>";
            title = data.Search[i].Title;
            year = data.Search[i].Year;

            tr = $("<tr></tr>")
            tr.append("<td>" + poster + "</td>");
            tr.append("<td>" + title + "</td>");
            tr.append("<td>" + year + "</td>")
            // tr.append("<td></td>").append(year);
            // txt1 = $("<p></p>").text(data.Plot);
            $("#brief-view > table > tbody").append(tr);

            // make another jQuery request
            $.get("https://www.omdbapi.com/?i="+data.Search[i].imdbID+"&apikey=af5dd467", function(detailedData, detailedStatus){
                console.log(detailedData);
                // create the bootstrap with the collapse!
            });
        }
       
    });
});

