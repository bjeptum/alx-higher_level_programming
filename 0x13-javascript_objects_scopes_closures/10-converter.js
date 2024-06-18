#!/usr/bin/node
/*
Converts no from base 10 to the number entered as argument
*/
exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
