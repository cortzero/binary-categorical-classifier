<template>
  <div class="m-3 p-3">
    <div>
      <h3>Clasificación de los datos</h3>
    </div>
    <div class="my-5">
      <div class="container">
        <div class="row">
          <div class="col-3">
            Aciertos: {{ hits }}
          </div>
          <div class="col-3">
            Errores: {{ mistakes }}
          </div>
          <div class="col-3">
            Total de ejemplos: {{ totalExamples }}
          </div>
          <div class="col-3">
            Precisión: {{ accuracy }}%
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
      hits: 0,
      mistakes: 0,
      totalExamples: 0,
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
    },

  },
  created() {
    /*this.results.forEach(result => {
      if(result.expected_category == result.real_category) {
        this.hits += 1;
      }
    });
    this.totalExamples = this.results.length;
    this.mistakes = this.totalExamples - this.hits;
    this.accuracy = Math.round((this.hits / this.totalExamples) * 100);*/
    console.log(this.response.categories);
    console.log(this.response.confusion_matrix);

    this.fields = JSON.parse(JSON.stringify(this.response.categories));

    for (let index = 0; index < this.fields.length; index++) {
      let row = {};
      row[" "] = this.fields[index];
      for (let j = 0; j < this.fields.length; j++) {
        row[this.fields[j]] = this.response.confusion_matrix[index][j];
      }
      this.matrix.push(row);
    }

    this.fields.unshift(" ");

    console.log(this.fields);
    console.log(this.matrix);


    let tp = 0;
    let sum = 0;
    for (let i = 0; i < this.response.categories.length; i++) {
      for (let j = 0; j < this.response.categories.length; j++) {
        if (i == j) {
          tp += this.response.confusion_matrix[i][j];
        }
        sum += this.response.confusion_matrix[i][j];
      }
    }
    this.accuracy = Math.round((tp / sum) * 100);
  }
}
</script>