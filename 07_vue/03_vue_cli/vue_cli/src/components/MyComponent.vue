<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild />
    <MyChild />
    <MyChild />
    <MyChild />
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent', // 개발자도구 vue에서 볼 이름
  components : {
    MyChild,
  }
}
</script>

<style>
.border {
  border: solid;
}
</style>