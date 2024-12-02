<template>
  <div id="main">
    <profile-menu />
    <div class="details">
      <profile-details
        v-if="criteries && certificates"
        :criteries="criteries"
        :certificates="certificates"
        @show-add-certificate-popup="showAddCertificatePopup = $event"
      />
    </div>
    <add-certificate-popup
      v-if="showAddCertificatePopup"
      v-model="showAddCertificatePopup"
      :criteries="criteries"
    />
  </div>
</template>

<script>
import axios from "axios";

import ProfileMenu from "@/components/Profile/ProfileMenu.vue";
import ProfileDetails from "@/components/Profile/ProfileDetails.vue";
import AddCertificatePopup from "@/components/Profile/AddCertificatePopup.vue";

export default {
  data() {
    return {
      showAddCertificatePopup: false,
      criteries: null,
      certificates: null,
    };
  },
  components: {
    ProfileMenu,
    ProfileDetails,
    AddCertificatePopup,
  },

  created() {
    axios.get("/api/criteries/").then((response) => {
      this.criteries = response.data;
    });
    axios.get("/api/certificates/").then((response) => {
      this.certificates = response.data;
    });
  },
};
</script>

<style lang="sass" scoped>
#main {
	min-height: 100vh;
	background: #5076B6;

	display: flex;
}

.details {
	padding-bottom: 2em;
	padding-left: .8em;

	flex-grow: 1;
	position: relative;
}
</style>
