#!/usr/bin/node
const axios = require('axios');
const url = 'https://swapi.dev/api/films/' + process.argv[2];

axios.get(url)
  .then(response => {
    const characters = response.data.characters;
    printCharacters(characters, 0);
  })
  .catch(error => {
    console.error(error.message);
  });

function printCharacters (characters, index) {
  if (index < characters.length) {
    axios.get(characters[index])
      .then(response => {
        console.log(response.data.name);
        printCharacters(characters, index + 1);
      })
      .catch(error => {
        console.error(error.message);
      });
  }
}
