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
      user: {},
      leaderboard: [],
      task: "",
      isOpenTrain: false,
      isOpenProfile: false,
      isFindingRoom: false
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
    async openTrain() {
      this.isOpenTrain = true;
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
        if (!this.isFindingRoom) {
          this.isFindingRoom = true;
          const response = await apiClient.get('/room/', {params: {"task_count": 10}});
          if (response.data.result === 'joined') {
            this.isFindingRoom = false;
            this.game(response.data, this.user);
          } else {
            await this.checkRoom();
          }
          console.log(response.data);
        } else {
          this.isFindingRoom = false;
        }
      } catch (error) {
        this.isFindingRoom = false;
        console.error(error);
      }
    },
    async checkRoom() {
      try {
        const itervalID = setInterval(async () => {
          const response = await apiClient.get('/room/', {params: {"task_count": 10}});
          console.log(response.data);
          if (response.data.result === 'joined') {
            clearInterval(itervalID);
            this.isFindingRoom = false;
            this.game(response.data, this.user);
          }
          else if (!this.isFindingRoom) {
            await apiClient.delete('/room/', {params: {"task_count": 10}});
            clearInterval(itervalID);
          }
        }, 1000);
      } catch (error) {
        console.error(error);
      }
    },
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
        <button v-if="isFindingRoom" class="race" @click="fetchRoom"
                :style="{borderColor: '#FFFFFF', backgroundColor: '#993D3D'}">ОТМЕНИТЬ
        </button>
        <button v-else class="race" @click="fetchRoom">ГОНКА</button>
        <button class="training" @click="openTrain">ТРЕНИРОВКА</button>
      </div>
    </div>
    <div class="right">
      <Leaderboard :places="this.leaderboard"/>
    </div>
  </div>
</template>
