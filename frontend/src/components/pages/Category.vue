<template>
  <div class="page-category">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="is-size-2 title">{{ category.name }}</h1>
      </div>

      <div
        class="column is-3"
        v-for="product in category.products"
        :key="product.id"
      >
         <product-box
        v-for="product in category.products"
        :key="product.id"
        :product="product"
      />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import ProductBox from "../ProductBox.vue";
export default {
  name: "category",
  components: {
    ProductBox,
  },
  data() {
    return {
      category: {
        products: [],
      },
    };
  },
  mounted() {
    this.getCategory();
  },
  methods: {
    async getCategory() {
      this.$store.commit("setLoading", true);
      const category_slug = this.$route.params.category_slug;
      await axios
        .get(`api/v1/products/category/${category_slug}/`)
        .then((response) => {
          console.log(response.data);
          this.category = response.data;
          document.title = this.category.name + " - My E-Commerce Store";
        })
        .catch((error) => {
          console.error("Error fetching category details:", error);
        });
      this.$store.commit("setLoading", false);
    },
    addToCart() {
      this.$store.commit("addToCart", {
        product: this.product,
        quantity: this.quantity,
      });
      toast({
        message: "Product added to cart!",
        type: "is-success",
        position: "top-right",
        duration: 3000,
      });
    },
  },
};
</script>