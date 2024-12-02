<template>
  <section id="workspace">
    <div class="section-header">
      <h1 class="section-header-title">Сертификаты</h1>
      <div
        class="add-certificate"
        @click="$emit('showAddCertificatePopup', true)"
      >
        <add-icon />
      </div>
    </div>
    <div class="certificate-list"></div>
  </section>
</template>

<script>
import AddIcon from "@/components/Icons/AddIcon.vue";

export default {
  emits: ["showAddCertificatePopup"],

  components: {
    AddIcon,
  },
};
</script>

<style lang="sass" scoped>
#workspace {
    color: white;
    display: flex;
    flex-direction: column;
    gap: 3em;

    padding: 1.5em 2.75em;
}

.certificate-list {
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    height: 100%;
    width: 100%;
    max-height: 10em;
}

.add-certificate {
    width: 100%;
    height: 8.6em;

    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #DEF1FF;
    border-radius: 0.75em;
    cursor: pointer;
}

.section-header-title {
    font-size: 2.5em;
    font-variation-settings: "wght" 600;
    font-weight: 600;
    padding-bottom: 0.5em;
}
</style>
