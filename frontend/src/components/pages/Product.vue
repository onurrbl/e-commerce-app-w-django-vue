<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img :src="product.image" :alt="product.name" />
          <h1 class="is-size-2 title">{{ product.name }}</h1>
          <p class="is-size-5">${{ product.price }}</p>
          <p class="is-size-5">{{ product.description }}</p>
        </figure>
        <div class="column is-3">
          <h2 class="subtitle">Information</h2>
          <p><strong>Price</strong> : ${{ product.price }}</p>
          <div class="field has-addons mt-6">
            <div class="control">
              <input type="number" class="input" min="1" v-model="quantity" />
              <div class="control">
                <a href="" class="button is-dark"></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Product",

  data() {
    return {
      product: {},
      quantity: 1,
    };
  },

  mounted() {
    this.getProduct();
  },

  methods: {
    getProduct() {
      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;

      axios
        .get(`api/v1/products/category/${category_slug}/${product_slug}/`)
        .then((response) => {
          console.log(response.data);
          this.product = response.data;
        })
        .catch((error) => {
          console.error("Error fetching product details:", error);
        });
    },
  },
};
</script>