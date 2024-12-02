<template>
  <label
    for="files"
    ref="root"
    class="wrap input"
    :class="{ dragging: dragging }"
  >
    <div class="inner">
      <add-icon />
      <div class="description">
        для загрузки сертификатов перетащите<br />
        файлы или нажмите на область
      </div>
    </div>
  </label>
  <input
    id="files"
    type="file"
    style="display: none"
    multiple
    accept="image/png, image/gif, image/jpeg"
    @change="uploadFilesList($event)"
  />
</template>

<script>
import axios from "axios";
import AddIcon from "@/components/Icons/AddIcon.vue";

export default {
  emits: ["drop"],

  components: {
    AddIcon,
  },

  data() {
    return {
      files: [],
      dragging: false,
      dropArea: false,
      count: 0,
    };
  },

  watch: {
    dragging(val) {
      if (!this.dropArea) return;
      if (val) {
        this.dropArea.classList.add("DragNDrop_area");
      } else {
        this.dropArea.classList.remove("DragNDrop_area");
      }
    },
  },

  mounted() {
    this.dropArea = this.$refs.root;
    if (!this.dropArea) return;

    this.dropArea = this.dropArea.parentElement;
    this.dropArea.addEventListener("dragstart", this.dragstart, false);
    this.dropArea.addEventListener("dragenter", this.dragenter, false);
    this.dropArea.addEventListener("dragleave", this.dragleave, false);
    this.dropArea.addEventListener("dragover", this.dragover, false);
    this.dropArea.addEventListener("drop", this.drop, false);
  },

  methods: {
    dragenter(e) {
      let haveFiles = false;

      if (e.dataTransfer.types) {
        for (let i = 0; i < e.dataTransfer.types.length; i++) {
          if (e.dataTransfer.types[i] === "Files") {
            haveFiles = true;
          }
        }
      }

      if (!haveFiles) return;

      e.preventDefault();
      this.count++;
      this.dragging = true;
    },

    dragleave() {
      this.count--;
      if (this.count === 0) {
        this.dragging = false;
      }
    },

    dragstart(e) {
      console.log("dragstart");
      e.stopPropagation();
      this.count = 0;
    },

    dragover(e) {
      e.preventDefault();
      e.stopPropagation();
    },

    drop(e) {
      e.preventDefault();
      e.stopPropagation();
      this.dragging = false;
      this.count = 0;
      this.uploadFilesList(e.dataTransfer.files);
    },

    async uploadFile(file) {
      console.log("uploading file");
      console.log(file);

      const formData = new FormData();
      formData.append("image", file);

      const url = "/api/media/";
      return axios.post(url, formData);
    },

    uploadFilesList(files) {
      if (!files?.length) return;
      files = Array.from(files);

      for (const file of files) {
        const item = {
          type: "image",
          isLoading: true,
          media: {
            src: URL.createObjectURL(file),
            name: file.name,
          },
        };

        this.files.push(item);

        this.uploadFile(file)
          .then((uploadFileInfo) => {
            console.log(uploadFileInfo);
          })
          .catch(() => {
            this.uploadError = true;
          });

        if (this.uploadError) return;
      }
    },
  },
};
</script>

<style lang="sass" scoped>
.wrap {
	padding: 2rem;
    background-color: #CCDEF1;
	border: 2px dashed #6D747C;
}

.wrap.dragging {
    background-color: #CCDEF177;
}

.dragging {
	opacity: 1;
}

.inner {
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	color: var(--white);
	gap: .8rem;
}

.description {
    color: #6D747C;
}
</style>

<style lang="sass">

.DragNDrop_area * {
	pointer-events: none;
}
</style>
