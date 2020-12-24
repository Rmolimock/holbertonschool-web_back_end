// comment
export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('name must be a String');
    if (typeof length !== 'number') throw TypeError('length must be a Number');
    if (!Array.isArray(students)) throw TypeError('students must be an Array');
    students.forEach(student => {
      if (typeof student !== 'string') { throw TypeError('students must contain strings'); }
    });
    this._students = students;
    this._length = length;
    this._name = name;
  }

  set name(name) {
    if (typeof name !== 'string') throw TypeError('name must be a String');
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set length(length) {
    if (typeof length !== 'number') throw TypeError('length must be a Number');
    this._length = length;
  }

  get length() {
    return this._length;
  }

  set students(students) {
    if (!Array.isArray(students)) throw TypeError('students must be an Array');
    students.forEach(student => {
      if (typeof student !== 'string') { throw TypeError('students must contain strings'); }
    });
    this._students = students;
  }

  get students() {
    return this._students;
  }
}
