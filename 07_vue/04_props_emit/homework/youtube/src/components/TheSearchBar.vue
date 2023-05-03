<template>
  <div>
    <input type="text" v-model="searchInputData"
    @keyup.enter="onSearchData">
  </div>
</template>

<script>
export default {
  name: 'TheSerachBar',
  data () {
    return {
      searchInputData : ''
    }
  },
  methods: {
    onSearchData() {
      this.$emit('the-search', this.searchInputData)
    }
  }
}
</script>

<style>

</style>