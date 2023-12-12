#!/usr/bin/node

const list = require('./100-data.js').list;
const new_list = list.map((i, index) => i * index);
console.log(list);
console.log(new_list);
