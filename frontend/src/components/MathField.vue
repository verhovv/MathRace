<script>
export default {
  props: {
    task: {
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
      <input type="number" class="answer"/>
      <button class="send-answer">=</button>
    </div>
  </div>
</template>