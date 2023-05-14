<template>
  <div class="col-lg-4 col-md-6 mb-4">
    <!-- 카드 세로 길이 조정 목적 h-100 추가 -->
    <div class="card h-100">
      <!-- 영화 포스터, 제목, 내용 출력 -->
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="card-img-top">
      <div class="card-body">
        <h3 class="card-title">{{ movie.title }}</h3>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    // 부모 컴포넌트에 보낼 데이터
    movie: {
      type: Object,
      required: true,
    },
  },
};
</script>
