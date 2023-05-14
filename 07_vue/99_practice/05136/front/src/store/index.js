import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articles: [],
  },
  getters: {
    getArticles(state) {
      // articles 상태 반환
      return state.articles
    }
  },
  mutations: {
    setArticles(state, articles) {
      // article 정보 state에 업데이트
      state.articles = articles
    }
  },
  actions: {
    async fetchArticles({ commit }) {
      // 백엔드에서 데이터 가져올 경로
      const response = await axios.get('/api/v1/')
      // 가져온 데이터 state 반영을 위한 mutatios 호출
      commit('setArticles', response.data)
    }
  },
  modules: {
  }
})
