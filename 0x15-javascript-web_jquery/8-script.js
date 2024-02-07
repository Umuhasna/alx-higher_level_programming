$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $('#list_movies').append(
      data.results.map(function (movie) {
        return '<li>' + movie.title + '</li>';
      }).join('')
    );
  });
});
