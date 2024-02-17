#!/usr/bin/node
// Script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(url, {
  validateStatus: function (status) {
    return true;
  }
})
  .then(response => {
    if (response.status === 200) {
      console.log(response.data.title);
    } else {
      console.log('code:', response.status);
    }
  })
  .catch(error => {
    console.log('Error:', error.message);
  });
