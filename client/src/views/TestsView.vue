<template>
  <div class="tests">
    123
    <!-- <VTest v-for="test in tests" :test="test" /> -->
  </div>
</template>

<!-- <script setup lang="ts">
import { onMounted, ref } from "vue";
import { useTestStore } from "../store/test";
import { Test } from "../types/Test";
import VTest from "../components/test.vue";

const testStore = useTestStore();

const tests = ref<Test[]>();

onMounted(async () => {
  await testStore.fetchTests();
  tests.value = testStore.getTests;
});
</script> -->
