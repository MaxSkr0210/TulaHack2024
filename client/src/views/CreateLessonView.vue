<template>
  <div class="craete">
    <form>
      <fwb-input
        v-model="title"
        label="Заголовок"
        placeholder="Введите заголовок урока"
        size="md"
      />

      <fwb-input
        v-model="description"
        label="Описание"
        placeholder="Введите краткое описание урока"
        size="md"
      />

      <fwb-textarea
        v-model="content"
        :rows="4"
        label="Содержимое урока"
        placeholder="Введите содержимое урока"
      />

      <fwb-input
        v-model="minPoint"
        label="Порок очков"
        placeholder="Введите количество очков"
        size="md"
      />

      <fwb-select
        v-model="selected"
        :options="characteristicsSelect"
        label="Выерете тип скила"
        size="md"
      />

      <fwb-file-input v-model="file" label="Загрузите картинку">
        <p class="!mt-1 text-sm text-gray-500 dark:text-gray-300">
          PNG или JPG
        </p>
      </fwb-file-input>

      <button @click="createLesson">Создать</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { FwbFileInput, FwbInput, FwbTextarea, FwbSelect } from "flowbite-vue";
import { useLessonStore } from "../store/lesson";

const store = useLessonStore();

const file = ref();
const description = ref("");
const title = ref("");
const content = ref("");
const minPoint = ref("");
const selected = ref("");
const characteristicsSelect = ref<any[]>([]);

const createLesson = async (e: Event) => {
  e.preventDefault();
  const formData = new FormData();

  formData.append("title", title.value);
  formData.append("description", description.value);
  formData.append("content", content.value);
  formData.append("min_point", minPoint.value);
  formData.append("sod", selected.value.toString());
  formData.append("img_path", file.value);

  await store.createLesson(formData);
};

onMounted(async () => {
  await store.fetchCharacteristic();
  const characteristics = store.getcharacteristics;

  for (const characteristic of characteristics) {
    characteristicsSelect.value.push({
      value: characteristic.id,
      name: characteristic.name,
    });
  }

  console.log(characteristicsSelect.value);
});
</script>
