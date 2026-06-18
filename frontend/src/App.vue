<script >
import Navbar from "./components/Navbar.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    Navbar,
  },
  data() {
    return {
      cart: [],
    };
  },

  beforeCreate() {
    this.$store.commit('initializeStore');
  },
  mounted() {
    this.cart = this.$store.state.cart;
  }
};
</script>

<template>
  <div>
    <header>
      <Navbar />
    </header>
    <div class="is-loading-bar has-text-centered" :class="{'is-loading' : $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>
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


is-loading-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background-color: transparent;
  z-index: 9999;

  .lds-dual-ring {
    display: inline-block;
    width: 24px;
    height: 24px;
    border: 3px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    border-top-color: #fff;
    animation: lds-dual-ring 1s linear infinite;
    margin-top: -10px; /* Center the spinner vertically */
  }

  &.is-loading {
    background-color: transparent; /* Keep the background transparent */
    
    .lds-dual-ring {
      display: inline-block; /* Show the spinner when loading */
    }
  }
}
</style>
