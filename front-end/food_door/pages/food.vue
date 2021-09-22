<template>
  <div class="container">
    <div class="nav-wrapper">
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
                <button class="button is-dark is-large">logout</button>
              </a>
            </div>
          </div>
        </div>
      </nav>
    </div>
    <section class="food-listing">
      <FoodMenu />
    </section>
  </div>
</template>

<script>
import foodMenu from '../components/foodMenu.vue';
export default {
  components: { foodMenu },
  data () {
    return {
      showMobileMenu: false
    };
  }
};
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';
</style>
