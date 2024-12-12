<template>
  <header id="dashboard-header">
    <div class="dashboard-navigation">
      <h1 class="section-header-title">Сотрудники</h1>
      <router-link :to="{ name: 'profile' }">Личный кабинет</router-link>
    </div>
    <div class="dashboard-filters">
      <input
        class="input"
        type="text"
        id="filter-text"
        placeholder="Поиск"
        v-model="filterText"
      />
      <select class="input" v-model="filterJobId">
        <option>Должность</option>
      </select>
      <div
        class="add-employee button"
        @click="$emit('showAddEmployeePopup', true)"
      >
        <svg
          class="add-employee-icon"
          width="18"
          height="18"
          viewBox="0 0 18 18"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M9 16V2M2 9H16"
            stroke="white"
            stroke-width="3"
            stroke-linecap="round"
          />
        </svg>
        <span>Добавить</span>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  emits: ["showAddEmployeePopup"],
  data() {
    return {
      filterText: "",
      filterJobId: 0,
    };
  },
};
</script>

<style lang="sass" scoped>
#dashboard-header {
    color: white;
    padding: 1em 0;
}

.dashboard-filters,
.dashboard-navigation {
    display: flex;
    flex-direction: row;
	justify-content: space-between;
    align-items: center;
}

.section-header-title {
    font-size: 2.5em;
    font-variation-settings: "wght" 600;
	font-weight: 600;
    padding-bottom: 0.5em;
}

.button {
    border: 1px white solid;
    border-radius: 0.625em;
    vertical-align: middle;
    padding: 0.35em 0.625em;
}

.add-employee-icon {
    margin: 0, 0.5em;
}
</style>
