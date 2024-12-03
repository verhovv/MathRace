<script>
import Menu from "@/components/Menu.vue";
import Game from "@/components/Game.vue";

import {UserAPI} from "@/api/user.js";

export default {
  components: { Menu, Game },

  data() {
    return {
      isMenu: true,
      user: null
    }
  },

  methods: {
    backToMenu() {
      this.isMenu = true;
    },

    backToGame() {
      this.isMenu = false;
    }
  },

  beforeMount() {
    UserAPI.login({username: "dmitry", password: ""}).then((req) => {
      console.log(req)
    })
  }
}
</script>

<template>
  <span>{{ this.user }}</span>
  <Menu v-if="isMenu" :game=backToGame />
  <Game v-else :back=backToMenu />
</template>