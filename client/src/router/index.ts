import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AuthView from "../views/AuthView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    meta: {
      Auth: true,
    },
    component: HomeView,
  },
  {
    path: "/auth",
    name: "auth",
    meta: {
      Auth: false,
    },
    component: AuthView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
