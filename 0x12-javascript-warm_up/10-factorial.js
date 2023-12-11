#!/usr/bin/node

function fac (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 1) {
    return (1);
  } else {
    return (n * fac(n - 1));
  }
}

console.log(fac(Number(process.argv[2])));
