#!/usr/bin/node
const Rectangle = require('./5-square.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let square = '';
    for (let j = 0; j < this.width; j++) {
      square = square + c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(square);
    }
  }
}
module.exports = Square;
