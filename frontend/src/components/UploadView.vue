<template>
  <div id="uploadview">
    <el-autocomplete class="inline-input" v-model="value" :fetch-suggestions="querySearch" placeholder="请输入内容" :trigger-on-focus="false" @select="handleSelect"></el-autocomplete>
    <div>
      <el-upload class="upload-demo" ref="upload" action="/api/upload_specimen" :on-preview="handlePreview" :on-remove="handleRemove" :file-list="fileList" :auto-upload="false">
        <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
        <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
        <div slot="tip" class="el-upload__tip">只能上传fcs文件，且不超过10M</div>
      </el-upload>
    </div>
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
      var result = {}
      let data = {
        'name': queryString.toString()
      }
      this.$axios.post('/api/query_specimen_by_name', data)
        .then(response => (result = response['data']['data']))
        .catch(function (error) { console.log(error) })
      var options = new Array(result.length)
      for (let index = 0; index < result.length; index++) {
        options[index] = {
          value: result[index]['specimendir'],
          label: result[index]['name']
        }
      }
      this.options = options
      var results = queryString ? options.filter(this.createFilter(queryString)) : options
      cb(results)
    },
    createFilter (queryString) {
      return (options) => {
        return (options.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0)
      }
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
