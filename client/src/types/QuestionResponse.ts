import { Answer } from "./Answer";

export interface Question {
  id: number;
  question_text: string;
  answers: Answer[];
}
