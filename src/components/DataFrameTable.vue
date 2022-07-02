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
      columnNames: [],
      rowData: []
    }
  },
  methods: {
    startClassification() {
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