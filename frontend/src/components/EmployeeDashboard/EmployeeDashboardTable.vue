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
    <tr>
      <td class="employee-id">1</td>
      <td class="name">Антон</td>
      <td class="last-name">Миколяй</td>
      <td class="surname">Дмитриевич</td>
      <td class="job-name">Библиотекарь</td>
      <td class="phone">+7 (963) 650-42-93</td>
      <td class="email">pochta@mail.ru</td>
      <td class="controls">
        <svg
          class="icon-edit"
          width="25"
          height="26"
          viewBox="0 0 25 26"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M11.8968 2.7063H3.42152C2.77929 2.7063 2.16337 2.96142 1.70925 3.41555C1.25512 3.86967 1 4.48559 1 5.12782V22.0785C1 22.7207 1.25512 23.3366 1.70925 23.7907C2.16337 24.2449 2.77929 24.5 3.42152 24.5H20.3722C21.0144 24.5 21.6303 24.2449 22.0844 23.7907C22.5386 23.3366 22.7937 22.7207 22.7937 22.0785V13.6031"
            stroke="#5076B6"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M19.6154 2.25227C20.0971 1.7706 20.7504 1.5 21.4316 1.5C22.1128 1.5 22.766 1.7706 23.2477 2.25227C23.7294 2.73394 24 3.38723 24 4.06841C24 4.7496 23.7294 5.40288 23.2477 5.88455L12.3351 16.7984C12.0476 17.0856 11.6925 17.2959 11.3024 17.4098L7.82384 18.4268C7.71965 18.4572 7.60922 18.459 7.50409 18.4321C7.39896 18.4052 7.303 18.3505 7.22626 18.2737C7.14952 18.197 7.09482 18.101 7.06789 17.9959C7.04096 17.8908 7.04278 17.7803 7.07317 17.6762L8.0902 14.1976C8.20465 13.8078 8.41534 13.4531 8.70285 13.1661L19.6154 2.25227Z"
            stroke="#5076B6"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
        <svg
          class="icon-delete"
          width="29"
          height="28"
          viewBox="0 0 29 28"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M3 2.5L26 25.5M3 25.5L26 2.5"
            stroke="#2B4D85"
            stroke-width="4.16667"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </td>
    </tr>
  </table>
</template>
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
