<template>
  <PopupTypeMinimal
    v-if="modelValue"
    v-bind="$attrs"
    @close="$emit('update:modelValue', false)"
  >
    <div class="add-employee">
      <h2 class="popup-title">Добавить сотрудника</h2>
      <form class="employee-form">
        <div class="form-inputs">
          <input
            class="input"
            type="text"
            id="first_name"
            name="first_name"
            placeholder="Имя"
            v-model="first_name"
          />
          <input
            class="input"
            type="text"
            id="last_name"
            name="last_name"
            placeholder="Фамилия"
            v-model="last_name"
          />
          <input
            class="input"
            type="text"
            id="surname"
            name="surname"
            placeholder="Отчество"
            v-model="surname"
          />
          <input
            class="input"
            type="text"
            id="job_title"
            name="job_title"
            placeholder="Должность"
            v-model="job_id"
          />
          <input
            class="input"
            type="tel"
            id="phone"
            name="phone"
            placeholder="Телефон"
            v-model="phone"
          />
          <input
            class="input"
            type="email"
            id="email"
            name="email"
            placeholder="Почта"
            v-model="email"
          />
        </div>
        <input class="button" type="submit" value="Сохранить" />
      </form>
    </div>
  </PopupTypeMinimal>
</template>

<script>
import PopupTypeMinimal from "@/components/Popup/TypeMinimal.vue";

export default {
  props: ["jobs", "modelValue"],

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
.add-employee {
    display: flex;
    flex-direction: column;

    background-color: white;
    width: 26.25em;
    height: 36em;
    border-radius: 1em;

    padding: 3.75em 1.9em;
    text-align: center;
}

.employee-form {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
    height: 100%;

    align-items: center;
}

.form-inputs {
    display: flex;
    flex-direction: column;
    width: 100%;

    gap: 1em;
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
