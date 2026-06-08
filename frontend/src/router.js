
import { createRouter, createWebHashHistory } from "vue-router";
import Home from "./components/pages/Home.vue";
import Product from "./components/pages/Product.vue";
const routes = [
    { path: "/", name: "home", component: Home },
    { path: "/about", name: "about", },
    { path: "/product/:category_slug/:product_slug", name: "product", component: Product }
]


const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router