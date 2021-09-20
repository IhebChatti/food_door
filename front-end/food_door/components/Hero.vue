<template>
  <section class="hero is-primary is-fullheight header-image">
    <!-- Hero content: will be in the middle -->
    <div class="hero-body">
      <div class="container has-text-centered">
        <a href="#">
          <img src="https://i.ibb.co/r5vp0Jg/Screenshot-from-2021-09-15-02-52-53.png" alt="">
        </a>
        <p class="subtitle has-text-black">
          Bring food right to your door
        </p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.header-image {
    background-image: url("https://www.nicerx.com/fast-food-capitals/assets/img/bg.jpg");
    background-position: center center;
    background-attachment: fixed;
    background-size: cover;
}
html {
    height: 100%;
    width: 100%;
}
</style>
