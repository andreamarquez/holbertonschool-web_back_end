const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const header = lines.shift();

        if (!header) {
          throw new Error('Cannot load the database');
        }

        const students = lines.map((line) => line.split(','));
        const totalStudents = students.length;

        const fields = {};
        students.forEach((student) => {
          const field = student[3];
          const firstname = student[0];

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        });

        let output = `Number of students: ${totalStudents}\n`;
        for (const [field, names] of Object.entries(fields)) {
          output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        }

        resolve(output.trim()); // Resolve with the formatted output
      } catch (error) {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

module.exports = countStudents;
