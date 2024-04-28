import { createApp } from "vue";
import { createPinia } from "pinia";
import VueCountdown from "@chenfengyuan/vue-countdown";

import "./index.css";
import "../node_modules/flowbite-vue/dist/index.css";

import App from "./App.vue";
import router from "./router";

const pinia = createPinia();

const app = createApp(App);

app.component(VueCountdown.name as string, VueCountdown);

app.use(router).use(pinia).mount("#app");
