import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import store from './components/store/index.js.js'

const app = createApp(App)
axios.defaults.baseURL = 'http://localhost:8000/'
app.use(router)
app.use(store)

app.mount('#app')
