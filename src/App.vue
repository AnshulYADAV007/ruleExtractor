<template>
  <div>
    <h1>Rule Extractor</h1>
    <br />
    <div>
      <form id="ruleForm" v-on:submit.prevent="onSubmit">
        <p>Choose your role:</p>
        <input type="radio" v-model="role" id="droolDev" name="role" value="droolDev">
        <label for="droolDev">Drool Developer</label><br>
        <input type="radio" v-model="role" id="analyst" name="role" value="analyst">
        <label for="analyst">Service Compliance Analyst</label><br>
        <p>What all columns do you want in the table?</p>
        <input type="checkbox" :checked="isColumn1" v-model="columns" id="titleColumn" name="columns" value="name">
        <label for="titleColumn">Name</label><br>
        <input type="checkbox" :checked="isColumn2" v-model="columns" id="descriptionColumn" name="columns" value="rule">
        <label for="descriptionColumn">Rule</label><br>
        <input type="checkbox" :checked="isColumn3" v-model="columns" id="dueDate" name="columns"
          value="due date by which the action must be completed.">
        <label for="dueDate">Due Date</label>
        <p>Provide the text for the Compliance</p>
        <textarea v-model="text" form="ruleForm" rows="20" cols="40" placeholder="Provide the text here"></textarea>
        <br />
        <input type="submit" value="Generate Rules">
      </form>
    </div>
    <br />
  </div>
  <div v-html="table">
  </div>
</template>

<script lang="ts">
import axios from 'axios'

export default {
  data() {
    return {
      table: '',
      role: "",
      columns: [],
      text: "",
      isColumn1: true,
      isColumn2: true,
      isColumn3: true
    }
  },
  methods: {
    async onSubmit() {
      let data = {
        role: this.role,
        columns: this.columns,
        text: this.text
      }
      let response = await axios.post('http://127.0.0.1:5000/', data)
      this.table = response.data
    }
  }
}
</script>

<style scoped>
label {
  margin: 0 1rem 0 1rem;
}
</style>
