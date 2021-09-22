<template>
  <div class="columns is-variable is-1-mobile is-0-tablet is-3-desktop is-8-widescreen is-2-fullhd">
    <div class="column is-half is-centered">
      <div class="card">
        <div class="card-image">
          <figure v-if="restaurant.images[0]" class="image is-16by9">
            <img :src="restaurant.images[0].image" alt="Placeholder image">
          </figure>
        </div>
        <div class="card-content is-right">
          <div class="media">
            <div class="media-content">
              <a href="food">
                <p class="title is-4">
                  {{ restaurant.name }}
                </p>
              </a>
              <p class="subtitle is-6">
                {{ restaurant.address }}
              </p>
            </div>
          </div>
          <div class="content">
            {{ restaurant.description }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Restaurant from '@/models/restaurant';
export default {
  props: {
    // eslint-disable-next-line vue/require-default-prop
    restaurant: new Restaurant()
  }
};
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';
</style>
