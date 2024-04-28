<template>
  <div class="lesson">
    {{ lesson?.content }}
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useLessonStore } from "../store/lesson";
import { Lesson } from "../types/Lesson";

const lesson = ref<Lesson>();

const route = useRoute();
const store = useLessonStore();

onMounted(async () => {
  const id = Number(route.params.id);
  await store.fetchLessonById(id);
  lesson.value = store.getLesson;
});
</script>
