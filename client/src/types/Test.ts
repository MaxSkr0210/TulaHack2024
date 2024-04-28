import { Question } from "./QuestionResponse";

export interface Test {
  id: number;
  title: string;
  questions: Question[];
}
