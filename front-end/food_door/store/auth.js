/* eslint-disable no-return-assign */
/* eslint-disable no-unused-vars */
import Vue from 'vue';
import User from '@/models/user';
const localVue = new Vue();

const CONTEXT = {
  LOGIN: {
    URL: 'api/token/'
  }
};

Object.freeze(CONTEXT);

//= ========================================================STATE========================================================
export const state = () => ({
  /**
   * @type {User}
   */
  user: new User()
});

//= ======================================================MUTATIONS======================================================

export const mutations = {
  // eslint-disable-next-line camelcase
  SET_TOKENS: (state, { access, refresh, user_types }) => {
    window.localStorage.setItem('access_token', access);
    window.localStorage.setItem('refresh_token', refresh);
    window.localStorage.setItem('user_types', user_types);
  }
};

//= =======================================================ACTIONS=======================================================

export const actions = {
  async login ({ commit, dispatch }, payload) {
    const result = await this.$axios.$post('http://127.0.0.1:8000/api/token/', payload);
    commit('SET_TOKENS', result);
  },

  async signup ({ commit, dispatch }, payload) {
    await this.$axios.$post('http://127.0.0.1:8000/signup/', payload);
  },

  logout ({ commit, dispatch }, payload) {
    window.localStorage.clear();
    window.sessionStorage.clear();
    this.$axios.setToken(false);
    this.$router.go();
  }
};
//= ======================================================GETTERS========================================================

export const getters = {
  list: state => state.restaurants,
  show: state => state.restaurant
};
