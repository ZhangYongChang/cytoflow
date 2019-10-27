<template>
  <div>
    <el-form ref="form" :model="form" label-width="100px" size="medium" hide-required-asterisk=false>
      <el-form-item label="送检人信息" label-width="100px">
        <el-row :gutter="30">
          <el-col :span="11">
            <el-form-item label="姓名">
              <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="年龄">
              <el-input v-model="form.age"></el-input>
            </el-form-item>
            <el-form-item label="性别">
              <el-select v-model="form.sex" placeholder="请选择性别" style="width:100px">
                <el-option label="男" value="Men"></el-option>
                <el-option label="女" value="Male"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form-item>
      <el-form-item label="标本信息" label-width="100px">
        <el-row :gutter="30">
          <el-col :span="11">
            <el-form-item label="标本编号">
              <el-input v-model="form.specimenno"></el-input>
            </el-form-item>
            <el-form-item label="医院">
              <el-input v-model="form.hospital"></el-input>
            </el-form-item>
            <el-form-item label="科室">
              <el-input v-model="form.department"></el-input>
            </el-form-item>
            <el-form-item label="床号">
              <el-input v-model="form.bedno"></el-input>
            </el-form-item>
            <el-form-item label="医生">
              <el-input v-model="form.doctor"></el-input>
            </el-form-item>
            <el-form-item label="病例号">
              <el-input v-model="form.caseno"></el-input>
            </el-form-item>
            <el-form-item label="标本类型">
              <el-select v-model="form.specimentype" placeholder="请选择标本类型">
                <el-option label="骨髓" value="GUSHUI"></el-option>
                <el-option label="尿液" value="NIAOYE"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="送检时间">
              <el-date-picker v-model="form.collecttime" type="date" placeholder="选择送检时间" format="yyyy 年 MM 月 dd 日" value-format="yyyy-MM-dd">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="接收时间">
              <el-date-picker v-model="form.recvtime" type="date" placeholder="选择接收时间" format="yyyy 年 MM 月 dd 日" value-format="yyyy-MM-dd">
              </el-date-picker>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onCommit">添加</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'SpecimenInputView',
  components: {
  },
  data () {
    return {
      form: {
        name: '',
        sex: '',
        age: 0,
        specimenno: '',
        hospital: '',
        department: '',
        bedno: '',
        doctor: '',
        specimentype: '',
        caseno: '',
        collecttime: '',
        recvtime: ''
      },
      result: {}
    }
  },
  methods: {
    onCommit () {
      this.$axios.post('/api/create_specimen', this.form)
        .then(response => {
          if (response['data']['error_num'] !== 0) {
            this.$notify.error({ title: '错误', message: response['data']['msg'] })
          } else {
            this.$notify({ title: '成功', message: '保存标本信息成功', type: 'success' })
            this.result = response['data']['data']
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
.el-form-item {
  margin-bottom: 20px;
  padding: 10px 0;
  &:last-child {
    margin-bottom: 0;
  }
}
</style>
