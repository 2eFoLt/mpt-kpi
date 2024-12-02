<template>
  <popup-type-minimal
    v-if="modelValue"
    v-bind="$attrs"
    @close="$emit('update:modelValue', false)"
  >
    <div class="add-cerificate">
      <h2 class="popup-title">Добавить сертификат</h2>
      <form class="cerificate-form">
        <div class="form-inputs">
          <select class="input">
            <option>Название критерия</option>
          </select>
          <many-file-input />
          <!--<input
            class="input file-input"
            type="file"
            id="certificate"
            name="file"
            accept="image/png, image/jpeg"
          />
          -->
        </div>
        <input class="button" type="submit" value="Сохранить" />
      </form>
    </div>
  </popup-type-minimal>
</template>

<script>
import PopupTypeMinimal from "@/components/Popup/TypeMinimal.vue";
import ManyFileInput from "@/components/Utils/ManyFileInput.vue";

export default {
  props: ["modelValue"],

  components: {
    PopupTypeMinimal,
    ManyFileInput,
  },
};
</script>

<style lang="sass" scoped>
.add-cerificate {
    display: flex;
    flex-direction: column;

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
