#!/usr/bin/node

// Get the value of x from the command-line argument
const x = process.argv[2];

// Check if x is a valid number
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // Convert x to an integer
  const numOccurrences = parseInt(x);

  // Check if numOccurrences is positive
  if (numOccurrences > 0) {
    // Loop to print "C is fun" numOccurrences times
    for (let i = 0; i < numOccurrences; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
}
