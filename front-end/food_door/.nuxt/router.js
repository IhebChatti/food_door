import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _022406f6 = () => interopDefault(import('../pages/cart.vue' /* webpackChunkName: "pages/cart" */))
const _4942a3e3 = () => interopDefault(import('../pages/Login.vue' /* webpackChunkName: "pages/Login" */))
const _368db9cb = () => interopDefault(import('../pages/myAccountResturant.vue' /* webpackChunkName: "pages/myAccountResturant" */))
const _17182a75 = () => interopDefault(import('../pages/Sign Up_customer.vue' /* webpackChunkName: "pages/Sign Up_customer" */))
const _1663d962 = () => interopDefault(import('../pages/Sign Up_resturant.vue' /* webpackChunkName: "pages/Sign Up_resturant" */))
const _0828e0ec = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _022406f6,
    name: "cart"
  }, {
    path: "/Login",
    component: _4942a3e3,
    name: "Login"
  }, {
    path: "/myAccountResturant",
    component: _368db9cb,
    name: "myAccountResturant"
  }, {
    path: "/Sign%20Up_customer",
    component: _17182a75,
    name: "Sign Up_customer"
  }, {
    path: "/Sign%20Up_resturant",
    component: _1663d962,
    name: "Sign Up_resturant"
  }, {
    path: "/",
    component: _0828e0ec,
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
