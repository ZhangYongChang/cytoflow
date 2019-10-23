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
      result: '',
      openLink: ''
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
    },
    openLink (newVal, oldVal) {
      window.open('/static/' + newVal['filename'], '_blank')
    }
  },
  mounted () {
    this.$axios.post('/api/query_specimen_suggest')
      .then(response => {
        if (response['data']['error_num'] !== 0) {
          this.$notify.error({ title: '错误', message: response['data']['msg'] })
        } else {
          this.suggestSpecimen = response['data']['data']
        }
      })
      .catch(error => {
        this.$notify.error({ title: '错误', message: error })
      })
  },
  methods: {
    handleGen (index, row) {
      this.$axios.post('/api/gen_report', { specimenid: this.tableData[index].specimenid })
        .then(response => {
          if (response['data']['error_num'] !== 0) {
            this.$notify.error({ title: '错误', message: response['data']['msg'] })
          } else {
            this.$notify({ title: '成功', message: '生成报表成功', type: 'success' })
            this.result = response['data']['data']
          }
        })
        .catch(error => {
          this.$notify.error({ title: '错误', message: error })
        })
    },
    handleDownload (index, row) {
      this.$axios.post('/api/query_report', { specimenid: this.tableData[index].specimenid })
        .then(response => {
          if (response['data']['error_num'] !== 0) {
            this.$notify.error({ title: '错误', message: response['data']['msg'] })
          } else {
            this.openLink = response['data']['data']
          }
        })
        .catch(error => {
          this.$notify.error({ title: '错误', message: error })
        })
    }
  }
}
</script>

<style scoped>
</style>
