import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _4dd52495 = () => interopDefault(import('../pages/cart.vue' /* webpackChunkName: "pages/cart" */))
const _640fe6d3 = () => interopDefault(import('../pages/food.vue' /* webpackChunkName: "pages/food" */))
const _73b53a24 = () => interopDefault(import('../pages/Login.vue' /* webpackChunkName: "pages/Login" */))
const _62cf152a = () => interopDefault(import('../pages/myAccountResturant.vue' /* webpackChunkName: "pages/myAccountResturant" */))
const _5c66d194 = () => interopDefault(import('../pages/Sign Up_customer.vue' /* webpackChunkName: "pages/Sign Up_customer" */))
const _59545010 = () => interopDefault(import('../pages/Sign Up_resturant.vue' /* webpackChunkName: "pages/Sign Up_resturant" */))
const _329b772d = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/cart",
    component: _4dd52495,
    name: "cart"
  }, {
    path: "/food",
    component: _640fe6d3,
    name: "food"
  }, {
    path: "/Login",
    component: _73b53a24,
    name: "Login"
  }, {
    path: "/myAccountResturant",
    component: _62cf152a,
    name: "myAccountResturant"
  }, {
    path: "/Sign%20Up_customer",
    component: _5c66d194,
    name: "Sign Up_customer"
  }, {
    path: "/Sign%20Up_resturant",
    component: _59545010,
    name: "Sign Up_resturant"
  }, {
    path: "/",
    component: _329b772d,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
