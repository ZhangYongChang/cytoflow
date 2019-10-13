<template>
  <div id="uploadview">
    <el-row>
      <el-col :span="12">
        <el-autocomplete class="inline-input" v-model="value" :fetch-suggestions="querySearch" placeholder="请输入内容" :trigger-on-focus="false" @select="handleSelect"></el-autocomplete>
      </el-col>
      <el-col :span="24">
        <el-upload class="upload-demo" ref="upload" action="/api/upload_specimen" :on-preview="handlePreview" :on-remove="handleRemove" :file-list="fileList" :auto-upload="false">
          <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
          <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
          <div slot="tip" class="el-upload__tip">只能上传fcs文件，且不超过10M</div>
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
      fileList: []

    }
  },
  methods: {
    querySearch (queryString, cb) {
      this.$axios.post('/api/query_specimen_by_name', {'name': queryString})
        .then(response => (this.options = response['data']['data']))
        .catch(function (error) { console.log(error) })
      console.log(this.options)
      var results = new Array(this.options.length)
      for (let index = 0; index < this.options.length; index++) {
        results[index] = this.options[index]['name']
      }
      cb(results)
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
  }
}
</script>

<style scoped>
</style>
