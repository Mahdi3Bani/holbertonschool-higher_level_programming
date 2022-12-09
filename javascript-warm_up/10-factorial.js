#!/usr/bin/node

function fact (a) {
  if (a === 1) {
    return a;
  }
  return a * fact(a - 1);
}
const process = require('process');
const args = process.argv;
if (isNaN(args[2])) {
  console.log('NaN');
} else {
  const fac = args[2];
  console.log(fact(fac));
}
