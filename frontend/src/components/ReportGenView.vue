<template>
  <div>
    <div id="selectmenu">
      <p @click="onClickDatasetView">DatasetView</p>
      <ol>
        <li v-for="subdir in datasets['subdirs']"
            :key="subdir"
            @click="onClickExperiment(subdir)">
          {{ subdir }}
        </li>
      </ol>
      <div id="tuborlist">
        <ol>
          <li v-for="(value, index) in selectdataset['files']"
              :key="index"
              @click="onClickTubor(selectdataset['subdir'], value, index)">
            {{ selectdataset['subdir'] }}: {{ value }}
          </li>
        </ol>
      </div>
    </div>
    <div id="showview">
      <div>
        <p v-html="msg"></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReportGenView',
  data () {
    return {
      datasets: {},
      selectdataset: {},
      selecttubor: {},
      figview: {},
      msg: ''
    }
  },
  watch: {
    figview (newVal, oldVal) {
      this.msg = '<img src="data:image/png;base64,' + newVal['img'] + '"/>'
    }
  },
  methods: {
    onClickDatasetView () {
      this.$axios.post('/api/list_flowmetory')
        .then(response => (this.datasets = response['data']))
        .catch(function (error) { console.log(error) })
    },
    onClickExperiment (subdir) {
      let data = {
        'subdir': subdir
      }
      this.$axios.post('/api/list_directory_tubor', data)
        .then(response => (this.selectdataset = response['data']))
        .catch(function (error) { console.log(error) })
    },
    onClickTubor (key, value, index) {
      let data = {
        'filename': value,
        'subdir': key
      }

      this.$axios.post('/api/get_tubor_fig', data)
        .then(response => (this.figview = response['data']))
        .catch(function (error) { console.log(error) })
    }
  }
}
</script>

<style scoped>
</style>
