<template>
  <div class="m-3 p-3">
    <div>
      <h3>Clasificación de los datos</h3>
    </div>
    <div class="my-5">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-3">
            Exactitud: {{ accuracy }}%
          </div>
          <div class="col-3">
            Precision: {{ precision }}%
          </div>
          <div class="col-3">
            Recall: {{ recall }}%
          </div>
        </div>
      </div>
    </div>
    <div class="mt-4">
      <button class="btn btn-success" @click="goBackHome">Volver al inicio</button>
    </div>
    <div class="mt-5">
      <b-table outlined responsive :items="matrix" :fields="fields" sticky-header="500px"></b-table>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    response: {
      type: Object
    }
  },
  data() {
    return {
      accuracy: 0.0,
      precision: 0.0,
      recall: 0.0,
      fields: [],
      matrix: []
    }
  },
  methods: {
    goBackHome() {
      this.$emit('nextStep', {componentName: 'UploadDataset'});
    }
  },
  created() {
    this.fields = JSON.parse(JSON.stringify(this.response.categories));

    for (let index = 0; index < this.fields.length; index++) {
      let row = {};
      row["Real \\ Predicted"] = this.fields[index];
      for (let j = 0; j < this.fields.length; j++) {
        row[this.fields[j]] = this.response.confusion_matrix[index][j];
      }
      this.matrix.push(row);
    }
    this.fields.unshift("Real \\ Predicted");

    this.accuracy = Math.round(this.response.classification_report.accuracy * 100)
    this.precision = Math.round(this.response.classification_report["macro avg"].precision * 100)
    this.recall = Math.round(this.response.classification_report["macro avg"].recall * 100)
  }
}
</script>