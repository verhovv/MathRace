<template>
  <div class="auth-container">
    <div class="auth-box">
      <Login v-if="isLogin" :switchToRegister="switchToRegister" />
      <Register v-else :switchToLogin="switchToLogin" />
    </div>
  </div>
</template>

<script>
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";

export default {
  components: { Login, Register },

  data() {
    return {
      isLogin: true,
    };
  },

  methods: {
    switchToRegister() {
      this.isLogin = false;
    },

    switchToLogin() {
      this.isLogin = true;
    },
  },
};
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.auth-box {
  background: #333333;
  border: 8px solid #4960B8;
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