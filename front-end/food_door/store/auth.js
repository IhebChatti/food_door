/* eslint-disable no-return-assign */
/* eslint-disable no-unused-vars */
import Vue from 'vue'
import User from '@/models/user'
const localVue = new Vue()

const CONTEXT = {
  LOGIN: {
    URL: 'api/token/'
  }
}

Object.freeze(CONTEXT)

//= ========================================================STATE========================================================
export const state = () => ({
  /**
   * @type {User}
   */
  user: new User()
})

//= ======================================================MUTATIONS======================================================

export const mutations = {
  SET_TOKENS: (state, { access, refresh }) => {
    window.localStorage.setItem('access_token', access)
    window.localStorage.setItem('refresh_token', refresh)
  }
}

//= =======================================================ACTIONS=======================================================

export const actions = {
  async login ({ commit, dispatch }, payload) {
    const result = await this.$axios.$post('http://127.0.0.1:8000/api/token/', payload)
    commit('SET_TOKENS', result)
  }
}
//= ======================================================GETTERS========================================================

export const getters = {
  list: state => state.restaurants,
  show: state => state.restaurant
}
