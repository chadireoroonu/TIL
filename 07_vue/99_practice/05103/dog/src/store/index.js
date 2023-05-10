import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    dogImageList: [],
  },
  getters: {
    setDogImages: state => state.dogImageList
  },
  mutations: {
    setDogImage(state, image) {
      state.dogImageList.push(image)
    }
  },
  actions: {
    getDogImage({ commit }) {
      axios
      .get('https://dog.ceo/api/breeds/image/random')
      .then((response)=> {
        const image = response.data.message;
        commit('setDogImage', image)
        console.log(response.data.message)
      })
      .catch((error) => {
        console.error(error)
      })
    } 
  },
})
