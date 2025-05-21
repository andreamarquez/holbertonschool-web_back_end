const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(path, 'utf-8');

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
  } catch (error) {
    // Throw an error if the file cannot be read
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
