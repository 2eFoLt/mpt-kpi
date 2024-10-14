<template>
  <div class="">
    <h2>Здесь ты можешь делать запросы на бекенд.</h2>
    <span class="warning">
      Если ты видешь это в проде, то срочно пиши @vasylyev
    </span>
    <h3>Параметры запроса на backend:</h3>
    <section class="request-actions">
      <div id="request-path-block" class="request-actions-block">
        <span>
          URL запроса:
          <a :href="requestURL" class="url-label">{{ requestURL }}</a>
        </span>
      </div>
      <div id="request-actions-block" class="request-actions-block">
        Отправить запрос:
        <button @click="sendRequest('GET')">GET</button>
        <button @click="sendRequest('POST')">POST</button>
        <button @click="sendRequest('PATCH')">PATCH</button>
      </div>
    </section>
    <FieldCreator @create-field="addField" :fieldToEdit="fieldToEdit" />
    <div id="request-body" class="request-data-block">
      <h5>Тело запроса:</h5>
      <FieldsViewer
        :fieldsList="fieldsList"
        @edit-field="setFieldToEdit"
        @delete-field="deleteField"
      />
    </div>
    <div v-if="responseFields" id="response-body" class="request-data-block">
      <h5>Тело Ответа:</h5>
      <FieldsViewer :fieldsList="responseFields" :readOnly="true" />
    </div>
  </div>
</template>

<style scoped>
.url-label {
  margin-left: 10px;
}
.warning {
  color: red;
}
.request-actions {
  display: flex;
  direction: column;
  gap: 10px;
}
</style>

<script>
import FieldCreator from "./FieldCreator.vue";
import FieldsViewer from "./FieldsViewer.vue";

import axios from "axios";

export default {
  components: {
    FieldCreator,
    FieldsViewer,
  },
  data() {
    return {
      fieldsList: [],
      responseData: null,
      fieldToEdit: null,
    };
  },

  mounted() {
    this.fieldsList =
      JSON.parse(localStorage.getItem("customRequestFieldsList")) ?? [];
  },

  computed: {
    requestBody() {
      const requestBody = {};
      this.fieldsList.map((field) => {
        requestBody[field.name] = field.value;
      });
      return JSON.parse(JSON.stringify(requestBody));
    },

    responseFields() {
      if (!this.responseData) return;

      return Object.entries(this.responseData)?.map((entrie) => {
        console.log(entrie[0]);
        return {
          name: entrie[0],
          value: entrie[1],
        };
      });
    },

    requestURL() {
      const url = new URL(document.URL);
      return `api${url.pathname}`;
    },
  },

  methods: {
    saveFieldsListToLocalStorage() {
      localStorage.setItem(
        "customRequestFieldsList",
        JSON.stringify(this.fieldsList)
      );
    },

    addField(fieldData) {
      const fieldIndex = this.fieldsList.findIndex(
        (field) => field.name === fieldData.name
      );

      if (~fieldIndex) {
        this.fieldsList.splice(fieldIndex, 1, fieldData);
      } else {
        this.fieldsList.push(fieldData);
      }

      this.saveFieldsListToLocalStorage();
    },

    deleteField(fieldName) {
      const fieldIndex = this.fieldsList.findIndex(
        (field) => field.name === fieldName
      );

      this.fieldsList.splice(fieldIndex, 1);
      this.saveFieldsListToLocalStorage();
    },

    sendRequest(method) {
      let promise = null;
      if (method === "GET") {
        promise = axios.get(this.requestURL);
      }
      if (method === "POST") {
        promise = axios.post(this.requestURL, this.requestBody);
      }
      if (method === "PATCH") {
        promise = axios.patch(this.requestURL, this.requestBody);
      }
      promise?.then((response) => {
        console.log(this.response);
        this.responseData = response.data;
      });
    },

    setFieldToEdit(field) {
      this.fieldToEdit = JSON.parse(JSON.stringify(field));
    },
  },
};
</script>
