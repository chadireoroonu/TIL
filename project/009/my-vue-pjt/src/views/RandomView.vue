<template>
  <div>
    <!-- 새 랜덤영화 가져올 버튼, 부트스트랩 적용 -->
    <button @click="newMovie" class="btn btn-success">PICK</button>
    <div class="random-movie" v-if="randomMovie">
      <!-- 영화 포스터, 제목 담은 카드 -->
      <div class="card">
        <img :src="`https://image.tmdb.org/t/p/w500${randomMovie.poster_path}`" class="card-img-top" alt="Movie Poster">
        <div class="card-body">
          <h5 class="card-title">{{ randomMovie.title }}</h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      randomMovie: null, // 랜덤 영화 정보를 저장할 변수
    }
  },
  created() {
    this.getRandomMovie() // 컴포넌트 생성 시 랜덤 영화 정보를 가져옴
  },
  methods: {
    getRandomMovie() {
      const movies = this.$store.state.movies // 모든 영화 목록 가져옴
      if (movies.length > 0) {
        const randomIndex = Math.floor(Math.random() * movies.length) // 랜덤 인덱스 생성
        this.randomMovie = movies[randomIndex] // 랜덤 영화 정보 할당
      }
    },
    newMovie() {
      this.getRandomMovie()
      }
    }
  }

</script>

<style>
.btn{
  /* 버튼 넓이 및 마진 조정 */
  margin-top: 30px;
  margin-bottom: 5px;
  width: 15rem;
}

.random-movie {
  display: flex;
  justify-content: center;
  /* 카드 높이 조정 */
  height: 60vh;
}

.card {
  width: 15rem;
  margin-bottom: 20px;
}
</style>
