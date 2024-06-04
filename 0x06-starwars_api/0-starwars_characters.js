#!/usr/bin/env node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const movieUrl = `${API_URL}/films/${movieId}/`;

request(movieUrl, (err, _, body) => {
  if (err) {
    console.error('Error fetching movie details:', err);
    return;
  }

  try {
    const charactersURL = JSON.parse(body).characters;
    const charactersPromises = charactersURL.map(url => 
      new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          } else {
            resolve(JSON.parse(charactersReqBody).name);
          }
        });
      })
    );

    Promise.all(charactersPromises)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.error('Error fetching character names:', allErr));

  } catch (parseErr) {
    console.error('Error parsing movie details:', parseErr);
  }
});
