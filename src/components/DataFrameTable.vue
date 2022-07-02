<template>
  <div class="m-3 p-3">
    <div>
      <h3>Dataframe</h3>
    </div>
    <div>
      <b-table outlined striped hover responsive :items="dataset"></b-table>
    </div>
    <div>
      <button class="btn btn-success" @click="startClassification">Clasificar</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    dataset: {
      type: Array
    }
  },
  data() {
    return {
      columnAttribute: [],
      datasetObject: {}
    }
  },
  methods: {
    startClassification() {
      Object.keys(this.dataset[0]).forEach((key) => {
        this.dataset.forEach((sample) => {
          this.columnAttribute.push(sample[key]);
        });
        this.datasetObject[key] = this.columnAttribute;
        this.columnAttribute = []
      });
      axios.post('http://127.0.0.1:5000/send', this.datasetObject).then(response => {
          const arrayString = JSON.stringify(response.data);
          const arrayObject = JSON.parse(arrayString);
          const arrayWithObjects = arrayObject.map(sample => {
            return JSON.parse(sample);
          });
          console.log(arrayWithObjects);
        }).finally(() => this.$emit('nextStep', {componentName: 'ClassificationResponse'}));
    }
  },
  created() {
    this.dataset.forEach((sample) => {
      const sampleString = JSON.stringify(sample);
      sample = JSON.parse(sampleString);
    });
  }
}
</script>