#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function requestList (characterList, index) {
  if (characterList.length === index) {
    return;
  }

  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      requestList(characterList, index + 1);
    }
  });
}

request(endpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characterList = JSON.parse(body).characters;

    requestList(characterList, 0);
  }
});
