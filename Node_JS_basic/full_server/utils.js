const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      try {
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const header = lines.shift();

        if (!header) {
          throw new Error('Cannot parse the database');
        }

        const students = lines.map((line) => line.split(','));
        const fields = {};

        students.forEach((student) => {
          const field = student[3];
          const firstname = student[0];

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        });

        resolve(fields);
      } catch (error) {
        reject(error);
      }
    });
  });
}

module.exports = readDatabase;
