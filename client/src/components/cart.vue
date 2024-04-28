<template>
  <div class="container">
    <i class="fas fa-utensils"></i>
    <span
      class="num"
      :data-val="score.score_amount"
      v-if="score.score_amount > 0"
      ref="valueDisplay"
      >0</span
    >
    <span class="num" v-else>0</span>
    <span class="text">{{ score.characteristic.name }}</span>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";

const props = defineProps({
  score: {
    type: Object,
    required: true,
  },
  interval: {
    type: Number,
    required: true,
  },
});

const valueDisplay = ref();

onMounted(() => {
  let startValue = 0;

  if (valueDisplay.value) {
    let endValue = parseInt(valueDisplay.value.getAttribute("data-val"));
    let duration = Math.floor(props.interval / endValue) / 2;
    let counter = setInterval(function () {
      startValue += 1;
      valueDisplay.value.textContent = startValue;
      if (startValue === endValue) {
        clearInterval(counter);
      }
    }, duration);
  }
});
</script>

<style scoped>
.container {
  width: 28vmin;
  height: 28vmin;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  padding: 1em 0;
  position: relative;
  font-size: 16px;
  border-radius: 0.5em;
  background-color: #21242b;
  border-bottom: 10px solid #18f98f;
}
i {
  color: #18f98f;
  font-size: 2.5em;
  text-align: center;
}
span.num {
  color: #ffffff;
  display: grid;
  place-items: center;
  font-weight: 600;
  font-size: 3em;
}
span.text {
  color: #e0e0e0;
  font-size: 1em;
  text-align: center;
  pad: 0.7em 0;
  font-weight: 400;
  line-height: 0;
}
@media screen and (max-width: 1024px) {
  .container {
    height: 26vmin;
    width: 26vmin;
    font-size: 12px;
  }
}
@media screen and (max-width: 768px) {
  .container {
    width: calc(50% - 40px);
    height: 30vmin;
    font-size: 14px;
  }
}
@media screen and (max-width: 480px) {
  .container {
    width: 100%;
    height: 25vmin;
    font-size: 8px;
  }
}
</style>
