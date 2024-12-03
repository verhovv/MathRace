<script>
export default {
  props: {
    task: {
      type: String,
      required: true
    },
    doAnswer: {
      type: Function,
      required: true
    },
    answer: {
      type: String,
      required: true
    }
  }
}
</script>

<template>
  <div class="field">
    <span class="task">{{ task }}</span>
    <div class="user-input">
      <input type="number" class="answer" v-bind:value="answer" />
      <button class="send-answer" @click="doAnswer">=</button>
    </div>
  </div>
</template>