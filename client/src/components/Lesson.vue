<template>
  <div class="lesson">
    <fwb-card
      img-alt="Desk"
      img-src="https://flowbite.com/docs/images/blog/image-1.jpg"
      variant="image"
    >
      <div class="p-5">
        <h5
          class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
          @click="goToLesson"
        >
          {{ lesson.title }}
        </h5>
        <p class="font-normal text-gray-700 dark:text-gray-400">
          {{ lesson.description }}
        </p>
      </div>
    </fwb-card>
  </div>
</template>

<script setup lang="ts">
import { FwbCard } from "flowbite-vue";
import { Lesson } from "../types/Lesson";
import router from "../router";

const props = defineProps<{
  lesson: Lesson;
}>();

const goToLesson = (e: Event) => {
  console.log(178);

  e.preventDefault();
  router.push("/lessons/" + props.lesson.id);
};
</script>
