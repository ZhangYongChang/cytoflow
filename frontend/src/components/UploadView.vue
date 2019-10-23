<template>
  <div id="uploadview">
    <el-row>
      <el-col :span="24">
        <el-select size="medium" v-model="value" filterable remote reserve-keyword placeholder="请输入标本号" :remote-method="querySearch">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <el-upload ref="upload" :data="submitParam" action="/api/upload_specimen_fcsfiles" :on-preview="handlePreview" :on-remove="handleRemove" :file-list="fileList" :auto-upload="false">
          <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
          <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
          <div slot="tip">只能上传fcs文件，且不超过10M</div>
        </el-upload>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'UploadView',
  data () {
    return {
      options: [],
      value: '',
      fileList: [],
      specimenList: [],
      submitParam: {}
    }
  },
  methods: {
    querySearch (queryString) {
      this.$axios.post('/api/query_specimenid', { 'specimenno': queryString })
        .then(response => {
          if (response['data']['error_num'] !== 0) {
            this.$notify.error({ title: '错误', message: response['data']['msg'] })
          } else {
            this.specimenList = response['data']['data']
          }
        })
        .catch(error => {
          this.$notify.error({ title: '错误', message: error })
        })
    },
    submitUpload () {
      this.$refs.upload.submit()
    },
    handleRemove (file, fileList) {
    },
    handlePreview (file) {
    },
    handleSelect (item) {
    }
  },
  watch: {
    specimenList: function (vaule) {
      this.options = this.specimenList.map(item => {
        return { value: item['specimenid'], label: item['specimenno'] }
      })
    },
    value: function (value) {
      this.submitParam = { 'specimenid': value }
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
