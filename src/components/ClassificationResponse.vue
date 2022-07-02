<template>
  <div class="m-3 p-3">
    <div>
      <h3>Clasificación de los datos</h3>
    </div>
    <div>
      <button class="btn btn-success" @click="goBackHome">Volver al inicio</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goBackHome() {
      this.$emit('nextStep', {componentName: 'UploadDataset'});
    }
  }
}
</script>