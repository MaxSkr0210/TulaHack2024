<template>
  <div class="timer">
    <div class="v">{{ timerOutput }}</div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";

const timerOutput = ref("");

const startTimer = () => {
  const timeNow = new Date().getTime();
  const timeDifference = countDownToTime - timeNow;
  const millisecondsInOneSecond = 1000;
  const millisecondsInOneMinute = millisecondsInOneSecond * 60;
  const millisecondsInOneHour = millisecondsInOneMinute * 60;
  const millisecondsInOneDay = millisecondsInOneHour * 24;
  const differenceInDays = timeDifference / millisecondsInOneDay;
  const remainderDifferenceInHours =
    (timeDifference % millisecondsInOneDay) / millisecondsInOneHour;
  const remainderDifferenceInMinutes =
    (timeDifference % millisecondsInOneHour) / millisecondsInOneMinute;
  const remainderDifferenceInSeconds =
    (timeDifference % millisecondsInOneMinute) / millisecondsInOneSecond;
  const remainingDays = Math.floor(differenceInDays);
  const remainingHours = Math.floor(remainderDifferenceInHours);
  const remainingMinutes = Math.floor(remainderDifferenceInMinutes);
  const remainingSeconds = Math.floor(remainderDifferenceInSeconds);
  timerOutput.value =
    remainingDays +
    " Days " +
    ": " +
    remainingHours +
    " Hours " +
    ": " +
    remainingMinutes +
    " Minutes " +
    ": " +
    remainingSeconds +
    " Seconds";
};

onMounted(() => {
  const time = localStorage.getItem("countdown");
  if (time) {
  }
  const date = new Date(Date.now() + 1000 * 60 * 15);

  const countDownToTime = date.getTime();

  setInterval(() => {
    startTimer();
  }, 1000);
});
</script>
