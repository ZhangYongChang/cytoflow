// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
import echarts from 'echarts'
import ecStat from 'echarts-stat'

Vue.prototype.$axios = axios
Vue.prototype.$echarts = echarts
Vue.prototype.$ecStat = ecStat
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})