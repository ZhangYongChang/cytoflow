<template>
  <div>
    <div id="table">
      <el-table :data="tableData.filter(data => !search || data.specimenno.toLowerCase().includes(search.toLowerCase()))" style="width: 100%">
        <el-table-column label="标本编号" prop="specimenno">
        </el-table-column>
        <el-table-column label="ID" prop="specimenid">
        </el-table-column>
        <el-table-column align="right">
          <template slot="header" slot-scope="scope">
            <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
          </template>
          <template slot-scope="scope">
            <el-button size="mini" @click="handleGen(scope.$index, scope.row)">生成</el-button>
            <el-button size="mini" @click="handleDownload(scope.$index, scope.row)">下载</el-button>
          </template>
        </el-table-column>
      </el-table>
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
      suggestSpecimen: [],
      tableData: [],
      search: '',
      figview: {},
      msg: '',
      result: ''
    }
  },
  watch: {
    figview (newVal, oldVal) {
      this.msg = '<img src="data:image/png;base64,' + newVal['img'] + '"/>'
    },
    suggestSpecimen (newVal, oldVal) {
      this.tableData = newVal.map(item => {
        return { specimenno: item['specimenno'], specimenid: item['specimenid'] }
      })
    }
  },
  mounted () {
    this.$axios.post('/api/query_specimen_suggest')
      .then(response => (this.suggestSpecimen = response['data']['data']))
      .catch(function (error) { console.log(error) })
  },
  methods: {
    handleGen (index, row) {
      this.$axios.post('/api/gen_report', { specimenid: this.tableData[index].specimenid })
        .then(response => (this.result = response['data']['data']))
        .catch(function (error) { console.log(error) })
    },
    handleDownload (index, row) {
    }
  }
}
</script>

<style scoped>
</style>
