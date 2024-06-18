#!/usr/bin/node
/*
Return the number of occurrences in a list
*/
exports.nbOccurences = function (list, searchElement) {
  return list.filter((currentElement) => currentElement === searchElement).length;
};
