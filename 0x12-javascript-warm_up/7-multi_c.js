#!/usr/bin/node

let i;
if ((isNaN(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(process.argv[2]);
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
