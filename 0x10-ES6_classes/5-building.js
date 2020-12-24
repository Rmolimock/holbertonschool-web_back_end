// comment
export default class Building {
  constructor(sqft) {
    if (this.evacuationWarningMessage === undefined && this.constructor !== Building) {
      throw Error(
        'Class extending Building must override evacuationWarningMessage',
      );
    }
    this._sqft = sqft;
  }

  set sqft(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
