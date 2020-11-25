import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movie: '',
    selectedMovie: 2,
    drawerState: false,
    login: false,
  },
  mutations: {
    toggleDrawerState (state, data) {
      state.drawerState = data
    }
  },
  getters : {
    drawerState: (state) => state.drawerState
  },
  actions: {
  },
  modules: {
  }
})
