import Vue from 'vue'
import { library, config } from '@fortawesome/fontawesome-svg-core'
import {
  FontAwesomeLayers,
  FontAwesomeLayersText,
  FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'

import {
  faEnvelope as freeFasFaEnvelope,
  faLock as freeFasFaLock,
  faUsers as freeFasFaUsers,
  faPhone as freeFasFaPhone,
  faAddressBook as freeFasFaAddressBook
} from '@fortawesome/free-solid-svg-icons'

library.add(
  freeFasFaEnvelope,
  freeFasFaLock,
  freeFasFaUsers,
  freeFasFaPhone,
  freeFasFaAddressBook
)

config.autoAddCss = false

Vue.component('fa', FontAwesomeIcon)
Vue.component('faLayers', FontAwesomeLayers)
Vue.component('faLayersText', FontAwesomeLayersText)
