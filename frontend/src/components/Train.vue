<script>
export default {
  props: {
    task: {
      type: String,
      required: true
    },
    close: {
      type: Function,
      required: true
    }
  }
}
</script>

<template>
  <div class="popup" id="train">
    <div class="field">
      <button class="exit" @click="close">X</button>
      <span class="task">{{ task }}</span>
      <div class="user-input">
        <input type="number" class="answer"/>
        <button class="send-answer">=</button>
      </div>
    </div>
  </div>
</template>