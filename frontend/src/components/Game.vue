<script >
import EndPanel from "@/components/EndPanel.vue";
import Road from "@/components/Road.vue";
import MathField from "@/components/MathField.vue";

import imgCar1 from "@/assets/images/car.png"
import apiClient from "@/api.js";

export default {
  components: { EndPanel, Road, MathField },

  data() {
    return {
      isEnded: false,
      task: "\\(\\sqrt{2^2 - 4}=\\)",
      userThis: {
        username: "Dmitry",
        imgCar: imgCar1,
        userMMR: 100
      },
      userOther: {
        username: "Pidoras",
        imgCar: imgCar1,
        userMMR: 100
      },
      answer: ""
    }
  },

  methods: {
    async doAnswer() {
      try {
        console.log(this.answer);
        const response = await apiClient.get('/answer/', {params: {"answer": this.answer}});
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }
  },

  props: {
    back: {
      type: Function,
      required: true
    },
    envData: {
      type: Object,
      required: true
    },
    user: {
      type: Object,
      required: true
    }
  }
}
</script>

<template>
  <EndPanel v-show=isEnded :isWin=true :plusMMR=10 :back=back />
  <div class="game">
    <div class="game-field">
      <Road :user="this.user" />
      <Road :user="this.envData.other_user" />
    </div>
    <div class="math-field">
      <div class="field">
        <span class="task">{{ this.envData.task_text ? this.envData.task_text : this.envData.first_task }}</span>
        <div class="user-input">
          <input type="number" class="answer" v-model="answer" />
          <button class="send-answer" @click="doAnswer">=</button>
        </div>
      </div>
    </div>
  </div>
</template>