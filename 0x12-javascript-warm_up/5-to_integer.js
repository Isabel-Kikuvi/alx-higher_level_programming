#!/usr/bin/node
const number = process.argv[2];
const parsNum = parseInt(number);
if (!isNaN(parsNum)) {
  console.log('My number: ', parsNum);
} else {
  console.log('Not a number');
}
