<template>
  <div>
    <DogImageItem v-for="(image, idx) in dogImageList" :key="idx" :image="image"/>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import DogImageItem from './DogImageItem.vue'

export default {
  components: {
    DogImageItem,
  },
  computed: {
    ...mapState(['dogImageList']),
  }
}
</script>

<style>

</style>