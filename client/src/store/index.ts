import { StateTree, defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  actions: {
    state: () => ({
      user: null,
    }),
    async login(login: string, password: string) {
      const res = await axios.post("http://localhost:5000/login", {
        login,
        password,
      });

      localStorage.setItem("jwt", res.data.access_token);
    },
    getters: {
      getterUser: (state: StateTree) => state.user,
    },
    // async getUser() {
    //   if (!localStorage.getItem("jwt")) return;
    //   const auth = "Bearer " + localStorage.getItem("jwt");

    //   const res = await axios.get("http://localhost:5000/protected", {
    //     headers: {
    //       Authorization: auth,
    //     },
    //   });

    //   console.log(132);

    //   this.user = await res.data.logged_in_as;
    // },
  },
});
