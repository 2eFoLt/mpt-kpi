<template>
  <div id="main">
    <ProfileMenu />
    <div class="details">
      <ProfileDetails />
    </div>
  </div>
</template>

<script>
import ProfileMenu from "@/components/Profile/ProfileMenu.vue";
import ProfileDetails from "@/components/Profile/ProfileDetails.vue";

export default {
  components: {
    ProfileMenu,
    ProfileDetails,
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
