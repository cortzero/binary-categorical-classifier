<template>
  <div id="app">
    <nav class="navbar navbar-dark color-blue justify-content-center">
      <div class="color-white-text pt-2">
        <h3>Clasificador de datos binarios y categóricos</h3>
      </div>
    </nav>
    <div>
      <component @nextStep='changeStep' :is="currentStep" v-bind="currentProps"></component>
    </div>
  </div>
</template>

<script>
import UploadDataset from './components/UploadDataset.vue';
import DataFrameTable from './components/DataFrameTable.vue';
import ClassificationResponse from './components/ClassificationResponse.vue';

export default {
  name: 'App',
  components: {
    UploadDataset,
    DataFrameTable,
    ClassificationResponse
  },
  data() {
    return {
      currentStep: 'UploadDataset',
      dataset: []
    }
  },
  methods: {
    changeStep(args) {
      this.dataset = args.dataset;
      this.currentStep = args.componentName;
    }
  },
  computed: {
    currentProps() {
      if (this.currentStep == 'DataFrameTable') {
        return {dataset: this.dataset};
      }
      return null;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
.color-blue {
  background-color: #00599C;
}
.color-white-text {
  color: #ffffff;
}
</style>
