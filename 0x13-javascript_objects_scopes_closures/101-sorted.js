#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  const value = dict[key];
  if (!(Object.prototype.hasOwnProperty.call(newDict, value))) {
    newDict[dict[key]] = [];
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
