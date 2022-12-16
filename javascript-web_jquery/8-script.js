$.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
  var movies = data.results;

  $.each(movies, function(index, movie) {
    $("#list_movies").append("<li>" + movie.title + "</li>");
  });
});