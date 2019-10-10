<template>
  <div>
    <div :id="viewid" style="height:400px;width:400px;float:left;"></div>
    <el-checkbox v-model="checked" @change="changeSelect">选择</el-checkbox>
  </div>
</template>

<script>
export default {
  name: 'Experiment',
  props: {
    item: {
      type: JSON,
      default: JSON,
      required: true
    }
  },
  data () {
    return {
      viewid: this.item['key'],
      xaxis: this.item['xaxis'],
      yaxis: this.item['yaxis'],
      points: this.item['data'],
      type: this.item['type'],
      checked: false
    }
  },
  methods: {
    changeSelect: function (value) {
      if (value) {
        this.$emit('figSelect', {
          viewid: this.item['key'],
          gate: []
        })
      } else {
        this.$emit('figDel', {
          viewid: this.item['key'],
          gate: []
        })
      }
    }
  },
  mounted () {
    function createLinearLogOption (xaxis, yaxis, points) {
      points.forEach(function (elem, index) {
        points[index][0] = points[index][0] / 1000
      })

      points = points.filter(function (item) {
        return item[0] > 0 && item[1] > 10
      })
      var option = {
        toolbox: {
          show: true,
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            saveAsImage: {}
          }
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'cross'
          }
        },
        xAxis: {
          min: 0,
          max: 300,
          scale: true,
          name: xaxis,
          nameLocation: 'end'
        },
        yAxis: {
          min: 10,
          max: 100000,
          scale: true,
          name: yaxis,
          nameLocation: 'end',
          type: 'log',
          logBase: 10,
          axisLabel: {
            formatter: function (value, index) {
              var text = Math.log10(value).toString()
              return '10^' + text
            }
          }
        },
        series: [{
          type: 'scatter',
          symbolSize: 3,
          data: points
        }]
      }
      return option
    }

    function createLogLogOption (xaxis, yaxis, points) {
      points = points.filter(function (item) {
        return item[0] > 10 && item[1] > 10
      })
      var option = {
        toolbox: {
          show: true,
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            saveAsImage: {}
          }
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'cross'
          }
        },
        xAxis: {
          min: 10,
          max: 100000,
          scale: true,
          name: xaxis,
          nameLocation: 'end',
          type: 'log',
          logBase: 10,
          axisLabel: {
            formatter: function (value, index) {
              var text = Math.log10(value).toString()
              return '10^' + text
            }
          }
        },
        yAxis: {
          min: 10,
          max: 100000,
          scale: true,
          name: yaxis,
          nameLocation: 'end',
          type: 'log',
          logBase: 10,
          axisLabel: {
            formatter: function (value, index) {
              var text = Math.log10(value).toString()
              return '10^' + text
            }
          }
        },
        series: [{
          type: 'scatter',
          symbolSize: 3,
          data: points
        }]
      }
      return option
    }

    function createLinearLinearOption (xaxis, yaxis, points) {
      points.forEach(function (ele, index) {
        points[index][0] = points[index][0] / 1000
        points[index][1] = points[index][1] / 1000
      })
      points = points.filter(function (item) {
        return item[0] > 0 && item[1] > 0
      })
      var option = {
        toolbox: {
          show: true,
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            saveAsImage: {}
          }
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'cross'
          }
        },
        xAxis: {
          scale: true,
          name: xaxis,
          nameLocation: 'end'
        },
        yAxis: {
          scale: true,
          name: yaxis,
          nameLocation: 'end'
        },
        series: [{
          type: 'scatter',
          symbolSize: 3,
          data: points
        }]
      }
      return option
    }

    function createOption (type, xaxis, yaxis, points) {
      if (type === 'linearlinear') {
        console.log('linearlinear')
        return createLinearLinearOption(xaxis, yaxis, points)
      } else if (type === 'linearlog') {
        console.log('linearlog')
        return createLinearLogOption(xaxis, yaxis, points)
      } else {
        console.log('loglog')
        return createLogLogOption(xaxis, yaxis, points)
      }
    }

    let option = createOption(this.type, this.xaxis, this.yaxis, this.points)
    let myChart = this.$echarts.init(document.getElementById(this.viewid), 'shine')
    if (option && typeof option === 'object') {
      myChart.setOption(option, true)
      myChart.on('click', function (params) {
        console.log(params)
        let x = param.x
        let y = param.y;
        let result = self.chartInstance.convertFromPixel({
          seriesIndex: 0,
          xAxisIndex: 0
        }, [x, y])
      })
    }
  }
}
</script>

<style scoped>
</style>
