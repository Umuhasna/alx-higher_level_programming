#!/usr/bin/node
function factorial (x) {
  if (x === 0) {
    return (1);
  }
  return (x * factorial(x - 1));
}
const num = parseInt(process.argv[2]);
if (num) {
  console.log(factorial(num));
} else {
  console.log('1');
}
