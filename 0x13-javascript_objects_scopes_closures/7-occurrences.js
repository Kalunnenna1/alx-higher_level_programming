#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter(number => number === searchElement).length;
};
