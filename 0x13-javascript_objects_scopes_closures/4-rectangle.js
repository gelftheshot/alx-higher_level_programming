#!/usr/bin/node

module.exports = class Rectangel {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += 'x';
      }
      console.log(x);
    }
  }

  rotate () {
    const m = this.width;
    this.width = this.height;
    this.height = m;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};