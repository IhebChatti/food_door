export default class User {
<<<<<<< HEAD
  constructor(data = {}) {
    if (!data) {
      data = {};
    }
    /**
     * @type {string}
     */
    this.first_name = data.first_name ?? "";
    /**
     * @type {string}
     */
    this.last_name = data.last_name ?? "";
    /**
     * @type {email}
     */
    this.email = data.email ?? "abc@gmail.com";
    /**
     * @type {string}
     */
    this.password = data.password ?? "";
    /**
     * @type {string}
     */
    this.address = data.address ?? "";
    /**
     * @type {string}
     */
    this.phone = data.phone ?? "";
    /**
     * @type {boolean}
     */
    this.is_verified = data.is_verified ?? false;
    /**
     * @type {VarDate}
     */
    this.last_login = data.last_login ?? "";
=======
  constructor (data = {}) {
    if (!data) { data = {} }
    /**
     * @type {string}
     */
    this.firstName = data.first_name ?? ''
    /**
     * @type {string}
     */
    this.lastName = data.last_name ?? ''
    /**
     * @type {string}
     */
    this.email = data.email ?? ''
    /**
     * @type {string}
     */
    this.address = data.address ?? ''
>>>>>>> 1a3d21c557ebfc19f2db8cff2dae20e39278a32c
  }
}
