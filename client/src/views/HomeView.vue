<template>
  <div class="home h-full" v-if="user">
    <div class="char">
      <Cart
        v-for="score in user.scores"
        :key="score.id"
        :score="score"
        :interval="4000"
      />
    </div>
    <div class="lessonsBlock">
      <h2 class="text-[40px]">Уроки</h2>
      <div class="flex gap-5 flex-wrap">
        <VLesson v-for="lesson in lessons" :key="lesson.id" :lesson="lesson" />
      </div>
    </div>
    <Msg v-if="showMsg" />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";

import axios from "axios";
import { useAuthStore } from "../store";
import Cart from "../components/cart.vue";
import Msg from "../components/Msg.vue";
import VLesson from "../components/Lesson.vue";
import { useLessonStore } from "../store/lesson";
import { Lesson } from "../types/Lesson";

axios.defaults.withCredentials = true;

const authStore = useAuthStore();
const lessonStore = useLessonStore();

const user = ref();
const lessons = ref<Lesson[]>();
const showMsg = ref(false);

onMounted(async () => {
  await lessonStore.fetchLessons();
  user.value = authStore.getterUser;
  lessons.value = lessonStore.getLessons;

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
