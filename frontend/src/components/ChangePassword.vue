<template>
  <div class="change-password-container">
    <h1>Смена пароля</h1>
    <form @submit.prevent="changeUsername">
      <input v-model="oldPassword" type="password" placeholder="Старый пароль" class="answer" required />
      <input v-model="newPassword" type="password" placeholder="Новый пароль" class="answer" required />
      <input v-model="newPassword2" type="password" placeholder="Подтверждение нового пароля" class="answer" required />
      <button type="submit" class="user-input">Сменить пароль</button>
    </form>
    <div class="switch-link">
      <span class="switch-text">Что меняем?</span>
      <button @click="switchToChangeUsername">Смена ника</button>
    </div>
  </div>
</template>

<script>
import apiClient from '@/api.js';

export default {
  data() {
    return {
      oldPassword: '',
      newPassword: '',
      newPassword2: '',
    };
  },
  methods: {
    async changeUsername() {
      try {
        const response = await apiClient.post('/change-password/', {
          old_password: this.oldPassword,
          new_password: this.newPassword,
          new_password2: this.newPassword2,
        });
        this.$root.setSuccess('Пароль успешно изменен');
        this.oldPassword = '';
        this.newPassword = '';
        this.newPassword2 = '';
      } catch (error) {
        if (error.response && error.response.status === 400) {
          this.$root.setError(Object.values(error.response.data).flat().join(' '));
        } else {
          this.$root.setError('Ошибка смены пароля');
        }
        console.error(error);
      }
    },
  },
  props: {
    switchToChangeUsername: {
      type: Function,
      required: true
    },
  },
};
</script>

<style scoped>
.change-password-container {
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
}
</style>