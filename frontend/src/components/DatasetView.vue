<template>
  <div id="datasetview" style="width:1600px">
    <div id="selectmenu" style="height:20px;width:300px;float:left;">
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
    <div id="showview" style="height:20px;width:1300px;float:left;">
      <Experiment v-for="(value, key) in showtubor"
                  :key="key"
                  :item="value">
      </Experiment>
    </div>
  </div>
</template>

<script>
import Experiment from './Experiment'
export default {
  name: 'DatasetView',
  components: {
    Experiment
  },
  data () {
    return {
      datasets: {},
      selectdataset: {},
      selecttubor: {},
      showtubor: {}
    }
  },
  watch: {
    selecttubor (newVal, oldVal) {
      let showGroup = [
        ['FSC-A', 'SSC-A'],
        ['SSC-A', 'PerCP-A'],
        ['FITC-A', 'PE-A'],
        ['FITC-A', 'PE-Cy7-A'],
        ['APC-A', 'APC-Cy7-A'],
        ['FITC-A', 'APC-A'],
        ['PE-Cy7-A', 'APC-Cy7-A'],
        ['PE-A', 'PE-Cy7-A']
      ]

      function getAxisData (tmptubor, xaxis, yaxis) {
        var result = []
        var xarray = tmptubor[xaxis]
        var yarray = tmptubor[yaxis]
        for (let index = 0; index < xarray.length; index++) {
          result.push([xarray[index], yarray[index]])
        }
        return result
      }

      function getKey (tmptubor, xaxis, yaxis) {
        return tmptubor['subdir'] + '/' + tmptubor['filename'] + '(' + xaxis + ',' + yaxis + ')'
      }

      this.showtubor = {}
      for (var j = 0, len = showGroup.length; j < len; j++) {
        let groupitem = showGroup[j]
        var xaxis = groupitem[0]
        var yaxis = groupitem[1]
        let data = getAxisData(newVal, xaxis, yaxis)
        let key = getKey(newVal, xaxis, yaxis)
        this.showtubor[key] = {
          'key': key,
          'xaxis': xaxis,
          'yaxis': yaxis,
          'data': data
        }
      }
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

      this.$axios.post('/api/get_tubor', data)
        .then(response => (this.selecttubor = response['data']))
        .catch(function (error) { console.log(error) })
    }
  }
}
</script>

<style scoped>
.slide {
  position: fixed;
  width: 50%;
  height: 100%;
  float: left;
  overflow: auto;
}
</style>
