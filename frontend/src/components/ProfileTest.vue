<template>
  <div>
    <h1>Профиль пользователя (просто для теста)</h1>
    <p>Имя пользователя: {{ user.username }}</p>
    <p>MMR: {{ user.mmr }}</p>
    <p>Индекс задачи: {{ user.task_index }}</p>
  </div>
</template>

<script>
import apiClient from '@/api.js';

export default {
  data() {
    return {
      user: {},
    };
  },
  mounted() {
    this.fetchProfile();
  },
  methods: {
    async fetchProfile() {
      try {
        const response = await apiClient.get('/profile/');
        this.user = response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>