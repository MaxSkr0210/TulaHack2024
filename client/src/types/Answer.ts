import { CharPoints } from "./Point";

export interface Answer {
  id: number;
  answer_text: string;
  characteristics: CharPoints[];
}
