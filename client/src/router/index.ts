import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AuthView from "../views/AuthView.vue";
import TestView from "../views/TestView.vue";
import { useAuthStore } from "../store";
import LessonView from "../views/LessonView.vue";

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
  // {
  //   path: "/tests",
  //   name: "tests",
  //   meta: {
  //     Auth: true,
  //   },
  //   component: TestsView,
  // },
  {
    path: "/test",
    name: "test",
    meta: {
      Auth: true,
    },
    component: TestView,
  },
  {
    path: "/lessons/:id",
    name: "lesson",
    meta: {
      Auth: true,
    },
    component: LessonView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from) => {
  if (localStorage.getItem("jwt")) {
    const store = useAuthStore();
    try {
      await store.getUser();
      const user = store.getterUser;

      if (to.meta.Auth && !user) {
        return "/auth";
      }

      if (!to.meta.Auth && user) {
        return true;
      }
    } catch (error) {
      await store.refreshToken();
    }
  }
});

export default router;
