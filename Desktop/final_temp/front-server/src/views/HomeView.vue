<template>
  <div class="home">
    <MyMovieImage/>
    <ChoiceList/>
    <MyMovieList/>
  </div>
</template>

<script>
// @ is an alias to /src
import MyMovieImage from '@/components/MyMovieImage.vue'
import ChoiceList from '@/components/ChoiceList.vue'
import MyMovieList from '@/components/MyMovieList.vue'

export default {
  name: 'HomeView',
  components: {
    MyMovieImage,
    ChoiceList,
    MyMovieList,
  }
}
</script>
