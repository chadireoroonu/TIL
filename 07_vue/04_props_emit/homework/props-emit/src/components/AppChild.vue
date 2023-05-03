<template>
  <div>
    <h1>App Child</h1>
    <input type="text" v-model="childData" @input="onChildInputData">
      <p>appData : {{ appData }}</p>
      <p>parentData : {{ parentData }}</p>
      <p>childData : {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appData : String,
    parentData : String
  },
  data() {
    return {
      childData: ''
    }
  },
  methods: {
    onChildInputData() {
      // ('이벤트 이름지정', '함께 전달할 데이터')
      this.$emit('child-input-change', this.childData)
    }
  }
}
</script>

<style>

</style>