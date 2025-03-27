export default class Airport {
  constructor(name, code) {
    // Type validation
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }

    // Attribute assignment
    this._name = name;
    this._code = code;
  }

  // Override toString method
  toString() {
    return `[object ${this._code}]`;
  }
}
