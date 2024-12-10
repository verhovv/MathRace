<template>
  <div class="change-username-container">
    <h1>Смена ника</h1>
    <form @submit.prevent="changeUsername">
      <input v-model="newUsername" type="text" placeholder="Имя пользователя" class="answer" required/>
      <button type="submit" class="user-input">Сменить ник</button>
    </form>
    <div class="switch-link">
      <button @click="logout" class="logout-button">Выйти из аккаунта</button>
      <button @click="switchToChangePassword">Смена пароля</button>
    </div>
  </div>
</template>

<script>
import apiClient from '@/api.js';

export default {
  data() {
    return {
      newUsername: '',
    };
  },
  methods: {
    async changeUsername() {
      try {
        const response = await apiClient.post('/change-username/', {
          new_username: this.newUsername,
        });
        this.$root.setSuccess('Ник успешно изменен');
        this.newUsername = '';
        this.$emit('username-changed');
      } catch (error) {
        if (error.response && error.response.status === 400) {
          this.$root.setError(Object.values(error.response.data).flat().join(' '));
        } else {
          this.$root.setError('Ошибка смены ника');
        }
        console.error(error);
      }
    },
    logout() {
      localStorage.removeItem('token');
      this.$root.setSuccess('Вы успешно вышли из аккаунта');
      this.$router.push('/auth');
    },
  },
  props: {
    switchToChangePassword: {
      type: Function,
      required: true
    },
  },
};
</script>

<style scoped>
.change-username-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: stretch;
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
  height: 100%;
}

.logout-button {
  border: 8px solid #ff4d4d;
  background: #ff4d4d;
  color: #FFFFFF;
}

.logout-button:hover {
  border-color: #FFFFFF;
  cursor: pointer;
  transition: 0.3s;
}
</style>