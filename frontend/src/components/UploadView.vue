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
        <el-upload ref="upload" :data="submitParam" action="/api/upload_specimen" :on-preview="handlePreview" :on-remove="handleRemove" :file-list="fileList" :auto-upload="false">
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
      value: 0,
      fileList: [],
      specimenList: [],
      submitParam: {}
    }
  },
  methods: {
    querySearch (queryString) {
      this.$axios.post('/api/query_specimenno', { 'specimenno': queryString })
        .then(response => (this.specimenList = response['data']['data']))
        .catch(function (error) { console.log(error) })
      console.log(this.specimenList)
      this.options = this.specimenList.map(item => {
        return { value: item['specimenid'], label: item['specimenno'] }
      })
      console.log(this.options)
    },
    submitUpload () {
      this.$refs.upload.submit()
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    handleSelect (item) {
      console.log(item)
    }
  },
  watch: {
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
