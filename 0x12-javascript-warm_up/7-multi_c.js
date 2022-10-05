#!/usr/bin/node

const count = process.argv[2];

if (count === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < count) {
    console.log('C is fun');
    i += 1;
  }
}
