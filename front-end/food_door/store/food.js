import FoodItem from '../models/food';

export const state = () => ({
  foods: [],
  food: new FoodItem(),
});

export const mutations = {
  SET_INDEX: (state, payload) =>
    (state.foods = payload.map((food) => new FoodItem(food))),
  SET_SHOW: (state, payload) => (state.food = new FoodItem(payload)),
  SET_DELETE: (state, payload) => {
    let index = state.foods.findIndex((food) => (food.id = payload));
    state.foods.splice(index, 1);
  },
  ADD_FOOD: (state, payload) => state.foods.push(payload),
};

export const actions = {
  async fetchFoods({ commit }) {
    const payload = await this.$axios.$get('http://127.0.0.1:8000/list_food');
    commit('SET_INDEX', payload);
  },
  async fetchFood({ commit }, id) {
    const payload = await this.$axios.$get('http://127.0.0.1:8000/get_food', {
      params: { food_id: id },
    });
    commit('SET_SHOW', payload);
  },
  async deleteFood({ commit }, id) {
    await this.$axios.$delete('http://127.0.0.1:8000/delete_food', {
      params: { food_id: id },
    });
    commit('SET_DELETE', id);
  },
  async createFood({ commit }, food) {
    const payload = await this.$axios.$post(
      'http://127.0.0.1:8000/create_food',
      food
    );
    commit('ADD_FOOD', payload);
  },
};

export const getters = {
  list: (state) => state.foods,
  show: (state) => state.food,
};
