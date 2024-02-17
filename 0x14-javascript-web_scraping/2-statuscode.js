#!/usr/bin/node
// Script that display the status code of a GET request.
const axios = require('axios');
const url = process.argv[2];

axios.get(url, {
  validateStatus: function (status) {
    return true;
  }
})
  .then(response => {
    console.log('code:', response.status);
  })
  .catch(error => {
    console.log('Error:', error.message);
  });
