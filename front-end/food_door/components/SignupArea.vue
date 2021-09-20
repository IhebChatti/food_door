<template>
  <div class="container">
    <div class="columns">
      <div class="column">
        <div class="container has-text-centered">
          <h1 class="title">
            A Resturant
          </h1>
          <img
            class="image is-4by6"
            src="https://i.ibb.co/1M5tj0t/27-277542-image-cartoon-pictures-of-restaurants.png"
            alt="resturant"
          >
          <p> If you are a resturant owner we offer you a place to sell your food</p>
          <br>
          <br>
          <a href="Sign Up_resturant"><button class="button is-success"> Sign up</button></a>
        </div>
      </div>
      <div class="column">
        <div class="container has-text-centered">
          <h1 class="title">
            A Customer
          </h1>
          <img
            class="image is-4by6
"
            src="https://i.ibb.co/tL0T5rq/png-transparent-hungry-girl-hunger-woman-woman-black-hair-people-cartoon-3.png"
            alt="resturant"
          >
          <p> If you are just a regular customer looking to order your favorite meal sign up here </p>
          <br>
          <a href="Sign Up_customer"><button class="button is-info"> Sign up</button></a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  setup () {
    return {}
  }
}
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';
</style>
