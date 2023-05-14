<template>
  <div>
    <!-- <h1>Movie View</h1> -->
    <!-- 영화카드들을 담을 컨테이너 -->
    <div class="container">
      <div class="row">
        <!-- MovieCard 컴포넌트 반복출력, 키는 영화 id -->
        <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
      </div>
    </div>
  </div>
</template>

<script>
// MovieCard 컴포넌트 가져오기
import MovieCard from './MovieCard.vue'

export default {
  components: {
    // MovieCard를 자식 컴포넌트로 등록
    MovieCard,
  },
  computed: {
    // vuex 상태의 movies 반환
    movies() {
      return this.$store.state.movies
    },
  },
  // created에서 영화 데이터 가져오기
  created() {
    this.$store.dispatch('getMovies').then(() => {
      // 영화 데이터 보여주는 메서드 실행
      this.show()
    })
  },
  methods: {
    show() {
      const movieList = document.querySelector('#movie-list')
      // movieList 요소가 있으면 보여주기
      if (movieList) {
        movieList.style.display = 'block'
      }
    },
  },
};
</script>

<style>
.container {
  margin-top: 20px;
}
</style>
