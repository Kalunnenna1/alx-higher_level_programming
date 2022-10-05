#!/usr/bin/node

const count = process.argv[2];
let output = '';

if (count === undefined || isNaN(count)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < count; i++) {
    output += 'X';
  }
  for (let i = 0; i < count; i++) {
    console.log(output);
  }
}
