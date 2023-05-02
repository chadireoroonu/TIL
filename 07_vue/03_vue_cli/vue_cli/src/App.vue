<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 사용 -->
    <MyComponent />
    <MyComponent />
    <HelloWorld msg="반가워 Vue!"/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyComponent from './components/MyComponent.vue'  // 불러오기
// .vue 생략 가능, 앞에 . 대신 @ 사용 시, src 폴더 의미
// import 뒤 이름은 그냥 변수, App 내에서만 일치시켜주면 페이지 동작

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponent,  // 등록
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
