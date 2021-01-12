const fs = require('fs');

const countStudents = (path) => {
  try {
    let input = fs.readFileSync(path, 'utf8').toString().split('\n');
    input = input.slice(1, input.length - 1);
    console.log(`Number of students: ${input.length}`);
    const studentArray = {};
    for (const each of input) {
      const student = each.split(',');
      if (!studentArray[student[3]]){
        studentArray[student[3]] = [];
      }
      studentArray[student[3]].push(student[0]);
    }
    for (const cls in studentArray) {
      let msg = `Number of students in ${cls}: ${studentArray[cls].length}. List: ${studentArray[cls].join(', ')}`
      if (cls) console.log(msg);
    }
  } catch (er) {
    throw new Error('Cannot load the infobase');
  }
};
module.exports = countStudents;
