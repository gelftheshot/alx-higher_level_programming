#!/usr/bin/node
// Script that writes a string to a file.
const fs = require('fs');
const filePath = process.argv[2];
const text = process.argv[3];

fs.writeFile(filePath, text, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
