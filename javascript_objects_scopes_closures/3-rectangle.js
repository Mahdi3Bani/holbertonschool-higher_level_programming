#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let square = '';
    for (let j = 0; j < this.height; j++) {
      square = square + 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(square);
    }
  }
};
