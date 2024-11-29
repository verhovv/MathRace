<script>
export default {
  props: {
    user: {
      type: Object,
      required: true
    }
  }
}
</script>

<template>
  <div class="road">
    <span> {{ user.username }} </span>
    <div class="car-way" id="you">
      <img :src="user.imgCar" alt="car">
    </div>
  </div>
</template>