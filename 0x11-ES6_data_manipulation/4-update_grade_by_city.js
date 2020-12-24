// comment
export default function updateStudentGradeByCity(array, city, newGrades) {
  byLocation = array.filter((i) => i.location === city)
  return byLocation.map((person) => {
    const grades = newGrades.filter((i) => i.studentId === person.id);
    const grade = grades.length ? grades[0].grade : 'N/A';
    return {
      ...person,
      grade,
    };
  });
}
