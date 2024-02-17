#!/usr/bin/node
// Script that display the status code of a GET request.
const axios = require('axios');

axios.get('https://api.github.com/users/github')
  .then(response => {
    console.log('code:', response.status);
  })
  .catch(error => {
    console.error(error);
  });