export default class Car {
  constructor(brand = undefined, motor = undefined, color = undefined) {
    // Type validation
    if (brand !== undefined && typeof brand !== 'string') {
      throw new TypeError('Brand must be a string');
    }
    if (motor !== undefined && typeof motor !== 'string') {
      throw new TypeError('Motor must be a string');
    }
    if (color !== undefined && typeof color !== 'string') {
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
    return new Constructor(); // Create a new instance without passing attributes
  }
}
