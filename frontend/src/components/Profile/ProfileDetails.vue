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
    <div
      class="criterion-secition"
      v-for="criterion in extendedCriteriesList"
      :key="criterion.id"
    >
      <h2 class="criterion-title">
        {{ criterion.name }}
      </h2>
      <div class="certificate-list">
        <div
          class="certificate"
          v-for="certificate in criterion.certificates"
          :key="certificate.id"
        >
          <img
            class="certificate_preview"
            :src="certificate.preview_url"
            alt="Здесь должно быть превью документа"
          />
          {{ truncateCertificateName(criterion.name) }}
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import AddIcon from "@/components/Icons/AddIcon.vue";

export default {
  emits: ["showAddCertificatePopup"],
  props: ["criteries", "certificates"],
  components: {
    AddIcon,
  },

  computed: {
    extendedCriteriesList() {
      const local_criteries = this.criteries.map((criterion) => {
        return {
          ...criterion,
          certificates: [],
        };
      });

      this.certificates.map((certificate) => {
        const criterion_index = this.criteries.findIndex(
          (criterion) => certificate.criterion_id === criterion.id
        );
        if (criterion_index < 0) return;
        local_criteries[criterion_index].certificates.push(certificate);
      });

      return local_criteries.filter(
        (criterion) => criterion.certificates.length !== 0
      );
    },
  },
  methods: {
    truncateCertificateName(text, maxlength = 23) {
      return text.length > maxlength
        ? text.slice(0, maxlength - 1) + "…"
        : text;
    },
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
    flex-direction: row;
    height: 100%;
    width: 100%;
    max-height: 10em;
    gap: 4.3125em;
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
.certificate_preview {
    width: 14.375em;
    height: 8.625em;
    object-fit: cover;
    border-radius: 0.75em;
}

.certificate {
    display: flex;
    flex-direction: column;
    font-variation-settings: "wght" 500;
	font-weight: 500;
    gap: 0.25em;
}

.criterion-title {
    padding-bottom: 2em;
	font-size: 1.6em;
    font-variation-settings: "wght" 600;
	font-weight: 600;
}
</style>
