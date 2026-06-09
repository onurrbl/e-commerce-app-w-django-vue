import { createStore } from "vuex";

export default createStore({
    state: {
        products: [],
        cart: {
            items: [],
        },
        isAuthenticated: false,
        token: null,
        isLoading: false,
    },
    getters: {
        getProducts(state) {
            return state.products;
        }

    },
    mutations: {
        setProducts(state, products) {
            state.products = products;
        },
        initializeStore(state) {
            if (localStorage.getItem("cart")) {
                state.cart = JSON.parse(localStorage.getItem("cart"));

            } else {
                localStorage.setItem("cart", JSON.stringify(state.cart));
            }

        },
        addToCart(state, product) {
            const exists = state.cart.items.find(item => item.id === product.id);
            if (exists) {
                exists.quantity += 1;
            } else {
                state.cart.items.push({ ...product, quantity: 1 });
            }
            localStorage.setItem("cart", JSON.stringify(state.cart));
        }
    },
    actions: {
        async fetchProducts({ commit }) {
            try {
                const response = await fetch("http://localhost:8000/api/products/latest-products/");
                const data = await response.json();
                commit("setProducts", data);
            } catch (error) {
                console.error("Error fetching products:", error);
            }
        }
    },
    modules: {},
}); 