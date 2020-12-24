// comment
export class HolbertonClass {
  constructor(year, location) {
    this._location = location;
    this._year = year;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this._holbertonClass = holbertonClass;
    this._firstName = firstName;
    this._lastName = lastName;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this.holbertonClass;
  }
}
const student0 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student1 = new StudentHolberton('John', 'Doe', class2020);
const student2 = new StudentHolberton('Albert', 'Clinton', class2019);
const student3 = new StudentHolberton('Donald', 'Bush', class2019);
const student4 = new StudentHolberton('Jason', 'Sandler', class2019);

export const listOfStudents = [student0, student1, student2, student3, student4];
