#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2);
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < (arr.length - i - 1); j++) {
      if (parseInt(arr[j]) > parseInt(arr[j + 1])) {
        const tmp = parseInt(arr[j]);
        arr[j] = parseInt(arr[j + 1]);
        arr[j + 1] = tmp;
      }
    }
  }
  arr.reverse();
  console.log(arr[1]);
}
