<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div>
      <header>
        <h2>예약 페이지</h2>
      </header>
      <section>
        <div>
          <h3>시간 선택</h3>
          <ul class="time-table">
            <li v-for="time in times" :key="time"
            @click="onClick(time)" class="item"
            :class="{'selected' : isSelected(time)}">
              {{ time }}
            </li>
          </ul>
        </div>
        <div class="selected-time">
          <hr>
          <h3>선택 시간 : 
            <span>{{ selectedTime }}</span>
          </h3>
        </div>
      </section>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      times:[
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectedTime: [],
    }
  },
  methods: {
    onClick(time) {
      if (this.selectedTime.includes(time)){
        const idx = this.selectedTime.indexOf(time)
        // 추가 공부 필요
        this.selectedTime.splice(idx, 1)
      } else {
        if (this.selectedTime.length === 5) {
          alert('5타임까지만 신청할 수 있습니다.')
          return
        }
        this.selectedTime.push(time)
      }
    },
    isSelected(time) {
      if (this.selectedTime.includes(time)) {
        return true
      } else {
        return false
      }
    }
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
.time-table {
  display: flex;
  width: 500px;
  flex-wrap: wrap;
  list-style: none;
}
.item {
  padding: 10px;
}
.selected {
  background-color: skyblue;
  font-weight: bold;
}
</style>