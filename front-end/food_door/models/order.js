export default class Order {
  constructor(data = {}) {
    if (!data) data = {};
    /**
     * @type {string}
     */
    this.food_name = data.food_name ?? "";
    /**
     * @type {string}
     */
    this.description = data.description ?? "";
    /**
     * @type {string}
     */
    this.description = data.description ?? "";
  }
}
