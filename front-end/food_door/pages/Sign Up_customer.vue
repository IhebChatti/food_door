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
        <form action="">
          <div class="field">
            <div class="control has-icons-left">
              <input v-model="first_name" class="input is-large" type="text" placeholder="first name">
              <span class="icon is-small is-left">
                <fa icon="users" />
              </span>
            </div>
          </div>
          <div class="field">
            <div class="control has-icons-left">
              <input v-model="last_name" class="input is-large" type="text" placeholder="last name">
              <span class="icon is-small is-left">
                <fa icon="users" />
              </span>
            </div>
          </div>
          <div class="field">
            <div class="control has-icons-left">
              <input v-model="email" class="input is-large" type="email" placeholder="email">
              <span class="icon is-small is-left">
                <fa icon="envelope" />
              </span>
            </div>
          </div>
          <div class="field">
            <div class="control has-icons-left">
              <input v-model="phone" class="input is-large" type="numbers" placeholder="phone number" autofocus="">
              <span class="icon is-small is-left">
                <fa icon="phone" />
              </span>
            </div>
          </div>
          <div class="field">
            <div class="control has-icons-left">
              <input v-model="address" class="input is-large" type="numbers" placeholder="address" autofocus="">
              <span class="icon is-small is-left">
                <fa icon="address-book" />
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
          <div class="select">
            <label class="select-label" for="select-role">Select your Role</label>
            <select id="select-role" v-model="user_types">
              <option selected disabled>
                Select dropdown
              </option>
              <option :value="user_types_choices[0].value">
                {{ user_types_choices[0].label }}
              </option>
              <option :value="user_types_choices[1].value">
                {{ user_types_choices[1].label }}
              </option>
            </select>
          </div>
        </form>
        <button class="button is-block is-warning is-large is-fullwidth signup" @click="submitRegister">
          Sign Up
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
      first_name: '',
      last_name: '',
      phone: '',
      address: '',
      email: '',
      password: '',
      user_types: -1,
      user_types_choices: [
        {
          value: 1,
          label: 'Client'
        },
        {
          value: 2,
          label: 'Restaurant'
        }
      ]
    };
  },
  methods: {
    ...mapActions({
      register: 'auth/signup'
    }),
    async submitRegister () {
      await this.register({
        email: this.email,
        password: this.password,
        first_name: this.first_name,
        last_name: this.last_name,
        phone: this.phone,
        address: this.address,
        user_types: this.user_types
      });
      this.$emit('signup');
      this.$router.push('/Login');
    }
  }
};
</script>

<style lang="scss" scoped>
@import '../node_modules/bulma';
.signup {
  margin-top: 2rem;
}
.select-label {
  float: left;
  margin-right: 1rem;
  margin-top: .5rem;
}
</style>
