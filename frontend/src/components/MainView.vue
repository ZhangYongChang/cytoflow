<template>
  <div>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">数据分析</el-menu-item>
      <el-menu-item index="2">送检信息</el-menu-item>
      <el-menu-item index="3">报表</el-menu-item>
      <el-menu-item index="4">数据上传</el-menu-item>
    </el-menu>
    <div class="line"></div>
    <div>
      <component :is="currentView"></component>
    </div>
  </div>
</template>

<script>
import WelcomeView from './WelcomeView.vue'
import DatasetView from './DatasetView.vue'
import UploadView from './UploadView.vue'
import PatientInputView from './PatientInputView.vue'
import ReportGenView from './ReportGenView.vue'
export default {
  name: 'MainView',
  data () {
    return {
      currentView: 'WelcomeView'
    }
  },
  components: {
    WelcomeView,
    DatasetView,
    UploadView,
    PatientInputView,
    ReportGenView
  },
  methods: {
    handleSelect (key, keyPath) {
      switch (key) {
        case '1':
          this.currentView = 'DatasetView'
          break
        case '2':
          this.currentView = 'PatientInputView'
          break
        case '3':
          this.currentView = 'ReportGenView'
          break
        case '4':
          this.currentView = 'UploadView'
          break
        default:
          break
      }
    }
  }
}
</script>

<style scoped>

</style>
