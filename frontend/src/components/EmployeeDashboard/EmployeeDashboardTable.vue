<template>
  <table class="employee-dashboard-table">
    <tr class="table-head">
      <th class="employee-id-column">#</th>
      <th class="name-column">Имя</th>
      <th class="last-name-column">Фамилия</th>
      <th class="surname-column">Отчество</th>
      <th class="job-name-column">Должность</th>
      <th class="phone-column">Номер телефона</th>
      <th class="email-column">Рабочая почта</th>
      <th class="controls-column"></th>
    </tr>
    <tr v-for="employee in employees" :key="employee.id">
      <td class="employee-id">{{ employee.id }}</td>
      <td class="name">{{ employee.first_name }}</td>
      <td class="last-name">{{ employee.last_name }}</td>
      <td class="surname">{{ employee.surname }}</td>
      <td class="job-name">{{ employee.job_id }}</td>
      <td class="phone">{{ employee.phone }}</td>
      <td class="email">{{ employee.email }}</td>
      <td class="controls">
        <edit-icon />
        <delete-icon />
      </td>
    </tr>
  </table>
</template>

<script>
import EditIcon from "@/components/Icons/EditIcon.vue";
import DeleteIcon from "@/components/Icons/DeleteIcon.vue";

export default {
  props: ["employees", "jobs"],
  components: [EditIcon, DeleteIcon],
};
</script>

<style lang="sass" scoped>
.employee-dashboard-table {
    background-color: white;
    width: 100%;
    padding: 0 0.625em;
    border-radius: 0.75em;
}

.table-head {
    font-variation-settings: "wght" 600;
	font-weight: 600;
    padding-bottom: 0.5em;
    text-align: left;
}

.icon-delete,
.icon-edit {
    margin: 0 0.5em;
}
</style>
