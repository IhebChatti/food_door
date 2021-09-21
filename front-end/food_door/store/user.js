import User from "../models/user";

export const state = () => ({
  users: [],
  user: new User()
});

export const mutations = {
  SET_INDEX: (state, payload) =>
    (state.users = payload.map(user => new User(user))),
  SET_SHOW: (state, payload) => (state.user = new User(payload)),
  SET_DELETE: (state, payload) => {
    const index = state.users.findIndex(user => (user.id = payload));
    state.users.splice(index, 1);
  },
  ADD_USER: (state, payload) => state.users.push(payload)
};

export const actions = {
  async fetchUsers({ commit }) {
    const payload = await this.$axios.$get("http://127.0.0.1:8000/list_users");
    commit("SET_INDEX", payload);
  },
  async fetchUser({ commit }, id) {
    const payload = await this.$axios.$get("http://127.0.0.1:8000/get_user", {
      params: { user_id: id }
    });
    commit("SET_SHOW", payload);
  },
  async deleteUser({ commit }, id) {
    await this.$axios.$delete("http://127.0.0.1:8000/delete_user", {
      params: { user_id: id }
    });
    commit("SET_DELETE", id);
  },
  async createFood({ commit }, user) {
    const payload = await this.$axios.$post(
      "http://127.0.0.1:8000/create_user",
      user
    );
    commit("ADD_USER", payload);
  }
};

export const getters = {
  list: state => state.users,
  show: state => state.user
};
