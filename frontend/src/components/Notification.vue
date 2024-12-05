<template>
  <div v-if="error" class="error-notification">
    {{ error }}
  </div>
  <div v-if="success" class="success-notification">
    {{ success }}
  </div>
</template>

<script>
export default {
  props: {
    error: {
      type: String,
      default: null,
    },
    success: {
      type: String,
      default: null,
    },
  },
};
</script>

<style scoped>
.error-notification {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 10px;
  background-color: #b92c28;
  color: white;
  text-align: center;
  z-index: 1000;
}

.success-notification {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 10px;
  background-color: #28a745;
  color: white;
  text-align: center;
  z-index: 1000;
}
</style>