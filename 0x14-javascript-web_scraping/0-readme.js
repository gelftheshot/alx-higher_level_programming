#!/usr/bin/node
// script that reads and prints the content
const fs = require('fs');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', function (err, data) {
  console.log(err || data);
});
