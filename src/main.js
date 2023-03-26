import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';


import VueRouter from 'vue-router'
import router from './router' 
Vue.use(VueRouter) 
Vue.use(MuseUI);
axios.defaults.baseURL = 'http://127.0.0.1:5000'; 
Vue.prototype.$ajax = axios;
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router:router,
}).$mount('#app')
