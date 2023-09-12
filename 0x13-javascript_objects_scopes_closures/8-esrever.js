#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0; i < list.length - i - 1; i++) {
    const tmp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = tmp;
  }
  return (list);
};
