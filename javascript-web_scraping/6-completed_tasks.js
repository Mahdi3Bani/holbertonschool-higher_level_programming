#!/usr/bin/node
const data = {};
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const content = JSON.parse(body);
  for (const task in content) {
    if (!(content[task].userId in data)) {
      data[content[task].userId] = 0;
    }
    if (content[task].completed === true) {
      data[content[task].userId]++;
    }
  }
  console.log(data);
}
);
