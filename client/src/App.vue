<script setup lang="ts"></script>

<template>
  <div id="app">
    <VNav />
    <div class="body">
      <router-view />
    </div>
  </div>
</template>

<script setup lang="ts">
import VNav from "./components/layout/VNav.vue";
</script>
