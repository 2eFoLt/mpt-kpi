<template>
  <div id="main">
    <DashboardHeader />
    <EmployeeDashboardTable />
    <AddEmployeePopup
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
      showAddEmployeePopup: true,
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
}
</style>
