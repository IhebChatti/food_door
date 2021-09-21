/* eslint-disable vue/no-multiple-template-root */
<template>
  <div class="layout has-navbar-fixed-top">
    <nav class="navbar is-fixed-top">
      <div class="container">
        <div class="navbar-brand">
          <a href="/" class="navbar-item is-size-1">
            Food Door
          </a>
          <span class="navbar-burger" data-target="navbarMenuHeroA" @click="showMobileMenu = !showMobileMenu">
            <span />
            <span />
            <span />
          </span>
        </div>
        <div id="navbarMenuHeroA" class="navbar-menu" :class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            <a class="navbar-item is-size-3" href="/Login">
              <button class="button is-dark is-large">Login</button>
            </a>
            <div class="dropdown is-hoverable">
              <div class="dropdown-trigger">
                <a class="navbar-item is-size-3" href="">
                  <button id="register_button" class="button is-dark is-large" aria-haspopup="true" aria-controls="dropdown-menu"> Register </button>
                </a>
              </div>
              <div id="dropdown-menu" class="dropdown-menu" role="menu">
                <div class="dropdown-content">
                  <a href="Sign Up_resturant" class="dropdown-item">
                    as Resturant
                  </a>
                  <hr class="dropdown-divider">
                  <a href="Sign Up_customer" class="dropdown-item">
                    as Customer
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <Hero />
    <section class="section is-large has-text-centered">
      <h1 class="title is-size-1">
        Sign up as
      </h1>
      <br>
      <br>
      <br>
      <div class="container">
        <SignupArea />
      </div>
    </section>
    <section class="section is-large has-text-centered">
      <h1 class="title">
        Resturants around you
      </h1>
      <div v-if="restaurants.length > 0">
        <div v-for="restau in restaurants" :key="restau.id">
          <ResturantCard :restaurant="restau" />
        </div>
      </div>
    </section>
    <section class="container">
      <FoodMenu />
    </section>
    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>Food Door </strong> by DA BOIS
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import FoodMenu from '../components/foodMenu.vue';
import Hero from '../components/Hero.vue';
export default {
  components: { Hero, FoodMenu },
  data () {
    return {
      showMobileMenu: false
    };
  },
  computed: {
    ...mapGetters({
      restaurants: 'restaurants/list'
    })
  },

  async mounted () {
    await this.fetchRestaurants();
  },
  methods: {
    ...mapActions({
      fetchRestaurants: 'restaurants/fetchRestaurants'
    })
  }
};
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';
#register_button{
  margin-top: 6px;
}
</style>
