#!/usr/bin/node
const oldDict = require('./101-data.js');
const sortedDict = {};
for (const userId in oldDict.dict) {
  const occ = oldDict.dict[userId];

  if (!(occ in sortedDict)) {
    sortedDict[occ] = [];
  }

  sortedDict[occ].push(userId);
}

console.log(sortedDict);
