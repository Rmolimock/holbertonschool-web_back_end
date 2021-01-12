const fs = require('fs');
const http = require('http');


function countStudents(path) {
  return new Promise((resolve, reject) => {
    try {
        const f = fs.readFileSync(path, { encoding: 'utf-8' });
        const rows = f.split('\n').slice(1);
        console.log(`Number of students: ${rows.length}`);
        let listCsStudents = '';
        let numlistCsStudents = 0;
        let numlistSweStudents = 0;
        let listSweStudents = '';

        rows.forEach((row) => {
        row = row.split(',');
        if (row[3] === 'SWE') {
            listSweStudents += listSweStudents ? `, ${row[0]}` : row[0];
            numlistSweStudents += 1;
        } else if (row[3] === 'CS') {
            numlistCsStudents += 1;
            listCsStudents += listCsStudents ? `, ${row[0]}` : row[0];
        }
        });

        resolve({
            total: totalData.length,
            cscounter,
            csStudents,
            swecounter,
            sweStudents,
          });
      } catch (err) { reject(Error('Cannot load the database')); }
  })
};

module.exports = countStudents

const app = http.createServer((req, res) => {
  if (req.url === '/' && req.method === 'GET') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url === '/students' && req.method === 'GET') {
    countStudents('database.csv').then(({
        total, cscounter, csStudents, swecounter, sweStudents,
    }) => {
        res.write('This is the list of our students\n');
        res.write(`Number of students: ${total}\n`);
        res.write(
          `Number of students in CS: ${cscounter}. List: ${csStudents}\n`,
        );
        res.write(
          `Number of students in SWE: ${swecounter}. List: ${sweStudents}\n`,
        );
      },
    ).catch((err) => { throw err; });
  } else {
      res.end();
    }
}).listen(1245);

module.exports = app;
