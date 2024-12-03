<script>
export default {
  props: {
    place: {
      type: Object,
      required: true
    },
    index: {
      type: Number,
      required: true
    }
  }
}
</script>

<template>
  <tr class="place">
    <td class="place-item">{{ index + 1 }}</td>
    <td class="place-item">{{ place.username }}</td>
    <td class="place-item">{{ place.mmr }}</td>
  </tr>
</template>