<template>
  <div id="app">
    <div>
      <h1>My first youtube project</h1>
        <TheSearchBar
          @the-search="onSearchData"
        />
    </div>
  </div>
</template>

<script>
import TheSearchBar from './components/TheSearchBar.vue'

export default {
  name: 'App',
  components: {
    TheSearchBar
  },
  data() {
    return {
      searchData: ''
    }
  },
  methods: {
    onSearchData(searchInputData) {
      this.searchData = searchInputData
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
