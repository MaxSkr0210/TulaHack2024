<template>
  <div
    class="modal z-10 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
  >
    <fwb-card variant="image">
      <div class="p-5">
        <h5
          class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
        >
          Хз че написать
        </h5>
        <p class="font-normal text-gray-700 dark:text-gray-400">
          Короче пройдите тест
        </p>
        <button
          @click="goToTest"
          type="submit"
          class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
        >
          Пройти тест
        </button>
      </div>
    </fwb-card>
  </div>
</template>

<script setup lang="ts">
import { FwbCard } from "flowbite-vue";
import router from "../router";

const goToTest = (e: Event) => {
  e.preventDefault();
  router.push("/test");
};
</script>
