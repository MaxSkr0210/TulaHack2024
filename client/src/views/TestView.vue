<template>
  <div class="test flex items-center justify-center" v-if="test">
    <fwb-card class="relative">
      <div class="p-5">
        <h5
          class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
        >
          {{ test.title }}
        </h5>
        <TheQuestion
          v-if="showQuestion"
          @answer="setAnswer"
          :question="test.questions[currentIndex]"
          :key="currentIndex"
        />
      </div>
    </fwb-card>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { Test } from "../types/Test";
import { FwbCard } from "flowbite-vue";
import { Answer } from "../types/Answer";
import { useTestStore } from "../store/test";
import TheQuestion from "../components/TheQuestion.vue";
import { useAuthStore } from "../store";
import router from "../router";

const showQuestion = ref(true);
const showResQuestion = ref(false);
const showResult = ref(false);

const currentIndex = ref(0);

const answer = ref<Answer>();
const test = ref<Test>();

const testStore = useTestStore();
const authStore = useAuthStore();

const setAnswer = async (e: Event, data: Answer) => {
  e.preventDefault();
  testStore.addAnswer(data.characteristics);

  if (test.value.questions.length - 1 > currentIndex.value) {
    currentIndex.value++;
  } else {
    showQuestion.value = false;
    showResult.value = true;
    const userId = authStore.getterUser.id;

    await testStore.updateScore(userId);
    router.push("/");
  }
};

onMounted(() => {
  test.value = testStore.getTest;
});
</script>

<style>
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.25);
  }
  100% {
    transform: scale(1);
  }
}
</style>
