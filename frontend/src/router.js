
import { createRouter, createWebHashHistory,createWebHistory } from "vue-router";
import Home from "./components/pages/Home.vue";
import Product from "./components/pages/Product.vue";
import Category from "./components/pages/Category.vue";
import Search from "./components/pages/Search.vue";
import Cart from "./components/pages/Cart.vue";
import Signup from "./components/pages/Signup.vue";
import Login from "./components/pages/Login.vue";
import Checkout from "./components/pages/Checkout.vue";
import Success from "./components/pages/Success.vue";
import Myaccount from "./components/pages/Myaccount.vue";
import store from './components/store/index.js.js';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: Signup
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: Login
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: Myaccount,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product,
    alias: '/product/:category_slug/:product_slug'
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
