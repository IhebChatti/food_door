/* eslint-disable vue/no-multiple-template-root */
<template>
  <div class="layout has-navbar-fixed-top">
    <nav class="navbar is-fixed-top">
      <div class="container">
        <div class="navbar-brand">
          <a href="#" class="navbar-item is-size-1">
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
import Hero from '../components/Hero.vue'
import {mapActions, mapGetters} from "vuex";
export default {
  components: { Hero },
  data () {
    return {
      showMobileMenu: false,
    }
  },
  methods: {
    ...mapActions({
      fetchRestaurants: 'restaurants/fetchRestaurants',
    }),
  },
  computed: {
    ...mapGetters({
      restaurants: 'restaurants/list',
    })
  },
  async mounted() {
    await this.fetchRestaurants();
  },
}
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';
</style>
