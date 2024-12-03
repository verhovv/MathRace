<script>
import Menu from "@/components/Menu.vue";
import Game from "@/components/Game.vue";

export default {
  components: { Menu, Game },

  data() {
    return {
      isMenu: true,
      firstTask: "",
      user: {}
    }
  },

  methods: {
    backToMenu() {
      this.isMenu = true;
    },

    backToGame(firstTask, user) {
      this.isMenu = false;
      this.firstTask = firstTask;
      this.user = user;
    }
  }
}
</script>

<template>
  <Menu v-if="isMenu" :game=backToGame />
  <Game v-else :back=backToMenu :envData="firstTask" :user="user" />
</template>