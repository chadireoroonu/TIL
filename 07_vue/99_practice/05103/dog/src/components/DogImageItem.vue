<template>
  <div>
    <img :src="image" class="dog-image">
  </div>
</template>

<script>
export default {
  props: {
    image: String
  }
}
</script>

<style>
.dog-image {
  width: 350px;
  height: 300px;
  border: none;
  outline: none;
  box-shadow: none;
}
</style>