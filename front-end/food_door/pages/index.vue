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
        <div v-show="userType == -1" id="navbarMenuHeroA" class="navbar-menu" :class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            <a class="navbar-item is-size-3" href="/Login">
              <button class="button is-dark is-large">Login</button>
            </a>
            <a class="navbar-item is-size-3" href="Sign Up_customer">
              <button class="button is-dark is-large">Register</button>
            </a>
          </div>
        </div>
        <div v-show="userType == 2 || userType == 1" id="navbarMenuHeroA" class="navbar-menu" :class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            <div class="dropdown is-hoverable">
              <div class="dropdown-trigger">
                <button class="button is-dark is-large account_m" aria-haspopup="true" aria-controls="dropdown-menu3">
                  My account
                </button>
              </div>
              <div id="dropdown-menu3" class="dropdown-menu" role="menu">
                <div class="dropdown-content">
                  <a href="myAccountResturant" class="dropdown-item">
                    Dashboard
                  </a>
                  <hr class="dropdown-divider">
                  <a class="dropdown-item" @click="logout">
                    Logout
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <Hero />
    <section v-show="userType == 2 || userType == 1" class="section is-large has-text-centered">
      <h1 class="title">
        Resturants around you
      </h1>
      <div v-if="restaurants.length > 0">
        <div v-for="restau in restaurants" :key="restau.id">
          <ResturantCard :restaurant="restau" />
        </div>
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
import { mapActions, mapGetters } from 'vuex';
import Hero from '../components/Hero.vue';
export default {
  components: { Hero },
  data () {
    return {
      showMobileMenu: false,
      userType: -1
    };
  },
  computed: {
    ...mapGetters({
      restaurants: 'restaurants/list'
    })
  },

  async mounted () {
    await this.fetchRestaurants();
    if (window.localStorage.user_types === '1') {
      this.userType = 1;
    } else if (window.localStorage.user_types === '2') {
      this.userType = 2;
    } else {
      this.userType = -1;
    }
  },
  methods: {
    ...mapActions({
      fetchRestaurants: 'restaurants/fetchRestaurants',
      logout: 'auth/logout'
    })
  }
};
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';
#register_button{
  margin-top: 6px;
}
.account_m{
  margin-top: 6px;
}
</style>
