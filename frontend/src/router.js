
import { createRouter, createWebHashHistory } from "vue-router";
// import Home from "./views/Home.vue";

const  routes= [
    { path: "/", name: "home", },
    { path: "/about", name: "about", }
]


const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router