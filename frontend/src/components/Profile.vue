<template>
  <div class="popup">
    <button class="exit" @click="close">X</button>
    <div class="change-box">
      <ChangePassword v-if="isChangePassword" :switchToChangeUsername="switchToChangeUsername" />
      <ChangeUsername v-else :switchToChangePassword="switchToChangePassword" />
    </div>
  </div>
</template>

<script>
import ChangeUsername from "@/components/ChangeUsername.vue";
import ChangePassword from "@/components/ChangePassword.vue";

export default {
  components: {ChangeUsername, ChangePassword },
  data() {
    return {
      isChangePassword: true,
      error: null,
    };
  },
  props: {
    user: {
      type: Object,
      required: true
    },
    close: {
      type: Function,
      required: true
    }
  },
  methods: {
    switchToChangeUsername() {
      this.isChangePassword = false;
    },

    switchToChangePassword() {
      this.isChangePassword = true;
    },
  },
}
</script>

<style scoped>
.change-box {
  padding: 20px;
  width: 20vw;
  min-width: 300px;
  height: 40vh;
  min-height: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: center;
  flex-shrink: 1;
}
</style>