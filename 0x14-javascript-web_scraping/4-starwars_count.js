#!/usr/bin/node
/*
Prints the number of movies
where the character “Wedge Antilles” is present
*/
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    // Parse the response body as JSON
    const filmsData = JSON.parse(body).results;
    // Check for  Wedge Antilles
    filmsData.forEach(film => {
        if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  }
});
