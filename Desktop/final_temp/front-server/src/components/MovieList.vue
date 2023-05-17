<template>
  <div>
    <h1>Movie List</h1>
    <MovieDetail/>
  </div>
</template>

<script>
import MovieDetail from '@/components/MovieDetail.vue'

export default {
  name: 'MovieList',
  components: {
    MovieDetail,
  }
  // store에서 모든 영화 정보 가져오기
}
</script>

<style>

</style>