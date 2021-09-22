<template>
  <div class="container">
    <form action="">
      <div class="field">
        <label class="label">Name</label>
        <div class="control">
          <input class="input" type="text" placeholder="Text input">
        </div>
      </div>
      <div class="field">
        <label class="label">if you have any prefrence please add it here </label>
        <div class="control">
          <textarea class="textarea" placeholder="Textarea" />
        </div>
      </div>
      <p class="price">
        price placeholder
      </p>
      <div class="field is-grouped">
        <div class="control">
          <button class="button is-link">
            Submit
          </button>
        </div>
        <div class="control">
          <button class="button is-link is-light">
            Cancel
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';

.container{
  width: 50%;
  height: 50%;
  margin-top: 15%;
}
</style>
