#!/usr/bin/node
const fs = require('fs');
try {
  const content = fs.readFileSync(process.argv[2], 'utf8');
  console.log(content);
} catch (err) {
  console.log(err);
}
