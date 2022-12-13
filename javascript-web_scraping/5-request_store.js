#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const fs = require('fs');
  fs.writeFileSync(process.argv[3], body, 'utf8', function (err) {
    if (err) throw err;
  });
});
