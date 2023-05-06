<template>
  <div id="app">
    <h1>점심메뉴</h1>
    <button @click="selectMenu">Pick One</button>
    <p>{{ menu }}</p>
    <hr>
    <h1>로또</h1>
    <button @click="selectNumbers">Get Lucky Numbers</button><br>
    <p v-if="numbers.length===6">{{ numbers }}</p>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      menuList: ['국밥', '피자', '돈까스', '햄버거', '치킨', '갈비', '삼겹살'],
      menu: '',
      numbers: []
    }
  },
  methods: {
    selectMenu() {
      const randomMenu = Math.floor(Math.random() * 7);
      this.menu = this.menuList[randomMenu]
    },
    selectNumbers() {
      const numbers = []
      while (numbers.length < 6) {
        const randomNumber = Math.floor(Math.random() * 45) + 1
        if (!numbers.includes(randomNumber)) {
          numbers.push(randomNumber)
        }
      } this.numbers = numbers
    }
  }
}
</script>

<style>

</style>
