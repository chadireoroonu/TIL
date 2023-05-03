<template>
  <!-- 루트 element가 단 하나 존재해야 함 -->
  <div>
    <h1>App Parent</h1>
    <input type="text" v-model="parentData">
      <p>AppData : {{ appData }}</p>
      <p>childData : {{ childData }}</p>
    <AppChild
      @child-input-change="onChildInputData"
      :app-data="appData"
      :parent-data="parentData"
    />
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  name: 'AppParent',
  props: {
    appData: String
  },
  data() {
    return {
      parentData: '',
      childData: '',
    }
  },
  components: {
    AppChild
  },
  methods: {
    onChildInputData(childInputData) {
      this.childData = childInputData
      this.$emit('child-input-change', childInputData)
    }
  }
}
</script>

<style>

</style>