<script>
import User from "@/components/User.vue";
import Leaderboard from "@/components/Leaderboard.vue";
import Train from "@/components/Train.vue";
import Profile from "@/components/Profile.vue";

import imgCar1 from "@/assets/images/car.png"

export default {
  components: { Train, User, Leaderboard, Profile },

  data() {
    return {
      user: {
        username: "Pidoras",
        totalWins: 10,
        imgCar: imgCar1,
        userMMR: 100
      },
      leaderboard: [
        { username: "Дмитрий", mmr: 100},
        { username: "Владимир", mmr: 30},
        { username: "Алексадр", mmr: 30},
        { username: "Павел", mmr: 30}
      ],
      task: "\\(\\sqrt{2^2 - 4}=\\)",
      isOpenTrain: false,
      isOpenProfile: false
    }
  },

  props: {
    game: {
      type: Function,
      required: true
    }
  },

  methods: {
    closeTrain() {
      this.isOpenTrain = false;
    },
    closeProfile() {
      this.isOpenProfile = false;
    },
    openProfile() {
      this.isOpenProfile = true;
    }
  }
}
</script>

<template>
  <Train v-show="isOpenTrain" :task="task" :close="closeTrain"/>
  <Profile v-show="isOpenProfile" :user="user" :close="closeProfile"/>
  <div class="menu">
    <div class="left">
      <User :user="this.user" :open="openProfile"/>
      <div class="menu-buttons">
        <button class="race" @click="game">ГОНКА</button>
        <button class="training" @click="isOpenTrain=true">ТРЕНИРОВКА</button>
      </div>
    </div>
    <div class="right">
      <Leaderboard :places="this.leaderboard"/>
    </div>
  </div>
</template>
