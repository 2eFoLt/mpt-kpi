<template>
  <div id="main">
    <dashboard-header @show-add-employee-popup="showAddEmployeePopup = true" />
    <employee-dashboard-table v-if="employees" :employees="employees" />
    <add-employee-popup
      v-if="showAddEmployeePopup"
      v-model="showAddEmployeePopup"
    />
  </div>
</template>

<script>
import axios from "axios";

import DashboardHeader from "@/components/EmployeeDashboard/DashboardHeader.vue";
import AddEmployeePopup from "@/components/EmployeeDashboard/AddEmployeePopup.vue";
import EmployeeDashboardTable from "@/components/EmployeeDashboard/EmployeeDashboardTable.vue";

export default {
  data() {
    return {
      showAddEmployeePopup: false,
      employees: null,
    };
  },
  components: {
    DashboardHeader,
    AddEmployeePopup,
    EmployeeDashboardTable,
  },

  created() {
    axios.get("/api/employees/").then((response) => {
      this.employees = response.data;
      console.log(this.employees);
    });
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
