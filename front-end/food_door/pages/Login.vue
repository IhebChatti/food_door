<template>
  <div class="hero is-fullheight is-dark">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="column is-8 is-offset-2" />
        <h3 class="title has-text-white">
          Welcome
        </h3>
        <hr class="login-hr">
        <p class="subtitle has-text-white">
          Your Food is waiting
        </p>
        <div class="box">
          <div class="box">
            <img src="https://i.ibb.co/r5vp0Jg/Screenshot-from-2021-09-15-02-52-53.png">
          </div>
          <div class="title has-text-grey is-5">
            Please enter your email and password.
          </div>
        </div>
        <form ref="observer-form">
          <div class="field">
            <div class="control has-icons-left">
              <input v-model="email" class="input is-large" type="email" placeholder="Email" autofocus="">
              <span class="icon is-small is-left">
                <fa icon="envelope" />
              </span>
            </div>
          </div>
          <div class="field">
            <div class="control has-icons-left">
              <input v-model="password" class="input is-large" type="password" placeholder="Password">
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
        <button class="button is-block is-primary is-large is-fullwidth" @click="submitLogin">
          Login
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data () {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    ...mapActions({
      login: 'auth/login'
    }),

    async submitLogin () {
      const payload = {
        email: this.email,
        password: this.password
      };
      await this.login(payload);
      this.$emit('login');
      this.$router.push('/');
    },

    clickSignUp () {
      this.$emit('signup');
    }
  }
};
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';

:hover.remember_me{
    color: white;
}
</style>
