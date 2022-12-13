#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const content = JSON.parse(body);
  let movies;
  let charac;
  let i = 0;
  for (movies in content.results) {
    for (charac in content.results[movies].characters) {
      if (content.results[movies].characters[charac] === 'https://swapi-api.hbtn.io/api/people/18/') {
        i++;
      }
    }
  }
  console.log(i);
});
