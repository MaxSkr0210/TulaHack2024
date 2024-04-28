<template>
  <div class="craete">
    <form>
      <fwb-input
        v-model="firstName"
        label="Имя"
        placeholder="Введите имя сотрудника"
        size="md"
      />

      <fwb-input
        v-model="lastName"
        label="Фамилия"
        placeholder="Введите фамилию сотрудника"
        size="md"
      />

      <fwb-input
        v-model="login"
        label="Пароль"
        placeholder="Создайте логин для сотрудника"
        size="md"
      />

      <fwb-input
        v-model="password"
        label="Пароль"
        placeholder="Создайте пароль для сотрудника"
        size="md"
      />

      <fwb-input
        v-model="rePassword"
        label="Пароль"
        placeholder="Повторите пароль"
        size="md"
      />

      <fwb-file-input v-model="file" label="Загрузите аватарку">
        <p class="!mt-1 text-sm text-gray-500 dark:text-gray-300">
          PNG или JPG
        </p>
      </fwb-file-input>

      <button @click="createLesson">Создать</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { FwbFileInput, FwbInput } from "flowbite-vue";
import router from "../router";
import { useAuthStore } from "../store";

const store = useAuthStore();

const file = ref();
const firstName = ref("");
const lastName = ref("");
const login = ref("");
const password = ref("");
const rePassword = ref("");
const characteristicsSelect = ref<any[]>([]);

const createLesson = async (e: Event) => {
  e.preventDefault();
  const formData = new FormData();

  if (password.value !== rePassword.value) return;
  formData.append("login", login.value);
  formData.append("password", password.value);
  formData.append("first_name", firstName.value);
  formData.append("last_name", lastName.value);
  formData.append("avatar_path", file.value);

  await store.createUser(formData);
  router.push("/");
};
</script>
