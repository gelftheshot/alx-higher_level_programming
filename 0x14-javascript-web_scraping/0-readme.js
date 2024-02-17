#!/usr/bin/node
// script that reads and prints the content
const fs = require('fs');
const file_path = process.argv[2];
fs.readFile(file_path, 'utf8', function (err, data) {
  console.log(err || data);
});