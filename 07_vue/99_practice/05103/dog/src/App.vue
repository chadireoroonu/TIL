<template>
  <div id="app">
    <h1>Dog API</h1>
    <button @click="getDogImage">Get Dog</button>
    <DogImage/>
    <DogImageItem/>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
import DogImage from './components/DogImage.vue'
import DogImageItem from './components/DogImageItem.vue'

export default {
  name: 'App',
  components: {
    DogImage,
    DogImageItem,
  },
  methods: {
    getDogImage() {
      // console.log('getDogImage')
      this.$store.dispatch('getDogImage')
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
