import { StateTree, defineStore } from "pinia";
import axios from "axios";

axios.defaults.withCredentials = true;

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
  }),
  getters: {
    getterUser: (state: StateTree) => state.user,
  },
  actions: {
    async createUser(newUser: FormData) {
      const res = await axios.post("http://localhost:5000/reg", newUser);
    },
    async login(login: string, password: string) {
      const res = await axios.post("http://localhost:5000/login", {
        login,
        password,
      });

      console.log(res);

      localStorage.setItem("jwt", res.data.access_token);
      localStorage.setItem("refresh_jwt", res.data.refresh_token);
    },

    async refreshToken() {
      const refresh_jwt = localStorage.getItem("refresh_jwt");
      const res = await axios.get("http://localhost:5000/refresh_token", {
        headers: {
          Authorization: "Bearer " + refresh_jwt,
        },
      });
      localStorage.setItem("jwt", res.data.access_token);
    },

    async getUser() {
      import.meta.env.VITE_SERVER_URL;

      if (!localStorage.getItem("jwt")) return;
      const auth = "Bearer " + localStorage.getItem("jwt");

      const res = await axios.get("http://localhost:5000/protected", {
        headers: {
          Authorization: auth,
        },
      });

      console.log(res.data.logged_in_as);

      this.user = await res.data.logged_in_as;
    },
  },
});
