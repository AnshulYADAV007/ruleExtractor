<template>
  <div>
    <h1>Rule Extractor</h1>
    <br />
    <form id="ruleForm" v-on:submit.prevent="onSubmit">
      <p>Provide the text for the Compliance</p>
      <textarea v-model="text" form="ruleForm" rows="20" cols="40" placeholder="Provide the text here"></textarea>
      <br />
      <input type="submit" value="Generate Rules">
      <button style="margin: 1rem;" @click.prevent="exportCSV">Download Rules</button>
      <button @click.prevent="clear">Clear</button>
      <p v-if="loading" class="loader">
      </p>
    </form>
    <br />
  </div>
  <div id="table" v-html="table">
  </div>
</template>

<script lang="ts">
import axios from 'axios'
import FileSaver from 'file-saver'

export default {
  data() {
    return {
      table: '',
      text: "",
      loading: false
    }
  },
  methods: {
    clear() {
      this.table = ""
      this.text = ""
      this.loading = false
    },
    async onSubmit() {
      let data = {
        text: this.text
      }
      this.loading = true
      this.table = ""
      try {
        let response = await axios.post('http://127.0.0.1:5000/', data)
        this.loading = false
        this.table = response.data
      } catch (e) {
        this.loading = false
        this.table = ""
        console.error(e)
      }
    },
    exportCSV() {
      let csv = []
      const rows = document.querySelectorAll("table tr")
      for (const row of rows.values()) {
        const cells = row.querySelectorAll("td, th")
        csv.push(Array.from(cells).map(cell => '"' + (cell as HTMLElement).innerText + '"').join(","))
      }
      const csvFile = new Blob([csv.join("\n")], { type: 'text/csv; charset=utf-8' })
      FileSaver.saveAs(csvFile, "data.csv")
    }
  }
}
</script>

<style scoped>
label {
  margin: 0 1rem 0 1rem;
}

.loader {
  border: 4px solid #f3f3f3;
  /* Light grey */
  border-top: 4px solid #3498db;
  /* Blue */
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
