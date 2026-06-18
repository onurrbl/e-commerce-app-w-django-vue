<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search Results</h1>
            </div>
            <div class="column is-12">
                <ProductBox v-for="product in searchResults" :key="product.id" :product="product" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import ProductBox from "../ProductBox.vue";
export default {
    name: "Search",

    data() {
        return {
            searchResults: [],
        };
    },
    components: {
        ProductBox,
    },
    mounted() {
        this.performSearch();
    },
    methods: {
        async performSearch() {
            const query = this.$route.query.query || '';
            if (query) {
                this.$store.commit("setLoading", true);
                try {
                    const response = await axios.post("api/v1/products/search/", { query });
                    this.searchResults = response.data;
                    document.title = `Search results for "${query}" - My E-Commerce Store`;
                } catch (error) {
                    console.error("Error performing search:", error);
                    this.searchResults = [];
                } finally {
                    this.$store.commit("setLoading", false);
                }
            }
        },
    },
};

</script>