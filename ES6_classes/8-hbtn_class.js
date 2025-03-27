export default class HolbertonClass {
  constructor(size, location) {
    // Type validation
    if (typeof size !== 'number') {
      throw new TypeError('Size must be a number');
    }
    if (typeof location !== 'string') {
      throw new TypeError('Location must be a string');
    }

    // Attribute assignment
    this._size = size;
    this._location = location;
  }

  // Override valueOf for casting to Number
  valueOf() {
    return this._size;
  }

  // Override toString for casting to String
  toString() {
    return this._location;
  }
}
