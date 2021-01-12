const countStudents = require('./3-read_file_async');
const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.write('Hello Holberton School!');
    res.end();
});
app.get('/students', async (req, res) => {
  const message = 'This is the list of our students\n';
  try {
    const [a, b, c] = await countStudents(process.argv[2]);
    res.status(200).write(`${message + a}\n${b}\n${c}\n`);
  } catch (er) {
    res.status(404).write(`${message}Cannot load the database`);
  }
  res.end()
});

app.listen(1245);

module.exports = app;
