#!/usr/bin/node

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let row = '';
      let y = 0;
      while (y < this.width) {
        row += myChar;
        y++;
      }

      console.log(row);
    }
  }
}

module.exports = Square;
