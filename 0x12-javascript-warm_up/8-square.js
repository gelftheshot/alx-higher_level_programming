#!/usr/bin/node

let i;
let j;
if ((isNaN(process.argv[2]))) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  for (i = 0; i < x; i++) {
    let b = '';
    for (j = 0; j < x; j++) {
      b += 'X';
    }
    console.log(b);
  }
}
