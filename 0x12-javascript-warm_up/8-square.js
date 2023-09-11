#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (size) {
  let square = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    if (i !== size - 1) {
      square += '\n';
    }
  }
  console.log(square);
} else {
  console.log('Missing size');
}
