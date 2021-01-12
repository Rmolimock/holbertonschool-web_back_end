process.stdin.setEncoding('utf-8');
process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const userName = process.stdin.read();
  if (userName) process.stdout.write(`Your name is: ${userName}\n`);
});
if (process.stdout.isTTY) {
  process.stdin.on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
}
