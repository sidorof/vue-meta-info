import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
const baseUrl = 'http://localhost:5000'
const apiUrl = baseUrl + '/api/v1/'
const apiMetaUrl = apiUrl + 'meta/'
Vue.use(Vuex)
Vue.prototype.$http = axios

const state = {
  classList: {},
  class: null,
  resources: [],
  resource: null,
  currentMethod: null,
  tab: null
}

export const mutations = {
  clearClass (state) {
    state.class = null
  },
  setClass (state, payload) {
    state.class = payload
  },
  setClassList (state, payload) {
    state.classList = payload
  },
  clearResource (state) {
    state.resource = null
  },
  setResource (state, payload) {
    state.resource = payload
  },
  setResources (state, payload) {
    state.resources = payload.resources
  },
  clearCurrentMethod (state) {
    state.currentMethod = null
  },
  setTab (state, payload) {
    state.tab = payload
  }
}

export const actions = {

  clearClass ({ commit }) {
    commit('clearClass')
  },
  loadClass ({ commit }, payload) {
    commit('setLoading', true, { root: true })
    commit('clearError', null, { root: true })
    commit('clearClass')
    axios({
      method: 'get',
      url: apiMetaUrl + 'classes/' + payload.name,
      params: {},
      headers: {
        'Content-type': 'application/json'
        // 'Authorization': 'Bearer ' + localStorage.getItem('auth_token')
      }
    })
      .then(response => {
        commit(
          'setClass',
          {
            name: payload.name,
            ...response.data[payload.name]
          }
        )
      })
      .catch(function (error) {
        console.log('error', error)
        commit('setError', error.message, { root: true })
      })
    commit('setLoading', false, { root: true })
  },
  loadClassList ({ commit }) {
    axios({
      method: 'get',
      url: apiMetaUrl + 'classes',
      headers: {
        'Content-type': 'application/json'
        // 'Authorization': 'Bearer ' + localStorage.getItem('auth_token')
      }
    })
      .then(response => {
        commit('setClassList', response.data.classes)
      })
      .catch(function (error) {
        console.log('error occurred')
        console.log('error', error.message)
        console.log('error', error.config)
        // commit('setError', error.response.message, { root: true })
      })
  },
  clearResource ({ commit }) {
    commit('clearResource')
  },
  loadResource ({ commit }, payload) {
    commit('setLoading', true, { root: true })
    commit('clearError', null, { root: true })
    commit('clearClass')
    axios({
      method: 'get',
      url: baseUrl + payload.metaUrl,
      params: {},
      headers: {
        'Content-type': 'application/json'
        // 'Authorization': 'Bearer ' + localStorage.getItem('auth_token')
      }
    })
      .then(response => {
        commit(
          'setResource',
          { name: payload.name, ...response.data }
        )
      })
      .catch(function (error) {
        console.log('error', error)
        commit('setError', error.message, { root: true })
      })
    commit('setLoading', false, { root: true })
  },
  loadResources ({ commit }) {
    // not commit, does not save the list
    commit('setLoading', true, { root: true })
    commit('clearError', null, { root: true })
    axios({
      method: 'get',
      url: apiMetaUrl.slice(0, -1),
      headers: {
        'Content-type': 'application/json'
        // 'Authorization': 'Bearer ' + localStorage.getItem('auth_token')
      }
    })
      .then(response => {
        commit('setResources', response.data)
      })
      .catch(function (error) {
        console.log('error occurred')
        console.log('error', error.message)
        console.log('error', error.config)
        commit('setError', error.response.message, { root: true })
      })
  },
  setCurrentMethod ({ commit }, payload) {
    commit('setCurrentMethod', payload)
  },
  clearCurrentMethod ({ commit }) {
    commit('clearCurrentMethod')
  }
}

export const getters = {

  getClass (state) {
    return state.class
  },
  getClassList (state) {
    return state.classList
  },
  getResource (state) {
    return state.resource
  },
  getResources (state) {
    return state.resources
  },
  getCurrentMethod (state) {
    const method = Object.keys(state.resource.methods)[state.tab]
    return state.resource.methods[method]
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
