#!/usr/bin/node

const process = require('process');
const args = process.argv;
if (isNaN(args[2])) {
  console.log('1');
} else {
  let a = 0;
  for (let i = 2; i < args.length; i++) {
    if (a > parseInt(args[i])) {
      a = args[i];
    }
  }
  let b = 0;
  for (let j = 2; j < args.length; j++) {
    if (parseInt(args[j]) > b || parseInt(args[j]) < a) {
      b = args[j];
    }
  }
  console.log(b);
}
