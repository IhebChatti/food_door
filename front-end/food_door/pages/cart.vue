<template>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">
          Cart
        </h1>
      </div>
      <div class="column is-12 box">
        <table v-if="cartTotalLength" class="table is-fullwidth">
          <thead>
            <tr>
              <th>Order</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <cartItem
              v-for="item in cart.item"
              :key="item.food.id"
              :initial-item="item"
            />
          </tbody>
        </table>
        <p v-else>
          You don't have any food in your cart...
        </p>
      </div>
    </div>
  </div>
</template>

<script>
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';
</style>
