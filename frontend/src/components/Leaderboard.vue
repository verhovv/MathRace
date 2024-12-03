<script>
import LBLine from "@/components/LBLine.vue";

export default {
  components: {LBLine},
  props: {
    places: {
      type: Object,
      required: true
    }
  }
}
</script>

<template>
  <div class="leaderboard">
    <h1>ЛУЧШИЕ ГОНЩИКИ</h1>
    <div class="scroll-table">
      <table class="users">
        <thead>
        <tr class="place">
          <th class="place-item">№</th>
          <th class="place-item">Имя игрока</th>
          <th class="place-item">MMR</th>
        </tr>
        </thead>
        <tbody>
        <LBLine v-for="(place, i) in places" :index="i" :place="place"/>
        </tbody>
      </table>
    </div>
  </div>
</template>