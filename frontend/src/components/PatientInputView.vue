<template>
  <div>
    <form
      action="/api/create_patient"
      method="POST"
      enctype="application/x-www-form-urlencoded"
    >
      <vue-form-generator
        :schema="schema"
        :model="model"
        :options="formOptions"
      ></vue-form-generator>
      <input
        @click="onCommit"
        type="submit"
        value="提交"
      >
    </form>
  </div>
</template>

<script>
import VueFormGenerator from 'vue-form-generator'
import 'vue-form-generator/dist/vfg.css'

export default {
  name: 'PatientInputView',
  components: {
    'vue-form-generator': VueFormGenerator.component
  },
  data () {
    return {
      model: {
        name: '张三',
        sex: '男',
        age: 30,
        specimenno: 'AAAA01',
        hospital: '湖北省人民医院',
        department: '00A',
        bedno: '010',
        doctor: '李四',
        specimentype: '骨髓',
        caseno: '01010A',
        collecttime: '2014-07-01',
        recvtime: '2014-07-02'
      },
      result: {},
      schema: {
        groups: [
          {
            legend: '基本信息',
            fields: [
              {
                type: 'input',
                inputType: 'text',
                label: 'Name',
                model: 'name',
                readonly: false,
                featured: true,
                required: true,
                disabled: false,
                placeholder: '姓名',
                validator: VueFormGenerator.validators.string
              },
              {
                type: 'select',
                label: 'Sex',
                model: 'sex',
                multi: false,
                required: true,
                multiSelect: false,
                values: ['男', '女', ' ']
              },
              {
                type: 'input',
                inputType: 'number',
                label: 'Age',
                model: 'age',
                min: 0,
                validator: VueFormGenerator.validators.number
              }
            ]
          },
          {
            legend: '标本信息',
            fields: [
              {
                type: 'input',
                inputType: 'text',
                label: '标本编号',
                model: 'specimenno',
                readonly: false,
                featured: true,
                required: true,
                disabled: false,
                placeholder: '标本编号',
                validator: VueFormGenerator.validators.string
              },
              {
                type: 'input',
                inputType: 'text',
                label: '送检医院',
                model: 'hospital',
                readonly: false,
                featured: true,
                required: true,
                disabled: false,
                placeholder: '送检医院',
                validator: VueFormGenerator.validators.string
              },
              {
                type: 'input',
                inputType: 'text',
                label: '科室',
                model: 'department',
                readonly: false,
                featured: true,
                required: true,
                disabled: false,
                placeholder: '科室',
                validator: VueFormGenerator.validators.string
              },
              {
                type: 'input',
                inputType: 'text',
                label: '床号',
                model: 'bedno',
                readonly: false,
                featured: true,
                required: true,
                disabled: false,
                placeholder: '床号',
                validator: VueFormGenerator.validators.string
              },
              {
                type: 'input',
                inputType: 'text',
                label: '送检医生',
                model: 'doctor',
                readonly: false,
                featured: true,
                required: true,
                disabled: false,
                placeholder: '送检医生',
                validator: VueFormGenerator.validators.string
              },
              {
                type: 'select',
                label: '标本类型',
                model: 'specimentype',
                multi: false,
                required: true,
                multiSelect: false,
                values: ['骨髓', '血液', '尿液']
              },
              {
                type: 'input',
                inputType: 'text',
                label: '病例号',
                model: 'caseno',
                readonly: false,
                featured: true,
                required: true,
                disabled: false,
                placeholder: '病例号',
                validator: VueFormGenerator.validators.string
              },
              {
                type: 'dateTimePicker',
                label: '采集时间',
                model: 'collecttime',
                required: true,
                placeholder: '采集时间'
              },
              {
                type: 'dateTimePicker',
                label: '接收时间',
                model: 'recvtime',
                required: true,
                placeholder: '接收时间'
              }
            ]
          }
        ]
      },
      formOptions: {
        validateAfterLoad: true,
        validateAfterChanged: true
      }
    }
  },
  methods: {
    onCommit () {
      this.$axios.post('/api/create_patient', this.model)
        .then(response => (this.result = response['data']))
        .catch(function (error) { console.log(error) })
    }
  }
}
</script>

<style scoped>
</style>
