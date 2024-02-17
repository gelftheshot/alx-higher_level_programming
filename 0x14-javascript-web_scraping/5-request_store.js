#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.
const axios = require('axios');
const fs = require('fs').promises;
const url = process.argv[2];
const file = process.argv[3];

axios.get(url, {
  responseType: 'arraybuffer'
})
  .then(response => {
    return fs.writeFile(file, response.data);
  })
  .catch(error => {
    console.error(error.message);
  });
