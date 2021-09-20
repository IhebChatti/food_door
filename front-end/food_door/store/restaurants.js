/* eslint-disable no-unused-vars */
import Restaurant from '@/models/restaurant';
import Vue from "vue";
const localVue = new Vue();

const CONTEXT = {
  INDEX: {
    URL: 'list_restaurants',
  },
}

Object.freeze(CONTEXT);

//=========================================================STATE========================================================
export const state = () => ({
  /**
   * @type {Restaurant}
   */
  restaurant: new Restaurant(),
  /**
   * @type {Array<Restaurant>}
   */
  restaurants: [],
});

//=======================================================MUTATIONS======================================================

export const mutations = {
  SET_INDEX: (state, payload) => state.restaurants = payload.map(restaurant => new Restaurant(restaurant)),
  SET_SHOW: (state, payload) => state.restaurant = new Restaurant(payload),
};



//========================================================ACTIONS=======================================================

export const actions = {
  async fetchRestaurants ({ commit }) {
    const payload = await this.$axios.$get('http://127.0.0.1:8000/list_restaurants')
    commit('SET_INDEX', payload)
  }
}
//=======================================================GETTERS========================================================

export const getters = {
  list: (state) => state.restaurants,
  show: (state) => state.restaurant,
}
