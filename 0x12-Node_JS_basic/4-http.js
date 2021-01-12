const http = require('http');

const app = http.createServer((request, response) => {
  response.setHeader('Content-Type', 'text/plain');
  response.statusCode = 200;
  response.end('Hello Holberton School!');
});
app.listen(1245);

module.exports = app;
