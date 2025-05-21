const readDatabase = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const databasePath = process.argv[2]; // Get the database file path from command-line arguments
      const studentsByField = await readDatabase(databasePath);

      let responseText = 'This is the list of our students\n';

      // Sort fields alphabetically (case insensitive)
      const sortedFields = Object.keys(studentsByField).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase())
      );

      // Append information for each field
      sortedFields.forEach((field) => {
        const students = studentsByField[field];
        responseText += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      });

      res.status(200).send(responseText.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    try {
      const databasePath = process.argv[2]; // Get the database file path from command-line arguments
      const major = req.params.major; // Get the major from the request parameters

      if (major !== 'CS' && major !== 'SWE') {
        res.status(500).send('Major parameter must be CS or SWE');
        return;
      }

      const studentsByField = await readDatabase(databasePath);
      const students = studentsByField[major];

      if (!students) {
        res.status(200).send('List: '); // If no students in the field, return an empty list
        return;
      }

      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
