#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
const axios = require('axios');
const url = process.argv[2];
const completed = {};

axios.get(url)
  .then(response => {
    const results = response.data;
    for (const result of results) {
      if (result.completed === true) {
        if (completed[result.userId] === undefined) {
          completed[result.userId] = 1;
        } else {
          completed[result.userId] += 1;
        }
      }
    }
    console.log(completed);
  })
  .catch(error => {
    console.error(error.message);
  });
