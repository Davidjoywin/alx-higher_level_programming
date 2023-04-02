#!/usr/bin/node

const dict = require('./101-data.json').dict;
const newDict = {};

Object.keys(dict).map(function (key) {
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  }
  return newDict[dict[key]].push(key);
});

console.log(newDict);