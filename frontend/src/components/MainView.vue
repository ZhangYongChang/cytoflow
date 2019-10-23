<template>
  <div>
    <el-container>
      <el-container>
        <el-aside width="200px">
          <el-menu :default-active="activeIndex" mode="vertical" @select="handleSelect">
            <el-menu-item index="1">送检信息</el-menu-item>
            <el-menu-item index="2">数据上传</el-menu-item>
            <el-menu-item index="3">数据分析</el-menu-item>
            <el-menu-item index="4">流式报表</el-menu-item>
            <el-menu-item index="5">标本预览</el-menu-item>
          </el-menu>
        </el-aside>
        <el-container>
          <el-main>
            <component :is="currentView"></component>
          </el-main>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import DatasetView from './DatasetView.vue'
import UploadView from './UploadView.vue'
import SpecimenInputView from './SpecimenInputView.vue'
import ReportGenView from './ReportGenView.vue'
import SpecimenPreview from './SpecimenPreview.vue'
export default {
  name: 'MainView',
  data () {
    return {
      activeIndex: '1',
      currentView: 'SpecimenInputView'
    }
  },
  components: {
    DatasetView,
    UploadView,
    SpecimenInputView,
    ReportGenView,
    SpecimenPreview
  },
  methods: {
    handleSelect (key, keyPath) {
      switch (key) {
        case '1':
          this.currentView = 'SpecimenInputView'
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
        case '5':
          this.currentView = 'SpecimenPreview'
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
