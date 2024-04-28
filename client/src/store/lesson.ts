import { defineStore } from "pinia";
import axios from "axios";
import { Lesson } from "../types/Lesson";

axios.defaults.withCredentials = true;

export const useLessonStore = defineStore("lesson", {
  state: () => ({
    lessons: [] as Lesson[],
    lesson: {} as Lesson,
    characteristic: [] as { id: number; name: string }[],
  }),
  actions: {
    async fetchLessons() {
      const res = await axios.get("http://localhost:5000/lesson");

      this.lessons = res.data;
    },
    async fetchRecomendations(characteristic_id: number, point: number) {
      const res = await axios.get(
        `http://localhost:5000/lesson/recomenfation?characteristic_id=${characteristic_id}&point=${point}`,
      );
      console.log(res.data);

      if (res.data.length === 0) {
        await this.fetchLessons();
        return;
      }

      this.lessons = res.data;
    },
    async fetchLessonById(id: number) {
      const res = await axios.get("http://localhost:5000/lesson/" + id);

      this.lesson = res.data;
    },

    async fetchCharacteristic() {
      const res = await axios.get("http://localhost:5000/characteristic");

      this.characteristic = res.data;
    },

    async createLesson(fromData: FormData) {
      const res = axios.post("http://localhost:5000/lesson", fromData);
      console.log(res);
    },
  },
  getters: {
    getLessons: (state) => state.lessons,
    getLesson: (state) => state.lesson,
    getcharacteristics: (state) => state.characteristic,
  },
});
