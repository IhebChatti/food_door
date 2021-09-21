export default class Restaurant {
  constructor (data = {}) {
    if (!data) { data = {}; };
    /**
     * @type {string}
     */
    this.name = data.name ?? '';
    /**
     * @type {string}
     */
    this.address = data.address ?? '';
    /**
     * @type {string}
     */
    this.phone = data.phone ?? '';
    /**
     * @type {string}
     */
    this.description = data.description ?? '';
    /**
     * @type {Array}
     */
    this.images = data.images ?? [];
  }
}
