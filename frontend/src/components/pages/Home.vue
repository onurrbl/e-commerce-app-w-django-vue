<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <div class="container">
          <h1 class="title">Welcome to My E-Commerce Store</h1>
          <h2 class="subtitle">Find the best products at unbeatable prices!</h2>
        </div>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="title is-3">Featured Products</h2>
      </div>

      <div
        class="column is-3"
        v-for="product in latestproducts"
        :key="product.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.thumbnail" />
            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-5 has-text-weight-bold">${{ product.price }}</p>
            <router-link :to="'/product'  + product.get_absolute_url  " class="button is-dark mt-4"> VView Details </router-link>
        
          </figure>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "Home",

  data() {
    return {
      latestproducts: [],
    };
  },
  components: {},
    mounted() {
        this.getLatestProducts();
    },
    methods: {
        getLatestProducts() {
            axios.get('api/v1/products/latest-products/')
                .then(response => {
                    console.log(response.data);
                    this.latestproducts = response.data;
                })
                .catch(error => {
                    console.error('Error fetching latest products:', error);
                });
        },
    }


};
</script>
<style scoped>  
.image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
}

</style>