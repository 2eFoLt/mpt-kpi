<template>
  <PopupTypeMinimal
    v-if="modelValue"
    v-bind="$attrs"
    @close="$emit('update:modelValue', false)"
  >
    <div class="add-cerificate">
      <h2 class="popup-title">Добавить сертификат</h2>
      <form class="cerificate-form">
        <select>
          <option>Название критерия</option>
        </select>
        <input
          type="file"
          id="certificate"
          name="file"
          accept="image/png, image/jpeg"
        />
        <input class="button" type="submit" value="Сохранить" />
      </form>
    </div>
  </PopupTypeMinimal>
</template>

<script>
import PopupTypeMinimal from "@/components/Popup/TypeMinimal.vue";

export default {
  props: ["modelValue"],

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
