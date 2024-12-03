<script>
import User from "@/components/User.vue";
import Leaderboard from "@/components/Leaderboard.vue";
import Train from "@/components/Train.vue";
import Profile from "@/components/Profile.vue";

import imgCar1 from "@/assets/images/car.png"
import apiClient from "@/api.js";

export default {
  components: {Train, User, Leaderboard, Profile},

  data() {
    return {
      user: {
        username: "Pidoras",
        imgCar: imgCar1,
        userMMR: 100
      },
      leaderboard: [
        {username: "Дмитрий", mmr: 100},
        {username: "Владимир", mmr: 30},
        {username: "Алексадр", mmr: 30},
        {username: "Павел", mmr: 30}
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
    },
    async fetchProfile() {
      try {
        const response = await apiClient.get('/profile/');
        this.user = response.data;
        this.user.imgCar = imgCar1;
      } catch (error) {
        console.error(error);
      }
    },
    async fetchLeaderboard() {
      try {
        const response = await apiClient.get('/leaderboard/');
        this.leaderboard = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async fetchRoom() {
      try {
        const response = await apiClient.get('/room/', {params: {"task_count": 10}});
        if (response.data.result === 'joined') {
          this.game(response.data, this.user);
        }
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }
  },

  beforeMount() {
    this.fetchProfile();
    this.fetchLeaderboard();
  },
}
</script>

<template>
  <Train v-show="isOpenTrain" :task="task" :close="closeTrain"/>
  <Profile v-show="isOpenProfile" :user="user" :close="closeProfile"/>
  <div class="menu">
    <div class="left">
      <User :user="this.user" :open="openProfile"/>
      <div class="menu-buttons">
        <button class="race" @click="fetchRoom">ГОНКА</button>
        <button class="training" @click="isOpenTrain=true">ТРЕНИРОВКА</button>
      </div>
    </div>
    <div class="right">
      <Leaderboard :places="this.leaderboard"/>
    </div>
  </div>
</template>
