<template>
  <div>
    <h1>Article View</h1>
      <ul>
        <li v-for="article in articles" :key="article.id">
          {{ article.title }}
        </li>
      </ul>
  </div>
</template>

<script>
export default {
  computed: {
    articles() {
      // store에서 articles 가져오기
      return this.$store.getters.getArticles
    }
  },
  created() {
    this.$store.dispatch('fetchArticles')
  }
}
</script>

<style>

</style>