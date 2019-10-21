<template>
  <div id="datasetview">
    <el-row>
      <el-col :span="24">
        <el-select size="medium" v-model="specimenid" filterable remote reserve-keyword placeholder="请输入标本号" :remote-method="specimenSearch">
          <el-option v-for="item in specimenoptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <el-select v-model="tobo" placeholder="请选择试管">
          <el-option v-for="item in tobooptions" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
      </el-col>
    </el-row>
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
      specimenlist: [],
      specimenoptions: [],
      specimenid: '',
      tobolist: [],
      tobooptions: [],
      tobo: '',
      orig_tobo: [],
      showtubor: {},
      selectfig: {}
    }
  },
  watch: {
    specimenid (newVal, oldVal) {
      this.$axios.post('/api/query_specimen_fcsfiles', { 'specimenid': newVal })
        .then(response => (this.tobolist = response['data']['data']['fcsfilenames']))
        .catch(function (error) { console.log(error) })
    },
    tobolist (newVal, oldVal) {
      this.tobooptions = this.tobolist.map(item => {
        return { value: item, label: item }
      })
    },
    tobo (newVal, oldVal) {
      console.log(newVal)
      this.$axios.post('/api/query_specimen_fcsfile_data', { 'specimenid': this.specimenid, 'filename': newVal })
        .then(response => (this.orig_tobo = response['data']['data']))
        .catch(function (error) { console.log(error) })
    },
    orig_tobo (newVal, oldVal) {
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
        return tmptubor['specimenid'] + '/' + tmptubor['filename'] + '(' + xaxis + ',' + yaxis + ')'
      }

      this.showtubor = {}
      for (var j = 0, len = showGroup.length; j < len; j++) {
        let groupitem = showGroup[j]
        var xaxis = groupitem[0]
        var yaxis = groupitem[1]
        let type = groupitem[2]
        let data = getAxisData(this.orig_tobo, xaxis, yaxis)
        let key = getKey(this.orig_tobo, xaxis, yaxis)
        this.showtubor[key] = {
          'key': key,
          'xaxis': xaxis,
          'yaxis': yaxis,
          'data': data,
          'type': type
        }
      }
    },
    specimenlist (newVal, oldVal) {
      this.specimenoptions = this.specimenlist.map(item => {
        return { value: item['specimenid'], label: item['specimenno'] }
      })
    }
  },
  methods: {
    specimenSearch (queryString) {
      this.$axios.post('/api/query_specimenid', { 'specimenno': queryString })
        .then(response => (this.specimenlist = response['data']['data']))
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
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
</style>
