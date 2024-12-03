<template>
  <div class="login-container">
    <h1>Вход</h1>
    <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="Имя пользователя" class="answer" required/>
      <input v-model="password" type="password" placeholder="Пароль" class="answer" required/>
      <button type="submit" class="user-input">Войти</button>
    </form>
    <div v-if="error" class="error">{{ error }}</div>
    <div class="switch-link">
      <span class="switch-text">Нет аккаунта?</span>
      <button @click="switchToRegister">Зарегистрироваться</button>
    </div>
  </div>
</template>

<script>
import apiClient from '@/api.js';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        const response = await apiClient.post('/login/', {
          username: this.username,
          password: this.password,
        });
        localStorage.setItem('token', response.data.token);
        this.$router.push('/');
      } catch (error) {
        if (error.response && error.response.status === 403 && error.response.data.error) {
          this.error = error.response.data.error;
        } else {
          this.error = "Ошибка входа";
        }
        console.error(error);
      }
    },
  },
  props: {
    switchToRegister: {
      type: Function,
      required: true,
    },
  },
};
</script>

<style scoped>
.login-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: stretch;
}

.error {
  color: #b92c28;
  margin-top: 10px;
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  background: #333333;
  padding: 10px;
  border: 2px solid red;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

h1 {
  text-align: center;
  margin-bottom: auto;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
}

.answer {
  padding: 10px;
  font-size: 1rem;
  width: 100%;
}

.user-input {

  padding: 10px;
  font-size: 1rem;
  width: 100%;
}

.switch-link {
  width: 100%;
  text-align: left;
  margin-top: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-content: stretch;
  align-items: center;
  gap: 20px;
}

.switch-link button {
  width: 60%;
}
</style>