<template>
  <div id="app">
    <p>counter : {{ number }}</p>
    <p>double counter : {{ doubleNumber }}</p>
    <button @click="increase">increase ++</button>
    <button @click="decrease">decrease --</button>
  </div>
</template>

<script>


export default {
  name: 'App',
  data() {
    return {
      number : 0
    }
  },
  created() {
    this.increase()
  },
  mountued() {},
  methods: {
    increase() {
      this.number += 1
    },
    decrease() {
      this.number -=1
    }
  },
  computed: {
    doubleNumber() {
      return this.number * 2
    }
  },
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
