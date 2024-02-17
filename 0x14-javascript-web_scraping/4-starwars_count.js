#!/usr/bin/node
// Script that prints the number of movies where the character
// “Wedge Antilles” is present.
const axios = require('axios');
const url = process.argv[2];

axios.get(url, {
  validateStatus: function (status) {
    return true;
  }
})
  .then(response => {
    if (response.status === 200) {
      const results = response.data.results;
      const count = results.reduce((count, result) => {
        return count + result.characters.filter(character => character.includes('18')).length;
      }, 0);
      console.log(count);
    } else {
      console.log('code:', response.status);
    }
  })
  .catch(error => {
    console.log('Error:', error.message);
  });
