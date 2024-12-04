<script >
import EndPanel from "@/components/EndPanel.vue";
import Road from "@/components/Road.vue";
import MathField from "@/components/MathField.vue";
import { VueMathjax } from 'vue-mathjax-next'

import imgCar1 from "@/assets/images/car.png"
import apiClient from "@/api.js";

export default {
  components: { EndPanel, Road, MathField, 'vue-mathjax': VueMathjax },

  data() {
    return {
      isEnded: false,
      isWin: true,
      diff: 0,
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
        const response = await apiClient.get('/answer/', {params: {"answer": this.answer}});
        console.log(response.data);
        if (response.data.result === 'good answer') {
          this.envData.task = response.data.task;
          this.envData.float = response.data.float;
          console.log(this.envData);
        }
        else if (response.data.result === 'win') {
          this.envData.float = 1;
          this.isEnded = true;
          this.isWin = true;
          this.diff = response.data.difference;
        }
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
  <EndPanel v-show=isEnded :isWin=isWin :plusMMR=diff :back=back />
  <div class="game">
    <div class="game-field">
<!--      <Road :user="this.user" :float="this.envData.float" />-->
      <div class="road">
        <span> {{ this.user.username }} </span>
        <div class="car-way" id="you">
          <img :src="this.user.imgCar" alt="car">
        </div>
      </div>
      <Road :user="this.envData.other_user" :float="this.envData.float" />
    </div>
    <div class="math-field">
      <div class="field">
        <vue-mathjax v-show="!isEnded" :formula="this.envData.task"></vue-mathjax>
        <div class="user-input">
          <input type="number" class="answer" v-model="answer" />
          <button class="send-answer" @click="doAnswer">=</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#you {
  padding-left: calc((100% - 280px) * v-bind(envData.float))
}
</style>