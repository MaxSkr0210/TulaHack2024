<script setup lang="ts">
import { FwbImg, FwbNavbar } from "flowbite-vue";
import { useAuthStore } from "./store";
import { ref, watch } from "vue";

const host = import.meta.env.VITE_SERVER_URL;
const authStore = useAuthStore();

const user = ref();

watch(
  () => authStore.user,
  (val) => {
    user.value = val;
  },
);
</script>

<template>
  <div id="app">
    <fwb-navbar v-if="user">
      <template #logo> Skils Up </template>
      <template #right-side>
        {{ user.first_name }} {{ user.last_name }}
        <fwb-img
          class="w-36"
          alt="ava"
          :src="host + `/img/` + user.avatar_path"
        />
      </template>
    </fwb-navbar>
    <div class="body">
      <router-view />
    </div>
  </div>
</template>
