<template>
  <PopupTypeMinimal
    v-if="modelValue"
    v-bind="$attrs"
    @close="$emit('update:modelValue', false)"
  >
    <div class="add-employee">
      <h2 class="popup-title">Добавить сотрудника</h2>
      <form class="employee-form">
        <input
          type="text"
          id="first_name"
          name="first_name"
          placeholder="Имя"
          v-model="first_name"
        />
        <input
          type="text"
          id="last_name"
          name="last_name"
          placeholder="Фамилия"
          v-model="last_name"
        />
        <input
          type="text"
          id="surname"
          name="surname"
          placeholder="Отчество"
          v-model="surname"
        />
        <input
          type="text"
          id="job_title"
          name="job_title"
          placeholder="Должность"
          v-model="job_id"
        />
        <input
          type="tel"
          id="phone"
          name="phone"
          placeholder="Телефон"
          v-model="phone"
        />
        <input
          type="email"
          id="email"
          name="email"
          placeholder="Почта"
          v-model="email"
        />
        <input class="button" type="submit" value="Сохранить" />
      </form>
    </div>
  </PopupTypeMinimal>
</template>

<script>
import PopupTypeMinimal from "@/components/Popup/TypeMinimal.vue";

export default {
  props: ["jobs"],

  data() {
    return {
      first_name: "",
      last_name: "",
      surname: "",
      email: "",
      job_id: "",
      phone: "",
    };
  },

  created() {
    console.log(this.modelValue);
  },

  components: {
    PopupTypeMinimal,
  },
};
</script>

<style lang="sass" scoped>
.add-cerificate {
    background-color: white;
    width: 46em;
    height: 33.5em;
    border-radius: 1em;

    padding: 3.75em 1.9em;
    text-align: center;
}

.cerificate-form {
    display: flex;
    flex-direction: column;
}

.button {
    width: fit-content;
	color: white;
    padding: 0.5em 1.8em;
	font-size: 1em;
    font-variation-settings: "wght" 600;
	font-weight: 600;
	background-color: #5076b6;
	border-radius: 0.4em;
	border-style: hidden;
}

.popup-title {
	color: #5076b6;
	font-size: 1.6em;
	line-height: 2em;
    font-variation-settings: "wght" 600;
	font-weight: 600;
    padding-bottom: 1.8em;
}
</style>
