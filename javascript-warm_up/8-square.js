#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    for (let j = 0; j < i; j++) {
      console.log('X');
    }
  }
}
