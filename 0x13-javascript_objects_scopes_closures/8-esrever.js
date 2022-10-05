#!/usr/bin/node

exports.esrever = function (list) {
  let left, right, temp;

  for (left = 0, right = list.length - 1; left < list.length / 2; left++, right--) {
    temp = list[left];
    list[left] = list[right];
    list[right] = temp;
  }

  return list;
};
