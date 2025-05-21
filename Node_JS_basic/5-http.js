const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.setHeader('Content-Type', 'text/plain');
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.setHeader('Content-Type', 'text/plain');
    res.statusCode = 200;
    res.write('This is the list of our students\n');

    const database = process.argv[2];
    countStudents(database)
      .then((output) => {
        res.write(output);
        res.end();
      })
      .catch((err) => {
        res.end(err.message);
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
