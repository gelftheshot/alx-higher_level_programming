#!/usr/bin/node
const axios = require('axios');
const url = 'https://swapi.dev/api/films/' + process.argv[2];

axios.get(url)
  .then(response => {
    const characters = response.data.characters;
    if (characters) {
      characters.forEach(character => {
        axios.get(character)
          .then(response => {
            console.log(response.data.name);
          })
          .catch(error => {
            console.error(error.message);
          });
      });
    } else {
      console.log('No characters found');
    }
  })
  .catch(error => {
    console.error(error.message);
  });
