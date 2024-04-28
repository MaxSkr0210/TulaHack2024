<template>
  <div class="lesson">
    <fwb-card
      img-alt="Desk"
      img-src="https://flowbite.com/docs/images/blog/image-1.jpg"
      variant="image"
      @click="goTotest($event, test.id)"
    >
      <div class="p-5">
        <h5
          class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
        >
          {{ test.title }}
        </h5>
      </div>
    </fwb-card>
  </div>
</template>

<script setup lang="ts">
import { FwbCard } from "flowbite-vue";
import { Test } from "../types/Test";
import router from "../router";

defineProps<{
  test: Test;
}>();

const goTotest = (e: Event, id: number) => {
  e.preventDefault();
  router.push("/tests/" + id);
};
</script>
