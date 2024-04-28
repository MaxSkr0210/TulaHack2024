<template>
  <div class="home h-full">
    <div class="flex justify-center items-center" v-if="showMsg">
      <div class="msg text-center">
        <p>
          Чтобы мы вас получше узнали и поняли, чему мы вас сможем научить вам
          необходимо пройти тестирование
        </p>
        <button
          @click="goToTest"
          type="submit"
          class="mt-5 text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 self-center"
        >
          Пройти тест
        </button>
      </div>
    </div>

    <main v-else>
      <div class="q" v-if="user">
        <div class="char">
          <Cart
            v-for="score in user.scores"
            :key="score.id"
            :score="score"
            :interval="4000"
          />
        </div>
        <div class="lessonsBlock">
          <div class="header flex items-center">
            <h2 class="text-[40px]">Уроки</h2>
            <button @click="goToCreate" v-if="user.role === 'Admin'">
              Добавить
            </button>
          </div>
          <div class="flex gap-5 flex-wrap">
            <VLesson
              v-for="lesson in lessons"
              :key="lesson.id"
              :lesson="lesson"
            />
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";

import axios from "axios";
import { useAuthStore } from "../store";
import Cart from "../components/cart.vue";
import VLesson from "../components/Lesson.vue";
import { useLessonStore } from "../store/lesson";
import { Lesson } from "../types/Lesson";
import router from "../router";

axios.defaults.withCredentials = true;

const authStore = useAuthStore();
const lessonStore = useLessonStore();

const user = ref();
const lessons = ref<Lesson[]>();
const showMsg = ref(false);

const goToTest = (e: Event) => {
  e.preventDefault();
  router.push("/test");
};

const goToCreate = (e: Event) => {
  e.preventDefault();
  router.push("/create_lesson");
};

onMounted(async () => {
  user.value = authStore.getterUser;

  let minC = 0;
  let point = Number.MAX_VALUE;

  for (const score of user.value.scores) {
    if (score.score_amount < point) {
      point = score.score_amount;
      minC = score.characteristic.id;
    }
  }

  await lessonStore.fetchRecomendations(minC, point);
  lessons.value = lessonStore.getLessons;

  console.log(user.value.scores);

  for (const scores of user.value.scores) {
    if (scores.score_amount === -1) showMsg.value = true;
  }
});
</script>

<style>
.body {
  margin: 30px auto 0 auto;
  width: 80%;
}
.char {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 10px;
}

@media screen and (max-width: 1024px) {
  .char {
    width: 85vw;
  }
}
@media screen and (max-width: 768px) {
  .char {
    width: 90vw;
    flex-wrap: wrap;
    gap: 30px;
  }
}
@media screen and (max-width: 480px) {
  .char {
    gap: 15px;
  }
}
</style>
