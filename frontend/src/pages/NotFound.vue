<template>
  <main class="centre-container">
    <section class="main-section">
      <div class="not-found">
        <h1>Страница 404</h1>
      </div>
      <CustomRequestsManager />
    </section>
  </main>
</template>

<style scoped>
.centre-container {
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<script>
import CustomRequestsManager from "@/components/CustomRequestsManager/RequestsManager.vue";
export default {
  components: {
    CustomRequestsManager,
  },
};
</script>
