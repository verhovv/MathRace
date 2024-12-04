<script>
export default {
  props: {
    isWin: {
      type: Boolean,
      required: true
    },
    plusMMR: {
      type: Number,
      required: true
    },
    back: {
      type: Function,
      required: true
    }
  }
}
</script>

<template>
  <div class="popup" id="end">
    <div class="content">
      <h1>{{ isWin ? "ПОБЕДА" : "ПОРАЖЕНИЕ" }}</h1>
      <span>{{isWin ? "+" : "-"}}{{ plusMMR }} MMR</span>
      <button @click="back">ВЫЙТИ</button>
    </div>
  </div>
</template>