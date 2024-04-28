import { defineStore } from "pinia";
import axios from "axios";
import { CharPoints } from "../types/Point";
import { Test } from "../types/Test";

axios.defaults.withCredentials = true;

export const useTestStore = defineStore("test", {
  state: () => ({
    test: {
      id: 1,
      title: "Моя викторина",
      description: "Викторина",
      questions: [
        {
          id: 1,
          question_text: "Как вы предпочитаете работать над проектом?",
          answers: [
            {
              id: 1,
              answer_text:
                "Я работаю один, предпочитаю минимальное взаимодействие.",
              characteristics: [
                { characteristics_id: 4, score: 1 },
                { characteristics_id: 3, score: 1 },
              ],
            },
            {
              id: 2,
              answer_text:
                "Я работаю один, но регулярно докладываю о своих результатах.",
              characteristics: [
                { characteristics_id: 4, score: 2 },
                { characteristics_id: 3, score: 2 },
              ],
            },
            {
              id: 3,
              answer_text:
                "Я работаю в команде, участвую в обсуждениях, но вношу свои идеи редко.",
              characteristics: [
                { characteristics_id: 4, score: 3 },
                { characteristics_id: 3, score: 3 },
              ],
            },
            {
              id: 4,
              answer_text:
                "Я активно сотрудничаю, координирую действия, предлагаю новые идеи.",
              characteristics: [
                { characteristics_id: 4, score: 4 },
                { characteristics_id: 3, score: 4 },
              ],
            },
          ],
        },
        {
          id: 2,
          question_text: "Как вы справляетесь с конфликтами в команде?",
          answers: [
            {
              id: 5,
              answer_text: "Я стараюсь избегать конфликтов, не вмешиваюсь.",
              characteristics: [
                { characteristics_id: 3, score: 1 },
                { characteristics_id: 4, score: 1 },
              ],
            },
            {
              id: 6,
              answer_text:
                "Я следую правилам и надеюсь, что всё разрешится само.",
              characteristics: [
                { characteristics_id: 3, score: 2 },
                { characteristics_id: 4, score: 2 },
              ],
            },
            {
              id: 7,
              answer_text:
                "Я стараюсь выслушать обе стороны и найти компромисс.",
              characteristics: [
                { characteristics_id: 3, score: 3 },
                { characteristics_id: 4, score: 3 },
              ],
            },
            {
              id: 8,
              answer_text:
                "Я активно решаю конфликты, предлагая решения, которые устраивают всех.",
              characteristics: [
                { characteristics_id: 3, score: 4 },
                { characteristics_id: 4, score: 4 },
              ],
            },
          ],
        },
        {
          id: 3,
          question_text:
            "Как вы реагируете на новые идеи или изменения в проекте?",
          answers: [
            {
              id: 9,
              answer_text:
                "Я предпочитаю работать по плану, изменения вызывают стресс.",
              characteristics: [{ characteristics_id: 2, score: 1 }],
            },
            {
              id: 10,
              answer_text:
                "Я принимаю изменения, но мне нужно время, чтобы привыкнуть.",
              characteristics: [{ characteristics_id: 2, score: 2 }],
            },
            {
              id: 11,
              answer_text:
                "Я открыт новым идеям и могу адаптироваться относительно быстро.",
              characteristics: [{ characteristics_id: 2, score: 3 }],
            },
            {
              id: 12,
              answer_text:
                "Я активно предлагаю новые идеи и всегда готов к изменениям.",
              characteristics: [{ characteristics_id: 2, score: 4 }],
            },
          ],
        },
        {
          id: 4,
          question_text:
            "Что вы делаете, если сталкиваетесь с проблемой в проекте?",
          answers: [
            {
              id: 13,
              answer_text:
                "Я стараюсь избежать проблемы или переложить её на других.",
              characteristics: [{ characteristics_id: 1, score: 1 }],
            },
            {
              id: 14,
              answer_text:
                "Я стараюсь решить проблему по мере сил, но могу попросить помощи.",
              characteristics: [{ characteristics_id: 1, score: 2 }],
            },
            {
              id: 15,
              answer_text: "Я анализирую проблему и ищу возможные решения.",
              characteristics: [{ characteristics_id: 1, score: 3 }],
            },
            {
              id: 16,
              answer_text:
                "Я предлагаю несколько вариантов решения и обсуждаю их с командой.",
              characteristics: [
                { characteristics_id: 1, score: 4 },
                { characteristics_id: 4, score: 2 },
              ],
            },
          ],
        },
        {
          id: 5,
          question_text: "Как бы вы описали своё отношение к обратной связи?",
          answers: [
            {
              id: 17,
              answer_text:
                "Я избегаю обратной связи, так как она вызывает дискомфорт.",
              characteristics: [{ characteristics_id: 3, score: 1 }],
            },
            {
              id: 18,
              answer_text:
                "Я принимаю обратную связь, но могу реагировать эмоционально.",
              characteristics: [{ characteristics_id: 3, score: 2 }],
            },
            {
              id: 19,
              answer_text:
                "Я приветствую конструктивную критику и использую её для улучшения.",
              characteristics: [{ characteristics_id: 3, score: 3 }],
            },
            {
              id: 20,
              answer_text: "Я активно прошу обратную связь и даю её другим.",
              characteristics: [{ characteristics_id: 3, score: 4 }],
            },
          ],
        },
        {
          id: 6,
          question_text: "Как вы обычно решаете творческие задачи?",
          answers: [
            {
              id: 21,
              answer_text:
                "Я следую проверенным методам и редко отступаю от них.",
              characteristics: [{ characteristics_id: 2, score: 1 }],
            },
            {
              id: 22,
              answer_text:
                "Я пытаюсь использовать различные методы, но предпочитаю надежные пути.",
              characteristics: [{ characteristics_id: 2, score: 2 }],
            },
            {
              id: 23,
              answer_text:
                "Я использую широкий набор методов и экспериментирую.",
              characteristics: [{ characteristics_id: 2, score: 3 }],
            },
            {
              id: 24,
              answer_text:
                "Я постоянно ищу новые пути и предлагаю креативные решения.",
              characteristics: [{ characteristics_id: 2, score: 4 }],
            },
          ],
        },
        {
          id: 7,
          question_text: "Как вы подходите к планированию проектов?",
          answers: [
            {
              id: 25,
              answer_text:
                "Я предпочитаю не планировать заранее и действую по обстоятельствам.",
              characteristics: [{ characteristics_id: 1, score: 1 }],
            },
            {
              id: 26,
              answer_text: "Я составляю простой план и следую ему.",
              characteristics: [{ characteristics_id: 1, score: 2 }],
            },
            {
              id: 27,
              answer_text:
                "Я составляю детальный план и вношу в него коррективы по ходу работы.",
              characteristics: [{ characteristics_id: 1, score: 3 }],
            },
            {
              id: 28,
              answer_text:
                "Я планирую тщательно и учитываю риски, регулярно оцениваю результаты.",
              characteristics: [{ characteristics_id: 1, score: 4 }],
            },
          ],
        },
        {
          id: 8,
          question_text:
            "Как часто вы делитесь своими идеями или мыслями с командой?",
          answers: [
            {
              id: 29,
              answer_text: "Я предпочитаю держать свои идеи при себе.",
              characteristics: [{ characteristics_id: 3, score: 1 }],
            },
            {
              id: 30,
              answer_text: "Я делюсь идеями, когда меня спрашивают.",
              characteristics: [{ characteristics_id: 3, score: 2 }],
            },
            {
              id: 31,
              answer_text: "Я делюсь идеями, если они могут помочь проекту.",
              characteristics: [{ characteristics_id: 3, score: 3 }],
            },
            {
              id: 32,
              answer_text:
                "Я регулярно предлагаю идеи и активно участвую в обсуждениях.",
              characteristics: [{ characteristics_id: 3, score: 4 }],
            },
          ],
        },
        {
          id: 9,
          question_text: "Как вы обычно принимаете решения в проекте?",
          answers: [
            {
              id: 33,
              answer_text: "Я предпочитаю, чтобы решения принимали другие.",
              characteristics: [{ characteristics_id: 1, score: 1 }],
            },
            {
              id: 34,
              answer_text:
                "Я принимаю решения, основываясь на рекомендациях других.",
              characteristics: [{ characteristics_id: 1, score: 2 }],
            },
            {
              id: 35,
              answer_text:
                "Я принимаю решения, основываясь на данных и анализе.",
              characteristics: [{ characteristics_id: 1, score: 3 }],
            },
            {
              id: 36,
              answer_text:
                "Я принимаю решения, учитывая мнение команды и возможные риски.",
              characteristics: [
                { characteristics_id: 1, score: 4 },
                { characteristics_id: 3, score: 2 },
              ],
            },
          ],
        },
        {
          id: 10,
          question_text: "Как вы относитесь к работе в группе?",
          answers: [
            {
              id: 37,
              answer_text:
                "Я предпочитаю работать в одиночку, а в группе чувствую себя некомфортно.",
              characteristics: [{ characteristics_id: 4, score: 1 }],
            },
            {
              id: 38,
              answer_text:
                "Я работаю в группе, но предпочитаю четко определенные роли.",
              characteristics: [{ characteristics_id: 4, score: 2 }],
            },
            {
              id: 39,
              answer_text:
                "Я чувствую себя комфортно в группе, активно участвую в обсуждениях.",
              characteristics: [{ characteristics_id: 4, score: 3 }],
            },
            {
              id: 40,
              answer_text:
                "Я предпочитаю работать в команде и беру на себя лидерские роли.",
              characteristics: [{ characteristics_id: 4, score: 4 }],
            },
          ],
        },
      ],
    } as Test,
    points: [] as CharPoints[],
  }),
  actions: {
    addAnswer(points: CharPoints[]) {
      if (this.points.length === 0) this.points.push(...points);
      else {
        for (let i = 0; i < points.length; i++) {
          for (let j = 0; j < this.points.length; j++) {
            if (
              this.points[j].characteristics_id === points[i].characteristics_id
            ) {
              this.points[j].score += points[i].score;
              break;
            } else {
              this.points.push(points[i]);
              break;
            }
          }
        }
      }
    },
    async updateScore(user_id: number) {
      await axios.put("http://localhost:5000/score/" + user_id, {
        results: this.points,
      });
    },
  },
  getters: {
    getPoints: (state) => state.points,
    getTest: (state) => state.test,
  },
});
