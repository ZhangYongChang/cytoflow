<template>
  <div>
    <el-form ref="form" :model="form" label-width="80px" size="medium" hide-required-asterisk=false>
      <el-form-item label="送检人信息">
        <el-row :gutter="20">
          <el-col :span="11">
            <el-form-item label="姓名">
              <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="性别">
              <el-select v-model="form.sex" placeholder="请选择性别">
                <el-option label="男" value="Men"></el-option>
                <el-option label="女" value="Male"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="年龄">
              <el-input v-model="form.age"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form-item>
      <el-form-item label="标本信息">
        <el-row :gutter="20">
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
            <el-form-item>
              <el-input v-model="form.caseno"></el-input>
            </el-form-item>
            <el-form-item label="标本类型">
              <el-select v-model="form.specimentype" placeholder="请选择标本类型">
                <el-option label="骨髓" value="GUSHUI"></el-option>
                <el-option label="尿液" value="NIAOYE"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="送检时间">
              <el-date-picker v-model="form.collecttime" type="datetime" placeholder="选择送检时间">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="接收时间">
              <el-date-picker v-model="form.recvtime" type="datetime" placeholder="选择接收时间">
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
  name: 'PatientInputView',
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
      this.$axios.post('/api/create_patient', this.form)
        .then(response => (this.result = response['data']))
        .catch(function (error) { console.log(error) })
    }
  }
}
</script>

<style scoped>
</style>
