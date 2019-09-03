import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

var state = {
  count: 1
}

var mutations = {
  intCount() {
    ++state.count
  }
}

var getters = {

}

var actions = {

}

const store = new Vuex.store({
  state,
  mutations,
  getters,
  actions
})

export default store