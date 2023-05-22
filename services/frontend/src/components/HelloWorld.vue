<template>
  <div>
    <h3>Note fo example</h3>
    <p>{{ msg }}</p>
  </div>

  <div>
    <input class="btn btn-dark" type="file" @change="uploadFile" ref="file">
    <button class="btn btn-success" @click="submitFile">Upload File</button>
  </div>

  <strong>
    <lable>File store ID is: </lable>

    <li v-for="[filename, ids] of files_id" :key="ids.id">
      <a v-on:click="download(ids)">{{filename}}</a>
    </li>
  </strong>



</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue';
export default defineComponent({
  name: 'PingPong',
  data() {
    return {
      msg: '',
      files_id: new Map(),
      url_d: "http://localhost:8000/docs/receive/",
      TOKEN: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjoxNzI2NDk4MjQ1fQ.kwT_C69A52K8kM2amluS6qWDOuKMOjqtRrKoNIRwPbg"
    };
  },
  methods: {
    getMessage() {
      axios.get('/')
          .then((res) => {
            this.msg = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    uploadFile() {
      this.filick = this.$refs.file.files[0];
    },
    submitFile() {
      const formData = new FormData();
      formData.append('file', this.filick);
      const headers = {'Content-Type': 'multipart/form-data', 'Authorization': this.TOKEN};
      axios.post('http://localhost:8000/docs/uploadfile', formData, {headers}).then((res) => {
        res.data.files;
        res.status;
        this.files_id.set(res.data["filename"], res.data["ID_file"])
        //this.files_id.push(res.data["ID_file"])
      })
    },
    force_download(res, title) {
      const url = window.URL.createObjectURL(new Blob([res.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', title)
      document.body.appendChild(link)
      link.click()
    },
    download(idishka) {
      const formData = new FormData();
      formData.append('file', this.filick);
      const headers = {'Authorization': this.TOKEN, "Access-Control-Expose-Headers": "Content-Disposition"};
      axios.get(this.url_d + idishka, {headers, responseType: 'blob'}).then((res) => {
        //let filename = res.headers['Content-Disposition'].split('filename=')[1].split('.')[0];
        this.force_download(res, "file")
      })
    },
  },
  created() {
    this.getMessage()
  }
})
</script>

