const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Read the file asynchronously
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        // Reject the promise if the file cannot be read
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        // Split the file content into lines and filter out empty lines
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        // Remove the header line
        const header = lines.shift();

        if (!header) {
          throw new Error('Cannot load the database');
        }

        // Parse the remaining lines into student records
        const students = lines.map((line) => line.split(','));

        // Log the total number of students
        console.log(`Number of students: ${students.length}`);

        // Group students by field
        const fields = {};
        students.forEach((student) => {
          const field = student[3]; // The field is the 4th column
          const firstname = student[0]; // The first name is the 1st column

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        });

        // Log the number of students and their names for each field
        for (const [field, names] of Object.entries(fields)) {
          console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }

        // Resolve the promise
        resolve();
      } catch (error) {
        // Reject the promise if there is an error processing the file
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

module.exports = countStudents;
