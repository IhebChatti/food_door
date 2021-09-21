import Order from "../models/order";

export const state = () => ({
  orders: [],
  order: new Order()
});

export const mutations = {
  SET_INDEX: (state, payload) =>
    (state.orders = payload.map(order => new Order(order))),
  SET_SHOW: (state, payload) => (state.food = new Order(payload)),
  SET_DELETE: (state, payload) => {
    let index = state.orders.findIndex(order => (order.id = payload));
    state.orders.splice(index, 1);
  },
  ADD_ORDER: (state, payload) => state.orders.push(payload)
};

export const actions = {
  async fetchorders({ commit }) {
    const payload = await this.$axios.$get("http://127.0.0.1:8000/list_orders");
    commit("SET_INDEX", payload);
  },
  async fetchOrder({ commit }, id) {
    const payload = await this.$axios.$get("http://127.0.0.1:8000/get_order", {
      params: { order_id: id }
    });
    commit("SET_SHOW", payload);
  },
  async deleteOrder({ commit }, id) {
    await this.$axios.$delete("http://127.0.0.1:8000/delete_order", {
      params: { order_id: id }
    });
    commit("SET_DELETE", id);
  },
  async createOrder({ commit }, order) {
    const payload = await this.$axios.$post(
      "http://127.0.0.1:8000/create_order",
      order
    );
    commit("ADD_ORDER", payload);
  }
};

export const getters = {
  list: state => state.orders,
  show: state => state.order
};
