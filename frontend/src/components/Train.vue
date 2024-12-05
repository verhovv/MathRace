<script>
import {VueMathjax} from 'vue-mathjax-next'
import apiClient from "@/api.js";

export default {
  components: {'vue-mathjax': VueMathjax},

  data() {
    return {
      curAnswer: "",
      answer: 0,
      task: ""
    }
  },
  props: {
    close: {
      type: Function,
      required: true
    }
  },
  methods: {
    async fetchTask() {
      try {
        const response = await apiClient.get('/task/');
        this.task = response.data.task;
        this.answer = response.data.answer;
      } catch (error) {
        console.error(error);
      }
    },
    async answerTask() {
      if (parseInt(this.curAnswer) === this.answer) {
        try {
          await this.fetchTask();
        } catch (error) {
          console.error(error);
        }
      }
      this.curAnswer = "";
    },
  },

  async beforeMount() {
    await this.fetchTask();
  }
}
</script>

<template>
  <div class="popup" id="train">
    <div class="field">
      <button class="exit" @click="close">X</button>
      <vue-mathjax class="task" :formula="task"></vue-mathjax>
      <div class="user-input">
        <input v-on:keyup.enter="answerTask" type="number" class="answer" v-model="curAnswer"/>
        <button class="send-answer" @click="answerTask">=</button>
      </div>
    </div>
  </div>
</template>