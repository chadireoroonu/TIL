<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class="card">
      <header>
        <h2>예약 페이지</h2>
      </header>
      <section>
        <div class="time-table">
          <h3>시간 선택</h3>
          <ul class="time-table-list">
            <li v-for="time in times" :key="time" @click="onClick(time)" class="list-item" :class="{'selected': isSelected}">
              {{ time }}
            </li>
          </ul>
        </div>
        <div class="selected-time">
          <h3>
            선택 시간 :
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
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectedTime: [],
    }
  },
  methods : {
    onClick(time) {
      if (this.selectedTime.includes(time)) {
        // 이미 선택되어 있다면 목록에서 제거
        // 제거 대상 인덱스 찾기
        const idx = this.selectedTime.indexOf(time)
        this.selectedTime.splice(idx, 1)

      } else {
        if (this.selectedTime.length === 5) {
          alert('최대 5개까지 선택 가능합니다.')
          return
        } 
        // 선택된 적 없는 값이지만, 이미 5개가 선택되어 있으면 경고문 띄우기
        // 선택된 값을 "선택 시간" 목록에 추가
      this.selectedTime.push(time)
      }
    },
    isSelcted(time) {
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
.time-table-list {
  display: flex;
  width: 500px;
  flex-wrap: wrap;
  list-style: none;
}
.list-item {
  margin: 10px;
  font-size: 24px;
  padding: 5px;
  cursor: pointer;
}
</style>
<!-- template, script 구조로 되어 있는 것들은 모두 components -->