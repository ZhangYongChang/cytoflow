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
    <div id="showview" style="width:1250px;float:left">
      <Experiment v-for="(value, key) in showtubor" :key="key" :item="value" :hisGates="hisGates" v-on:saveGate="saveGate">
      </Experiment>
    </div>
    <div id="showresult" style="float:right">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>细胞比例</span>
        </div>
        <div v-for="(value, key) in polygonGateStat" :key="key" class="text item">
          {{key}}:{{value}}%
        </div>
      </el-card>
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
      polygonGateStat: {},
      hisGates: {},
      result: ''
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
      this.$axios.post('/api/query_fcsfile_gate', { 'specimenid': this.specimenid, 'fcsfilename': newVal })
        .then(response => {
          if (response['data']['error_num'] !== 0) {
            this.$notify.error({ title: '错误', message: response['data']['msg'] })
          }
          this.hisGates = response['data']['data']
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
        this.$axios.post('api/cell_stat', { specimenid: this.specimenid, fcsfilename: this.tobo, polygongate: gates })
          .then(response => {
            if (response['data']['error_num'] !== 0) {
              this.$notify.error({ title: '错误', message: response['data']['msg'] })
            } else {
              this.polygonGateStat = response['data']['data']['stat']
              let result = {
                '淋巴细胞(绿色)': parseFloat(this.polygonGateStat['green'] * 100).toFixed(2),
                '前体B淋巴细胞(黄色)': parseFloat(this.polygonGateStat['yellow'] * 100).toFixed(2),
                '异常细胞群(红色)': parseFloat(this.polygonGateStat['red'] * 100).toFixed(2),
                '有核红区域细胞(紫色)': parseFloat(this.polygonGateStat['purple'] * 100).toFixed(2)
              }
              this.polygonGateStat = result
            }
          })
          .catch(error => {
            this.$notify.error({ title: '错误', message: error })
          })
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
.box-card {
  width: 380px;
}

text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: '';
}
.clearfix:after {
  clear: both;
}
</style>
