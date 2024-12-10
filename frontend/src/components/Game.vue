<script>
import EndPanel from "@/components/EndPanel.vue";
import {VueMathjax} from 'vue-mathjax-next'

import apiClient from "@/api.js";

export default {
  components: {EndPanel, 'vue-mathjax': VueMathjax},

  data() {
    return {
      isEnded: false,
      isWin: false,
      diff: 0,
      userThis: {},
      userOther: {},
      answer: "",
      otherFloat: 0
    }
  },

  methods: {
    async doAnswer() {
      try {
        const response = await apiClient.get('/answer/', {params: {"answer": this.answer}});
        if (response.data.result === 'good answer') {
          this.envData.task = response.data.task;
          this.envData.float = response.data.float;
        } else if (response.data.result === 'win') {
          this.envData.float = 1;
          this.isEnded = true;
          this.isWin = true;
          this.diff = response.data.difference;
        }
      } catch (error) {
        console.error(error);
      }
      this.answer = "";
    },
    async checkOther() {
      try {
        const itervalID = setInterval(async () => {
          const response = await apiClient.get('/enemy/');
          if (this.isWin) {
            clearInterval(itervalID);
          } else if (response.data.result === 'race is going') {
            this.otherFloat = response.data.float;
          } else if (response.data.result === 'lose') {
            clearInterval(itervalID);
            this.otherFloat = 1;
            this.isEnded = true;
            this.isWin = false;
            this.diff = response.data.difference;
          }
        }, 1000);
      } catch (error) {
        console.error(error);
      }
    }
  },

  async mounted() {
    await this.checkOther();
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
      <div class="road">
        <span> {{ this.user.username }} - {{ this.user.mmr }}MMR </span>
        <div class="car-way" id="you">
          <img :src="'images/' + this.user.imgCar" alt="car">
        </div>
      </div>
      <div class="road">
        <span> {{ this.envData.other_user.username }} - {{ this.envData.other_user.mmr }}MMR </span>
        <div class="car-way" id="other">
          <img :src="'images/' + this.envData.other_user.imgCar" alt="car">
        </div>
      </div>
    </div>
    <div class="math-field">
      <div class="field">
        <vue-mathjax v-show="!isEnded" :formula="this.envData.task"></vue-mathjax>
        <div class="user-input">
          <input v-on:keyup.enter="doAnswer" type="number" class="answer" v-model="answer"/>
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

#other {
  padding-left: calc((100% - 280px) * v-bind(otherFloat))
}
</style>