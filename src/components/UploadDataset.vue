<template>
  <div class="m-3 p-3">
    <div>
      <h3>
        Primero suba un dataset que ya se encuentre codificado en one-hot
      </h3>
    </div>
    <div>
      <input type="file" name="dataset" id="dataset" accept=".xls, .xlsx" @change="uploadDataset">
    </div>
    <div>
      <button class="btn btn-success" @click="changeComponent">Subir dataset</button>
    </div>
  </div>
</template>

<script>
import * as XLSX from 'xlsx';

export default {
  data() {
    return {
      dataset: undefined
    }
  },
  methods: {
    uploadDataset(event) {
      const datasetFile = event.target.files ? event.target.files[0] : null;
      if (datasetFile) {
        const reader = new FileReader();
        reader.readAsBinaryString(datasetFile);
        reader.onload = () => {
          const fileData = reader.result;
          const workbook = XLSX.read(fileData, {type: 'binary'});
          const firstSheetName = workbook.SheetNames[0];
          const sheet1 = workbook.Sheets[firstSheetName];
          this.dataset = XLSX.utils.sheet_to_json(sheet1);
        };
      }
    },
    changeComponent() {
      if (this.dataset) {
        this.$emit('nextStep', {componentName: 'DataFrameTable', dataset: this.dataset});
      }
    }
  }
}
</script>
