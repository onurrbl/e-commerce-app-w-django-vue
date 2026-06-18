<template>
  <div class="column is-3">
    <figure class="image mb-4">
      <img :src="product.thumbnail" :alt="product.name" />
    </figure>
    <h3 class="is-size-4">{{ product.name }}</h3>
    <p class="is-size-6 has-text-grey">${{ product.price }}</p>
    <router-link
      :to="'/product' + product.get_absolute_url"
      class="button is-dark mt-4"
    >
      View Details
    </router-link>
  </div>
</template>

<script>
export default {
  name: "ProductBox",
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style  scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>