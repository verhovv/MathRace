<script>
export default {
  computed: {
    userRoad: function() {
      return {
        paddingLeft: `calc((100% - 380px) * ${this.float})`
      }
    }
  },

  props: {
    user: {
      type: Object,
      required: true
    },
    float: {
      type: Number,
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

<style scoped>
#you {
  padding-left: calc((100% - 380px) * v-bind(float))
}
</style>