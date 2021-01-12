const fs = require('fs');

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

        console.log(`Number of students in CS: ${numlistCsStudents}. List: ${listCsStudents}`);
        console.log(`Number of students in SWE: ${numlistSweStudents}. List: ${listSweStudents}`);
    } catch (err) { reject(Error('Cannot load the database')); }
  })
};

module.exports = countStudents
