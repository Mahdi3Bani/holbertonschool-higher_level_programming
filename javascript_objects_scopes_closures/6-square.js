#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let square = '';
    for (let j = 0; j < this.width; j++) {
      square = square + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(square);
    }
  }
}
module.exports = Square;
