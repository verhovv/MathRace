<script >
import EndPanel from "@/components/EndPanel.vue";
import Road from "@/components/Road.vue";
import MathField from "@/components/MathField.vue";

import imgCar1 from "@/assets/images/car.png"

export default {
  components: { EndPanel, Road, MathField },

  data() {
    return {
      isEnded: true,
      task: "\\(\\sqrt{2^2 - 4}=\\)",
      user: {
        username: "Dmitry",
        totalWins: 10,
        imgCar: imgCar1,
        userMMR: 100
      },
      userOther: {
        username: "Pidoras",
        totalWins: 10,
        imgCar: imgCar1,
        userMMR: 100
      }
    }
  },

  props: {
    back: {
      type: Function,
      required: true
    },
  }
}
</script>

<template>
  <EndPanel v-show=isEnded :isWin=true :plusMMR=10 :back=back />
  <div class="game">
    <div class="game-field">
      <Road :user="this.user"/>
      <Road :user="this.userOther"/>
    </div>
    <div class="math-field">
      <MathField :task="this.task" />
    </div>
  </div>
</template>