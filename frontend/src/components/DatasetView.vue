<template>
  <div id="datasetview">
    <div id="selectmenu">
      <p @click="onClickDatasetView">DatasetView</p>
      <ol>
        <li v-for="subdir in datasets['data']" :key="subdir" @click="onClickExperiment(subdir)">
          {{ subdir }}
        </li>
      </ol>
      <div id="tuborlist">
        <ol>
          <li v-for="(value, index) in selectdataset['fcsfilenames']" :key="index" @click="onClickTubor(selectdataset['querysubdir'], value, index)">
            {{ selectdataset['querysubdir'] }}: {{ value }}
          </li>
        </ol>
      </div>
    </div>
    <div id="showview">
      <div>
        <Experiment v-for="(value, key) in showtubor" :key="key" :item="value" v-on:figSelect="figSelect" v-on:figDel="figDel">
        </Experiment>
      </div>
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
      showtubor: {},
      selectfig: {}
    }
  },
  watch: {
    selecttubor (newVal, oldVal) {
      let showGroup = [
        ['FSC-A', 'SSC-A', 'linearlinear'],
        ['SSC-A', 'PerCP-A', 'linearlog'],
        ['FITC-A', 'PE-A', 'loglog'],
        ['FITC-A', 'PE-Cy7-A', 'loglog'],
        ['APC-A', 'APC-Cy7-A', 'loglog'],
        ['FITC-A', 'APC-A', 'loglog'],
        ['PE-Cy7-A', 'APC-Cy7-A', 'loglog'],
        ['PE-A', 'PE-Cy7-A', 'loglog']
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
        return tmptubor['querysubdir'] + '/' + tmptubor['filename'] + '(' + xaxis + ',' + yaxis + ')'
      }

      this.showtubor = {}
      for (var j = 0, len = showGroup.length; j < len; j++) {
        let groupitem = showGroup[j]
        var xaxis = groupitem[0]
        var yaxis = groupitem[1]
        let type = groupitem[2]
        let data = getAxisData(newVal, xaxis, yaxis)
        let key = getKey(newVal, xaxis, yaxis)
        this.showtubor[key] = {
          'key': key,
          'xaxis': xaxis,
          'yaxis': yaxis,
          'data': data,
          'type': type
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
        'querysubdir': subdir
      }
      this.$axios.post('/api/list_directory_tubor', data)
        .then(response => (this.selectdataset = response['data']['data']))
        .catch(function (error) { console.log(error) })
    },
    onClickTubor (key, value, index) {
      let data = {
        'filename': value,
        'querysubdir': key
      }

      this.$axios.post('/api/get_tubor', data)
        .then(response => (this.selecttubor = response['data']['data']))
        .catch(function (error) { console.log(error) })
    },
    figSelect (data) {
      this.selectfig[data['viewid']] = data
      console.log(this.selectfig)
    },
    figDel (data) {
      delete this.selectfig.data['viewid']
      console.log(this.selectfig)
    }
  }
}
</script>

<style scoped>
</style>
