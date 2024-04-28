<template>
  <div>
    <p v-html="question.question_text"></p>
    <div class="flex flex-col gap-2 mt-4">
      <fwb-button
        size="md"
        v-for="answer in question.answers"
        v-html="answer.answer_text"
        @click="setAnswer($event, answer)"
      ></fwb-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Question } from "..//types/QuestionResponse";
import { FwbButton } from "flowbite-vue";
import { Answer } from "../types/Answer";

defineProps<{
  question: Question;
}>();

const $emits = defineEmits(["answer"]);

const setAnswer = (e: Event, answer: Answer) => {
  $emits("answer", e, answer);
};
</script>
