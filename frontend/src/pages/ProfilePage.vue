<template>
  <div id="main">
    <ProfileMenu />
    <div class="details">
      <ProfileDetails />
    </div>
    <AddCertificatePopup
      v-if="showAddCertificatePopup"
      v-model="showAddCertificatePopup"
    />
  </div>
</template>

<script>
import ProfileMenu from "@/components/Profile/ProfileMenu.vue";
import ProfileDetails from "@/components/Profile/ProfileDetails.vue";
import AddCertificatePopup from "@/components/Profile/AddCertificatePopup.vue";

export default {
  data() {
    return {
      showAddCertificatePopup: true,
    };
  },
  components: {
    ProfileMenu,
    ProfileDetails,
    AddCertificatePopup,
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
