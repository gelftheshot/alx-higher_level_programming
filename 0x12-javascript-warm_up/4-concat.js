#!/usr/bin/node

let v1 = 'undefined';
const v2 = 'is';
let v3 = 'undefined';

if (process.argv[2]) {
  v1 = process.argv[2];
}

if (process.argv[3]) {
  v3 = process.argv[3];
}

console.log(v1, v2, v3);
