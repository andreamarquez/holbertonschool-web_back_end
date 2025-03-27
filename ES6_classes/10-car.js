export default class Car {
  constructor(brand, motor, color) {
    // Type validation
    if (typeof brand !== 'string') {
      throw new TypeError('Brand must be a string');
    }
    if (typeof motor !== 'string') {
      throw new TypeError('Motor must be a string');
    }
    if (typeof color !== 'string') {
      throw new TypeError('Color must be a string');
    }

    // Attribute assignment
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Method to clone the car
  cloneCar() {
    const Constructor = this.constructor; // Dynamically get the class of the current object
    return new Constructor(this._brand, this._motor, this._color); // Pass attributes to the new instance
  }
}
