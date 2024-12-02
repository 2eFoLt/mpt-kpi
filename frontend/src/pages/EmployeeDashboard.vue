<template>
  <div id="main">
    <dashboard-header @show-add-employee-popup="showAddEmployeePopup = true" />
    <employee-dashboard-table />
    <add-employee-popup
      v-if="showAddEmployeePopup"
      v-model="showAddEmployeePopup"
    />
  </div>
</template>

<script>
import DashboardHeader from "@/components/EmployeeDashboard/DashboardHeader.vue";
import AddEmployeePopup from "@/components/EmployeeDashboard/AddEmployeePopup.vue";
import EmployeeDashboardTable from "@/components/EmployeeDashboard/EmployeeDashboardTable.vue";

export default {
  data() {
    return {
      showAddEmployeePopup: false,
    };
  },
  components: {
    DashboardHeader,
    AddEmployeePopup,
    EmployeeDashboardTable,
  },
};
</script>

<style lang="sass" scoped>
#main {
	min-height: 100vh;
	background: #5076B6;
    padding: 3em 2.75em;
}
</style>
