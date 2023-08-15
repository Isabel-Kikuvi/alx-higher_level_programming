#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      let y = 0;
      while (y < this.width) {
        row += 'X';
        y++;
      }

      console.log(row);
    }
  }
}

module.exports = Rectangle;
