import { defineStore } from "pinia";
import axios from "axios";
import { Lesson } from "../types/Lesson";
import Lesson from "../components/Lesson.vue";

axios.defaults.withCredentials = true;

export const useLessonStore = defineStore("lesson", {
  state: () => ({
    lessons: [] as Lesson[],
    lesson: {} as Lesson,
  }),
  actions: {
    async fetchLessons() {
      const res = await axios.get("http://localhost:5000/lesson");

      this.lessons = res.data;
    },
    async fetchLessonById(id: number) {
      const res = await axios.get("http://localhost:5000/lesson/" + id);

      this.lesson = res.data;
    },
  },
  getters: {
    getLessons: (state) => state.lessons,
    getLesson: (state) => state.lesson,
  },
});
