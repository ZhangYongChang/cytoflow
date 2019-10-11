<template>
  <div id="uploadview">
    <el-autocomplete class="inline-input" v-model="value" :fetch-suggestions="querySearch" placeholder="请输入内容" :trigger-on-focus="false" @select="handleSelect"></el-autocomplete>
    <p>upload file</p>
  </div>
</template>

<script>
export default {
  name: 'UploadView',
  data () {
    return {
      options: [],
      value: ''
    }
  },
  methods: {
    querySearch (queryString, cb) {
      var result = {}
      let data = {
        'name': queryString.toString()
      }
      this.$axios.post('/api/query_all_specimen', data)
        .then(response => (result = response['data']))
        .catch(function (error) { console.log(error) })
      this.options = new Array(result.length)
      for (let index = 0; index < result.length; index++) {
        const element = result[index]
        this.options[index] = {
          value: element['specimenid'],
          label: element['name']}
      }

      var options = this.options
      var results = queryString ? options.filter(this.createFilter(queryString)) : options
      cb(results)
    },
    createFilter (queryString) {
      return (options) => {
        return (options.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0)
      }
    }
  },
  handleSelect (item) {
    console.log(item)
  }
}
</script>

<style scoped>
</style>
