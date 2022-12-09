#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  let square = '';
  for (let j = 0; j < args[2]; j++) {
    square = square + 'X';
  }
  for (let i = 0; i < args[2]; i++) {
    console.log(square);
  }
}
