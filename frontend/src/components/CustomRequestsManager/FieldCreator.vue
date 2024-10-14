<template>
  <section class="field-creator">
    <h5>Добавить поле в тело запроса</h5>
    <label>
      Название поля:
      <input type="text" v-model="fieldName" />
      <span v-if="fieldNameError" class="text-error">
        Поле с названием имени переменной запроса не может быть пустым
      </span>
    </label>
    <br />
    <label>
      Значение:
      <input
        v-if="fieldType === 'text'"
        :name="fieldName"
        type="text"
        v-model="value"
      />
      <input
        v-if="fieldType === 'number'"
        :name="fieldName"
        type="number"
        v-model="value"
      />
      <textarea v-if="fieldType === 'json'" :name="fieldName" v-model="value" />
    </label>
    <br />
    <label>
      Тип данных:
      <select v-if="fieldType" v-model="fieldType">
        <option v-for="type in fieldsTypes" :key="type" :value="type">
          {{ type }}
        </option>
      </select>
    </label>
    <button class="button" @click="createField">Добавить поле</button>
  </section>
</template>

<style scoped>
label {
  margin: 7px 0;
}
.button {
  padding: 5px 10px;
  font-weight: bold;
  font-size: 1em;
  display: block;
  border: 1px black solid;
  border-radius: 5px;
  margin: 7px 0;
}
</style>

<script>
export default {
  props: ["fieldToEdit"],
  emits: ["create-field"],
  data() {
    return {
      value: this.fieldToEdit?.value ?? "",
      fieldName: this.fieldToEdit?.name ?? "",
      fieldType: this.fieldToEdit?.type ?? null,
      fieldNameError: false,
      fieldValueError: false,
      fieldsTypes: ["text", "number", "json"],
    };
  },

  created() {
    this.fieldType = this.fieldsTypes[0];
  },

  computed: {
    isFormValid() {
      return this.validateFields() && this.validateFieldName();
    },

    isNumberFieldValid() {
      if (this.fieldType === "number" && this.value === "") {
        return false;
      }
      return true;
    },

    isJSONFieldValid() {
      if (this.fieldType === "json") {
        try {
          JSON.parse(this.value);
          return true;
        } catch (e) {
          return false;
        }
      }
      return true;
    },
  },

  watch: {
    value(newValue, oldValue) {
      if (this.fieldType === "number" && newValue === "") {
        this.value = oldValue;
      }
    },
    fieldType() {
      this.setDefaultFieldValue();
    },

    fieldToEdit(newValue, oldValue) {
      if (newValue === oldValue) return;
      this.value = this.fieldToEdit?.value ?? "";
      this.fieldName = this.fieldToEdit?.name ?? "";
      this.fieldType = this.fieldToEdit?.type ?? null;
    },
  },

  methods: {
    validateFieldName() {
      if (this.fieldName === "") {
        this.fieldNameError = true;
        return false;
      }
      return true;
    },

    validateFields() {
      const isValid = this.isNumberFieldValid && this.isJSONFieldValid;
      this.fieldValueError = !isValid;

      return isValid;
    },

    createField() {
      if (!this.isFormValid) return;
      const newField = {
        value: this.value,
        name: this.fieldName,
        type: this.fieldType,
      };

      this.$emit("create-field", newField);
      this.setDefaultFieldValue();
      this.fieldName = "";
    },

    setDefaultFieldValue() {
      if (this.fieldType === "text") {
        this.value = "";
      }
      if (this.fieldType === "number") {
        this.value = 0;
      }
      if (this.fieldType === "json") {
        this.value = "{}";
      }
    },
  },
};
</script>
