#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const content = JSON.parse(body).results;
  let i = 0;
  for (const movies in content) {
    const charac = content[movies].characters;
    for (const char in charac) {
      if (charac[char].endsWith('/18/')) {
        i++;
      }
    }
  }
  console.log(i);
});
