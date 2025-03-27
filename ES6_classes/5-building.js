export default class Building {
  constructor(sqft) {
    // Type validation
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    }

    // Attribute assignment
    this._sqft = sqft;

    // Ensure the class is abstract
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }
}
