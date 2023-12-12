#!/usr/bin/node
exports.converter = function (base) {
  return i => i.toString(base);
};
