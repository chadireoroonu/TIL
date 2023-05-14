import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: []
  },
  getters: {
  },
  mutations: {
    SET_MOVIES(state, movies) {
      state.movies = movies
    }
  },
  actions: {
    getMovies({ commit }) {
      axios.get('https://api.themoviedb.org/3/movie/top_rated', {
        params: {
          api_key: 'fa9034a3d887b37f550a9dcb9401884f'
        }
      })
      .then(response => {
        const movies = response.data.results
        commit('SET_MOVIES', movies)
      })
    }
  },
  modules: {
  }
})
