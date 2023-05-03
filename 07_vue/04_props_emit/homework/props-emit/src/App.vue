<template>
  <div id="app">
    <h1>APP</h1>
    <input type="text" v-model="appData">
      <p>AppData : {{ appData }}</p>
      <p>childData : {{ childData }}</p>
    <AppParent
      @child-input-change="onChildInputData" 
      :app-data="appData"
    />
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent
  },
  data() {
    return {
      appData: '',
      childData: '',
    }
  },
  methods: {
    onChildInputData(childInputData) {
      this.childData = childInputData
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
