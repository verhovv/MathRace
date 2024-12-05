<template>
  <Notification :error="error" :success="success"></Notification>
  <router-view></router-view>
</template>

<script>
import Notification from '@/components/Notification.vue';

export default {
  components: {
    Notification,
  },
  data() {
    return {
      error: null,
      success: null,
    };
  },
  methods: {
    setError(message) {
      this.error = message;
      setTimeout(() => {
        this.error = null;
      }, 3500);
    },
    setSuccess(message) {
      this.success = message;
      setTimeout(() => {
        this.success = null;
      }, 3500);
    },
  },
};
</script>