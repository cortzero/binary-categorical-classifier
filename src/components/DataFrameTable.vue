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
      this.$emit('nextStep', {componentName: 'ClassificationResponse'});
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