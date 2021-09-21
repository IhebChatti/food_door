export default class User {
  constructor (data = {}) {
    if (!data) { data = {}; }
    /**
     * @type {string}
     */
    this.firstName = data.first_name ?? '';
    /**
     * @type {string}
     */
    this.lastName = data.last_name ?? '';
    /**
     * @type {string}
     */
    this.email = data.email ?? '';
    /**
     * @type {string}
     */
    this.address = data.address ?? '';
  }
}
