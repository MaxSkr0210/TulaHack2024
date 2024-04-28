import { createApp } from "vue";
import { createPinia } from "pinia";

import "./index.css";
import "../node_modules/flowbite-vue/dist/index.css";

import App from "./App.vue";
import router from "./router";

const pinia = createPinia();

createApp(App).use(router).use(pinia).mount("#app");
