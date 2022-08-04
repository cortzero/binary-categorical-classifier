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
      <div class="my-1" v-for="result in results" :key="result.id">
        <div class="card">
          <div class="card-body">
            <div class="container mx-2 mw-100">
              <div class="row">
                <div class="col-11">
                  <h5 class="card-title text-start fw-bold">Ejemplo {{ result.id }}</h5>
                </div>
                <div class="col-1">
                  <font-awesome-icons 
                    v-if="result.expected_category == result.real_category" 
                    icon="circle-check" 
                    style="color:green">
                  </font-awesome-icons>
                  <font-awesome-icons
                    v-else
                    icon="circle-xmark" 
                    style="color:red">
                  </font-awesome-icons>
                </div>
              </div>
              <div class="row">
                <div class="text-start">Expected category: {{ result.expected_category }}</div>
              </div>
              <div class="row">
                <div class="text-start">Computed category: {{ result.real_category }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    results: {
      type: Array
    }
  },
  data() {
    return {
      hits: 0,
      mistakes: 0,
      totalExamples: 0,
      accuracy: 0.0
    }
  },
  methods: {
    goBackHome() {
      this.$emit('nextStep', {componentName: 'UploadDataset'});
    },

  },
  created() {
    this.results.forEach(result => {
      if(result.expected_category == result.real_category) {
        this.hits += 1;
      }
    });
    this.totalExamples = this.results.length;
    this.mistakes = this.totalExamples - this.hits;
    this.accuracy = Math.round((this.hits / this.totalExamples) * 100);
  }
}
</script>