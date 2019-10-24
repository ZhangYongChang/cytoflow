<template>
  <div id="datasetview">
    <div>
      <el-row>
        <el-col :span="5">
          <el-select size="medium" v-model="specimenid" filterable remote reserve-keyword placeholder="请输入标本号" :remote-method="specimenSearch">
            <el-option v-for="item in specimenoptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-col>
        <el-col :span="5">
          <el-select v-model="tobo" placeholder="请选择试管">
            <el-option v-for="item in tobooptions" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="5">
          <el-button type="primary" @click="onSaveGate">提交</el-button>
        </el-col>
      </el-row>
    </div>
    <div id="showview">
      <Experiment v-for="(value, key) in showtubor" :key="key" :item="value" v-on:saveGate="saveGate">
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
      specimenlist: [],
      specimenoptions: [],
      specimenid: '',
      tobolist: [],
      tobooptions: [],
      tobo: '',
      showtubor: {},
      crossFlag: false,
      crossGate: {},
      polygonFlag: false,
      polygonGate: {},
      reslut: {}
    }
  },
  watch: {
    specimenid (newVal, oldVal) {
      this.$axios.post('/api/query_specimen_fcsfiles', { 'specimenid': newVal })
        .then(response => {
          if (response['data']['error_num'] !== 0) {
            this.$notify.error({ title: '错误', message: response['data']['msg'] })
          }
          this.tobolist = response['data']['data']['fcsfilenames']
        })
        .catch(error => {
          this.$notify.error({ title: '错误', message: error })
        })
    },
    tobolist (newVal, oldVal) {
      this.tobooptions = this.tobolist.map(item => {
        return { value: item, label: item }
      })
    },
    tobo (newVal, oldVal) {
      this.clearGates()
      this.showtubor = {}
      this.$axios.post('/api/query_specimen_fcsfile_data', { 'specimenid': this.specimenid, 'filename': newVal })
        .then(response => {
          if (response['data']['error_num'] !== 0) {
            this.$notify.error({ title: '错误', message: response['data']['msg'] })
          }
          this.refreshTubo(response['data']['data'])
        })
        .catch(error => {
          this.$notify.error({ title: '错误', message: error })
        })
    },
    specimenlist (newVal, oldVal) {
      this.specimenoptions = this.specimenlist.map(item => {
        return { value: item['specimenid'], label: item['specimenno'] }
      })
    }
  },
  methods: {
    getKey: function (tmptubor, xaxis, yaxis) {
      return tmptubor['specimenid'] + '/' + tmptubor['filename'] + '(' + xaxis + ',' + yaxis + ')'
    },
    clearGates: function () {
      this.crossFlag = false
      this.crossGate = {}
      this.polygonFlag = false
      this.polygonGate = {}
    },
    refreshTubo: function (orig) {
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
      var newtubor = {}
      for (var j = 0, len = showGroup.length; j < len; j++) {
        let groupitem = showGroup[j]
        var xaxis = groupitem[0]
        var yaxis = groupitem[1]
        let type = groupitem[2]
        let data = this.getAxisData(orig, xaxis, yaxis)
        let key = this.getKey(orig, xaxis, yaxis)
        newtubor[key] = {
          'key': key,
          'xaxis': xaxis,
          'yaxis': yaxis,
          'data': data,
          'type': type
        }
      }
      this.showtubor = newtubor
      orig = null
    },
    getAxisData: function (tmptubor, xaxis, yaxis) {
      var xarray = tmptubor[xaxis]
      var result = new Array(xarray.length)
      var yarray = tmptubor[yaxis]
      for (let index = 0; index < xarray.length; index++) {
        result[index] = [xarray[index], yarray[index]]
      }
      return result
    },
    specimenSearch: function (queryString) {
      this.$axios.post('/api/query_specimenid', { 'specimenno': queryString })
        .then(response => {
          if (response['data']['error_num'] !== 0) {
            this.$notify.error({ title: '错误', message: response['data']['msg'] })
          }
          this.specimenlist = response['data']['data']
        })
        .catch(error => {
          this.$notify.error({ title: '错误', message: error })
        })
    },
    onSaveGate: function () {
      if (this.crossFlag) {
        this.$axios.post('api/save_spceiment_fcsfile_gate', this.crossGate)
          .then(response => {
            if (response['data']['error_num'] !== 0) {
              this.$notify.error({ title: '错误', message: response['data']['msg'] })
            } else {
              this.$notify({ title: '成功', message: '保存十字门成功', type: 'success' })
              this.reslut = response['data']['data']
            }
          })
          .catch(error => {
            this.$notify.error({ title: '错误', message: error })
          })
      }

      if (this.polygonFlag) {
        this.$axios.post('api/save_spceiment_fcsfile_gate', this.polygonGate)
          .then(response => {
            if (response['data']['error_num'] !== 0) {
              this.$notify.error({ title: '错误', message: response['data']['msg'] })
            } else {
              this.$notify({ title: '成功', message: '保存多边形门成功', type: 'success' })
              this.reslut = response['data']['data']
            }
          })
          .catch(error => {
            this.$notify.error({ title: '错误', message: error })
          })
      }
    },
    saveGate: function (data) {
      if (data['gatetype'] === 1) {
        this.polygonFlag = true
        var gate = []
        var polygons = data['gates']['polygonGate']
        var colors = ['green', 'yellow', 'red', 'purple']
        polygons.forEach((polygon, index) => {
          gate.push({
            name: colors[index],
            data: polygon
          })
        })
        var gates = {
          xaxis: 'SSC-A',
          yaxis: 'PerCP-A',
          gate: gate
        }
        this.polygonGate = {
          specimenid: this.specimenid,
          fcsfilename: this.tobo,
          gatetype: 1,
          gates: gates
        }
      } else {
        if (this.crossFlag === false) {
          this.crossGate = {
            specimenid: this.specimenid,
            fcsfilename: this.tobo,
            gatetype: 0,
            gates: []
          }
          this.crossFlag = true
        }
        this.crossGate['gates'].push({
          xaxis: data['gates']['xaxis'],
          yaxis: data['gates']['yaxis'],
          point: data['gates']['crossGate']
        })
      }
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
