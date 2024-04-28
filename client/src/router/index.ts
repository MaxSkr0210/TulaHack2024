import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AuthView from "../views/AuthView.vue";
import TestView from "../views/TestView.vue";
import { useAuthStore } from "../store";
import LessonView from "../views/LessonView.vue";
import GameView from "../views/GameView.vue";
import CreateLessonView from "../views/CreateLessonView.vue";
import CreateUserView from "../views/CreateUserView.vue";

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
  {
    path: "/game",
    name: "game",
    meta: {
      Auth: true,
    },
    component: GameView,
  },
  {
    path: "/create_lesson",
    name: "create_lesson",
    meta: {
      Auth: true,
    },
    component: CreateLessonView,
  },
  {
    path: "/create_user",
    name: "create_user",
    meta: {
      Auth: true,
    },
    component: CreateUserView,
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
      return "/";
    }
  } else {
    if (!to.meta.Auth) return true;
    else return "/auth";
  }
});

export default router;
