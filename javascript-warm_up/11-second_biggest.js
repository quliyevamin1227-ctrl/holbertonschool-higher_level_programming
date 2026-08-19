#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);

  const biggest = args[0];
  let secondBiggest = null;

  for (const num of args) {
    if (num < biggest) {
      secondBiggest = num;
      break;
    }
  }

  console.log(secondBiggest === null ? 0 : secondBiggest);
}
