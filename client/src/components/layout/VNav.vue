<template>
  <fwb-navbar v-if="user">
    <template #logo>
      <fwb-navbar-logo
        alt="Flowbite logo"
        image-url="/images/logo.svg"
        link="#"
      >
        Flowbite
      </fwb-navbar-logo>
    </template>
    <template #default="{ isShowMenu }">
      <fwb-navbar-collapse :is-show-menu="isShowMenu">
        <fwb-navbar-link is-active link="#"> Home </fwb-navbar-link>
        <fwb-navbar-link link="#"> Services </fwb-navbar-link>
        <fwb-navbar-link link="#"> Pricing </fwb-navbar-link>
        <fwb-navbar-link link="#"> Contact </fwb-navbar-link>
      </fwb-navbar-collapse>
    </template>
    <template #right-side>
      {{ user.first_name }} {{ user.last_name }}
      <fwb-img
        class="w-36"
        alt="ava"
        :src="`http://localhost:5000/img/` + user.avatar_path"
      />
    </template>
  </fwb-navbar>
</template>

<script setup lang="ts">
import {
  FwbImg,
  FwbNavbar,
  FwbNavbarCollapse,
  FwbNavbarLink,
  FwbNavbarLogo,
} from "flowbite-vue";
import { useAuthStore } from "../../store";
import { onMounted, ref } from "vue";

const store = useAuthStore();

const user = ref();

onMounted(() => {
  user.value = store.getterUser;
});
</script>
