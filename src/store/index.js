import Vue from 'vue'
import Vuex from 'vuex'

import metaStore from './modules/meta'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loading: false,
    error: null
  },
  mutations: {
    setLoading (state, payload) {
      state.loading = payload
    },
    setError (state, payload) {
      // format: {message: error}
      state.error = payload
    },
    clearError (state) {
      state.error = null
    }
  },
  actions: {
    clearError ({ commit }) {
      commit('clearError')
    },
    setError ({ commit }, payload) {
      commit('setError', payload)
    }
  },
  getters: {
    loading (state) {
      return state.loading
    },
    error (state) {
      return state.error
    }
  },
  modules: {
    meta: metaStore
  }
})
