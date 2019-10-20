<template>
  <div>
    <el-container>
      <el-aside width="200px">
        <el-menu :default-active="activeIndex" mode="vertical" @select="handleSelect">
          <el-menu-item index="1">送检信息</el-menu-item>
          <el-menu-item index="2">数据上传</el-menu-item>
          <el-menu-item index="3">数据分析</el-menu-item>
          <el-menu-item index="4">流式报表</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <component :is="currentView"></component>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import DatasetView from './DatasetView.vue'
import UploadView from './UploadView.vue'
import PatientInputView from './PatientInputView.vue'
import ReportGenView from './ReportGenView.vue'
export default {
  name: 'MainView',
  data () {
    return {
      activeIndex: '1',
      currentView: 'PatientInputView'
    }
  },
  components: {
    DatasetView,
    UploadView,
    PatientInputView,
    ReportGenView
  },
  methods: {
    handleSelect (key, keyPath) {
      switch (key) {
        case '1':
          this.currentView = 'PatientInputView'
          break
        case '2':
          this.currentView = 'UploadView'
          break
        case '3':
          this.currentView = 'DatasetView'
          break
        case '4':
          this.currentView = 'ReportGenView'
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
