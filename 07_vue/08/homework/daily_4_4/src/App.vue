<template>
  <div id="app">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500&display=swap" rel="stylesheet">
    <h1>SSAFY TUBE</h1>
    <iframe :src="`https://youtube.com/embed/${video}`" frameborder="0" id="video"></iframe>
    <p id="title">{{ title }}</p>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      video: null,
      title: '',
    }
  },
  methods: {
    ssafyTube() {
      axios
      .get('https://www.googleapis.com/youtube/v3/search', {
        params: {
          key: 'AIzaSyAkgkAqWog8uMp4TkiOK8No5PkEfTbaBsM',
          part: 'snippet',
          type: 'video',
          q: '코딩노래'
          }
        }
      )
      .then(temp => {
        console.log(temp)
        this.video = temp.data.items[0].id.videoId
        this.title = temp.data.items[0].snippet.title
      })
      .catch(error => {
        console.error(error)
      })
    } 
  },
  created() {
    this.ssafyTube()
  }
}
</script>

<style>
#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgb(0, 110, 255);
  margin-top: 60px;
}
#title {
  font-family: 'Noto Sans KR', sans-serif;
  color: rgb(112, 112, 112);
  border: 1px solid rgb(112, 112, 112);
}
</style>
