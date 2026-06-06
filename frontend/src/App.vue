<script >
import Navbar from "./components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },

};
</script>

<template>
  <div>
    <header>
      <div><p>Hello, World!</p></div>
      <Navbar />
    </header>
    <div class="section">
      <router-view> </router-view>
    </div>
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<style lang="scss">
@import "../node_modules/bulma";
</style>
