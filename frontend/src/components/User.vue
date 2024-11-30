<script>
export default {
  props: {
    user: {
      type: Object,
      required: true
    },
    open: {
      type: Function,
      required: true
    }
  }
}
</script>

<template>
  <div class="user-info" @click="open">
    <span class="username">{{ user.username }}</span>
    <span class="wins">{{ user.totalWins }} побед</span>
  </div>
  <div class="car-image">
    <img :src="user.imgCar" alt="Машина">
  </div>
</template>