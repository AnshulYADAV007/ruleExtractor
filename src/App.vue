<template>
  <div>
    <h1>Rule Extractor</h1>
    <br />
    <div>
      <form id="ruleForm" v-on:submit.prevent="onSubmit">
        <p>Provide the text for the Compliance</p>
        <textarea v-model="text" form="ruleForm" rows="20" cols="40" placeholder="Provide the text here"></textarea>
        <br />
        <input type="submit" value="Generate Rules">
      </form>
      <button @click="exportCSV">Download Rules</button>
    </div>
    <br />
  </div>
  <div id="table" v-html="table">
  </div>
</template>

<script lang="ts">
import axios from 'axios'
import '../node_modules/file-saver/src/FileSaver.js'

export default {
  data() {
    return {
      table: '',
      text: ""
    }
  },
  methods: {
    async onSubmit() {
      let data = {
        text: this.text
      }
      let response = await axios.post('http://127.0.0.1:5000/', data)
      this.table = response.data
    },
    exportCSV() {
      let csv = []
      const rows = document.querySelectorAll("table tr")
      for (const row of rows.values()) {
        const cells = row.querySelectorAll("td, th")
        csv.push(Array.from(cells).map(cell => '"' + cell.innerText + '"').join(","))
      }
      const csvFile = new Blob([csv.join("\n")], { type: 'text/csv; charset=utf-8' })
      saveAs(csvFile, "data.csv")
    }
  }
}
</script>

<style scoped>
label {
  margin: 0 1rem 0 1rem;
}
</style>
