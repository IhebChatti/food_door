<template>
  <div class="container">
    <div class="nav-wrapper">
      <nav class="navbar">
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
              <div class="dropdown">
                <div class="dropdown-trigger">
                  <button class="button" aria-haspopup="true" aria-controls="dropdown-menu3">
                    <span> My account</span>
                    <span class="icon is-small">
                      <i class="fas fa-angle-down" aria-hidden="true" />
                    </span>
                  </button>
                </div>
                <div id="dropdown-menu3" class="dropdown-menu" role="menu">
                  <div class="dropdown-content">
                    <a href="#" class="dropdown-item">
                      Dashboard
                    </a>
                    <hr class="dropdown-divider">
                    <a href="#" class="dropdown-item">
                      Logout
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>
    <div class="tabs is-large">
      <ul>
        <li class="is-active">
          <a href="#form">Add food</a>
        </li>
        <li><a href="#food_list">Food list</a></li>
      </ul>
    </div>
    <div class="form">
      <form action="">
        <div class="field">
          <label class="label">Name</label>
          <div class="control">
            <input class="input" type="text" placeholder="Text input">
          </div>
        </div>
        <div class="field">
          <label class="label">description</label>
          <div class="control">
            <input class="input" type="text" placeholder="Text input">
          </div>
        </div>
        <div class="field">
          <label class="label">Price</label>
          <div class="control">
            <input class="input" type="text" placeholder="Text input">
          </div>
        </div>
        <div class="file is-large">
          <label class="file-label">
            <input class="file-input" type="file" name="resume">
            <span class="file-cta">
              <span class="file-icon">
                <i class="fas fa-upload" />
              </span>
              <span class="file-label">
                Upload photo
              </span>
            </span>
          </label>
        </div>
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
  </div>
</template>

<script>
export default {
  data () {
    return {
      showMobileMenu: false
    };
  }
};
</script>

<style lang="scss" scoped>

</style>
