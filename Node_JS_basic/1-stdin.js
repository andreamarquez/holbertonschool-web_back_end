console.log('Welcome to Holberton School, what is your name?');

process.stdin.setEncoding('utf-8');

process.stdin.on('data', (input) => {
  const name = input.trim();
  console.log(`Your name is: ${name}`);
  console.log('This important software is now closing');
  process.exit(); // Exit the program after displaying the closing message
});

process.stdin.on('end', () => {
  // This ensures the closing message is displayed for piped input
  console.log('This important software is now closing');
});
