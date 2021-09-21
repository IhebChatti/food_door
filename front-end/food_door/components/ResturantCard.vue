<template>
  <div class="container">
    <div class="columns is-variable">
      <div class="column">
        <div class="card">
          <div class="card-image">
            <figure v-if="restaurant.images[0]" class="image">
              <img :src="restaurant.images[0].image" alt="Placeholder image">
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-content">
                <p class="title is-4">
                  {{ restaurant.name }}
                </p>
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
