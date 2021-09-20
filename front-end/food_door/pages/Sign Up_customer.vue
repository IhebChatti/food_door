<template>
  <div class="hero is-fullheight is-info">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="column is-8 is-offset-2" />
        <h3 class="title has-text-white">
          Welcome
        </h3>
        <hr class="login-hr">
        <p class="subtitle has-text-white">
          Your food awaits you
        </p>
        <div class="box">
          <div class="box">
            <img src="https://i.ibb.co/r5vp0Jg/Screenshot-from-2021-09-15-02-52-53.png">
          </div>
          <div class="title has-text-grey is-5">
            Please fill this form
          </div>
        </div>
        <form>
          <div class="field">
            <div class="control has-icons-left">
              <input class="input is-large" type="text" placeholder="name" autofocus="">
              <span class="icon is-small is-left">
                <fa icon="users" />
              </span>
            </div>
          </div>
          <div class="field">
            <div class="control has-icons-left">
              <input class="input is-large" type="email" placeholder="email" autofocus="">
              <span class="icon is-small is-left">
                <fa icon="envelope" />
              </span>
            </div>
          </div>
          <div class="field">
            <div class="control has-icons-left">
              <input class="input is-large" type="numbers" placeholder="phone number" autofocus="">
              <span class="icon is-small is-left">
                <fa icon="phone" />
              </span>
            </div>
          </div>
          <div class="field">
            <div class="control has-icons-left">
              <input class="input is-large" type="password" placeholder="Password">
              <span class="icon is-small is-left">
                <fa icon="lock" />
              </span>
            </div>
          </div>
        </form>
        <label class="checkbox remember_me" style="margin: 20px;">
          <input type="checkbox">
          Remember me
        </label>
        <button class="button is-block is-warning is-large is-fullwidth">
          Sign Up
        </button>
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
