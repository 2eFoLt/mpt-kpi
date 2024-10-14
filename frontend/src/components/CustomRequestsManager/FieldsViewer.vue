<template>
  {
  <div
    class="field"
    v-for="field in fieldsList"
    :key="field.name"
    :class="{ selected: field.selected }"
  >
    <strong>{{ field.name }}:</strong>
    <span :class="{ text: field.type === 'text' }">{{ field.value }}</span>
    <template v-if="!readOnly">
      <span calss="edit" @click="editField(field)">Редактировать</span>
      <span calss="delete" @click="deleteField(field)">Удалить</span>
    </template>
  </div>
  }
</template>

<style scoped>
.field {
  padding: 10px 5px;
  span {
    margin: 0 10px;
  }
  .text {
    color: brown;
  }
  .number {
    color: blue;
  }
  .json {
    color: green;
  }
  .text::before {
    color: brown;
    content: '"';
  }
  .text::after {
    color: brown;
    content: '"';
  }
  .delete {
    color: red;
  }
}
</style>

<script>
export default {
  props: {
    fieldsList: {
      type: Array,
      required: true,
    },
    readOnly: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  emits: ["delete-field", "edit-field"],
  methods: {
    deleteField(field) {
      this.$emit("delete-field", field.name);
    },
    editField(field) {
      this.$emit("edit-field", field);
    },
  },
};
</script>
