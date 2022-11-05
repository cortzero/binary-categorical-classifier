import Vue from 'vue'
import App from './App.vue'
import "bootstrap"
import "bootstrap/dist/css/bootstrap.min.css";
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faCircleCheck, faCircleXmark } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

Vue.config.productionTip = false

library.add(faCircleCheck);
library.add(faCircleXmark);

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.component('font-awesome-icons', FontAwesomeIcon);
new Vue({
  render: h => h(App),
}).$mount('#app')
