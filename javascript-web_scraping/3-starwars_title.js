#!/usr/bin/node
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(link, function (error, response, body) {
  if (error) throw error;
  const content = JSON.parse(body);
  console.log(content.title);
});
