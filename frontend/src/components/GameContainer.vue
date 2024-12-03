<script>
import Menu from "@/components/Menu.vue";
import Game from "@/components/Game.vue";

export default {
  components: { Menu, Game },

  data() {
    return {
      isMenu: true
    }
  },

  methods: {
    backToMenu() {
      this.isMenu = true;
    },

    backToGame() {
      this.isMenu = false;
    }
  }
}
</script>

<template>
  <Menu v-if="isMenu" :game=backToGame />
  <Game v-else :back=backToMenu />
</template>