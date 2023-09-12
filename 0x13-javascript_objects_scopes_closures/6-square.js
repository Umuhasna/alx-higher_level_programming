#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let sq = '';
    for (let i = 0; i < this.width; i++) {
      sq += c;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(sq);
    }
  }
}

module.exports = Square;
