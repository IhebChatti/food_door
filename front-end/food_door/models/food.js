export default class FoodItem {
  constructor(data = {}) {
    if (!data) data = {};
    /**
     * @type {string}
     */
    this.name = data.name ?? '';
    /**
     * @type {string}
     */
    this.description = data.description ?? '';
    /**
     * @type {number}
     */
    this.price = data.price ?? 0.0;
  }
}
