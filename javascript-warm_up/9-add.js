#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (isNaN(args[2])) {
  console.log('NaN');
} else {
  console.log(parseInt(args[2]) + parseInt(args[3]));
}
