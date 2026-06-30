<script>
export default {
  name: "Navbar",
  data() {
    return {
      showMobileMenu: false,
      searchQuery: "",
    };
  },
  computed: {
    cartItemCount() {
      return this.$store.state.cart.items.length;
    },
  },
  methods: {
    handleSearch() {
      if (this.searchQuery.trim()) {
        this.$router.push({
          name: "search",
          query: { query: this.searchQuery },
        });
        this.searchQuery = "";
      }
    },
  },
};
</script>
<template>
  <div id="wrapper">
    <div class="navbar">
      <div class="navbar-brand">
        <RouterLink class="navbar-item" to="/"
          ><strong>Go to Home</strong></RouterLink
        >
        <RouterLink class="navbar-item" to="/about">Go to About</RouterLink>
        <a
          href=""
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbarmenu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-start">
          <div class="navbar-item">
            <div class="has-addons field">
              <div class="control flex flex-col w-3rem ">
                <input 
                  v-model="searchQuery"
                  type="text"
                  class="input"
                  placeholder="Search products..."
                  @keyup.enter="handleSearch">
                <div class="control">
                  <button 
                    class="button is-success"
                    @click="handleSearch"
                    type="button">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="navbar-end">
          <RouterLink class="navbar-item" to="/winter">Winter</RouterLink>
          <RouterLink class="navbar-item" to="/summer">Summer</RouterLink>
          <div class="nacbar-item">
            <div class="buttons navbar-item">
              <router-link to="log-in"> Log In </router-link>
              <router-link to="cart" class="button is-succes">
                <span class="icon navbar-item"><i class="fas fa-shopping-cart"></i> </span>
                <span>Cart {{ cartItemCount }}</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
      <div class="navbar-item">

        <h1>My E-Commerce Store</h1>
      </div>
      <nav></nav>
    </div>
  </div>
</template>

<style scoped>
.navbar {
  background-color: #ffffff;
  color: #111827;
}

.navbar-brand,
.navbar-item,
nav,
.navbar h1 {
  background-color: #ffffff;
  color: #111827;
}

.navbar-item:hover,
.navbar-item:focus {
  background-color: #ffffff;
  color: #111827;
}
</style>
