<script>
export default {
  props: {
    user: {
      type: Object,
      required: true
    },
    close: {
      type: Function,
      required: true
    }
  }
}
</script>

<template>
  <div class="popup" id="profile">
    <button class="exit" @click="close">X</button>
    <div class="content">
      <div class="inline-field">
        <span>Имя:</span><input type="text">
      </div>
      <div class="inline-field">
        <span>Почта:</span><input type="email">
      </div>
      <div class="inline-field" id="email-code">
        <span>Код из письма:</span><input type="text">
      </div>
      <div class="inline-field">
        <span>Пароль:</span><input type="password">
      </div>
      <div class="inline-field" id="repeat-password">
        <span>Повторите:</span><input type="password">
      </div>
      <div class="inline-field">
        <span>Делайте это сами, я хз, как лучше</span>
      </div>
    </div>
  </div>
</template>