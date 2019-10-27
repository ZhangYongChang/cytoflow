import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    curGates: {},
    curTubo: {}
  },
  getters: {
    getcurGates: function (state) {
      return state.curGates
    },
    getcurTubo: function (state) {
      return state.curTubo
    }
  },
  mutations: {
    deleteGateByKey: function (state, key) {
      console.log('deleteGateByKey:')
      console.log(key)
    },
    addGate: function (state, gateData) {
      console.log('addGate:')
      console.log(gateData)
    },
    updateTubo: function (state, curTobo) {
      console.log('updateTubo')
      console.log(curTobo)
    },
    resetGate: function (state, gateData) {
      console.log(gateData)
    }
  },
  actions: {
    deleteGateByKeyFun: function (context, key) {
      context.commit('deleteGateByKey', key)
    },
    addGateFun: function (context, gateData) {
      context.commit('addGate', gateData)
    },
    updateTuboFun: function (context, curTubo) {
      context.commit('updateTubo', curTubo)
    },
    resetGateFun: function (context, gateData) {
      context.commit('resetGate', gateData)
    }
  }
})

export default store
