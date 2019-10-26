<template>
  <div style="width:600px;height:600px;float:left;border:1px solid #00F">
    <div style="width:600px;height:100px">
      <el-button @click="onClickGateUpload">门上传</el-button>
    </div>
    <div :id="viewid" style="width:500px;height:500px"></div>
  </div>
</template>

<script>
import echarts from 'echarts'
import zrender from 'zrender'
export default {
  name: 'Experiment',
  props: {
    item: {
      type: Object,
      default: Object,
      required: true
    },
    hisGates: {
      type: Object,
      default: Object,
      required: true
    }
  },
  data () {
    return {
      viewid: this.item['key'],
      xaxis: this.item['xaxis'],
      yaxis: this.item['yaxis'],
      points: this.item['data'].splice(0, 1500),
      type: this.item['type'],
      // 绘图相关的对象
      myChart: null,
      gateViewGroup: null,
      polygonPoints: null,
      traceEl: null,
      drawing: false,
      // 控制相关对象
      checked: false,
      // polygon or cross
      gateType: 'cross',
      // 绘图的结果，对于十字门来说是1维数组，[x1,y1]对于多边形来说是3维数组[[[x1,y1],...,[xn,yn],[x1,y1]],[[x1,y1],...,[xk,yk],[x1,y1]]]
      crossGate: [],
      polygonGate: []
    }
  },
  methods: {
    initConf: function (value) {
      if (this.type === 'linearlog') {
        this.gateType = 'polygon'
      } else {
        this.gateType = 'cross'
      }
      if (this.gateViewGroup == null) {
        this.gateViewGroup = new zrender.Group()
        this.registerGateDraw()
      }
      this.gateViewGroup.removeAll()
      this.gate = []
    },
    registerGateDraw: function () {
      this.myChart.getZr().on('mousedown', this.onMouseDown)
      this.myChart.getZr().on('mousemove', this.onMouseMove)
      this.myChart.getZr().on('mouseup', this.onMouseUp)
      this.myChart.getZr().on('dblclick', this.onDbClick)
    },
    onMouseDown: function (e) {
      // 如果是十字门直接绘制
      if (this.gateType === 'cross') {
        // 横线
        var xLine = new echarts.graphic.Line({
          shape: {
            x1: e.offsetX - 100,
            y1: e.offsetY,
            x2: e.offsetX + 100,
            y2: e.offsetY
          },
          style: {
            stroke: 'green',
            lineWidth: 2
          }
        })
        // 竖线
        var yLine = new echarts.graphic.Line({
          shape: {
            x1: e.offsetX,
            y1: e.offsetY - 100,
            x2: e.offsetX,
            y2: e.offsetY + 100
          },
          style: {
            stroke: 'green',
            lineWidth: 2
          }
        })
        this.gateViewGroup.add(xLine)
        this.gateViewGroup.add(yLine)
        this.myChart.getZr().add(this.gateViewGroup)
        this.crossGate = [e.offsetX, e.offsetY]
      } else {
        if (!this.drawing) {
          this.drawing = true
          this.gate.push([])
          this.polygonPoints = this.gate[this.gate.length - 1]
        }
      }
    },
    onMouseMove: function (e) {
      if (this.gateType === 'cross') {
        // nothing to do
      } else {
        if (this.drawing && this.polygonPoints.length > 0) {
          this.traceEl.attr('shape', {
            x1: this.polygonPoints[this.polygonPoints.length - 1][0],
            y1: this.polygonPoints[this.polygonPoints.length - 1][1],
            x2: e.offsetX,
            y2: e.offsetY
          })
        }
      }
    },
    onMouseUp: function (e) {
      if (this.gateType === 'cross') {
        // nothing to do
      } else {
        this.polygonPoints.push([e.offsetX, e.offsetY])
        this.traceEl = new echarts.graphic.Line({
          shape: {
            x1: 0, y1: 0, x2: 0, y2: 0
          },
          style: {
            stroke: 'green',
            lineWidth: 2
          }
        })
        this.gateViewGroup.add(this.traceEl)
        this.myChart.getZr().add(this.gateViewGroup)
      }
    },
    onDbClick: function (e) {
      if (this.gateType === 'cross') {
        // nothing to do
      } else {
        if (this.polygonPoints.length < 4 || !this.drawing) {
          return
        }
        this.polygonPoints.length -= 1
        this.drawing = false
        this.traceEl.attr('shape', {
          x1: this.polygonPoints[this.polygonPoints.length - 1][0],
          y1: this.polygonPoints[this.polygonPoints.length - 1][1],
          x2: this.polygonPoints[0][0],
          y2: this.polygonPoints[0][1]
        })
      }
      this.polygonPoints.push(this.polygonPoints[0])
      this.polygonGate.push(this.polygonPoints)
    },
    onClickGateUpload: function () {
      if (this.gateType === 'cross') {
        this.crossGate = this.point2Coord(this.crossGate)
      } else {
        var gateData = []
        this.polygonGate.forEach((elem, index) => {
          var polygon = []
          elem.forEach((point, index) => {
            polygon.push(this.point2Coord(point))
          })
          gateData.push(polygon)
        })
        this.polygonGate = gateData
      }
      this.postGateData()
      var gatetype = 0
      if (this.gateType === 'polygon') {
        gatetype = 1
      }
      this.$emit('saveGate', {
        gatetype: gatetype,
        gates: {
          xaxis: this.xaxis,
          yaxis: this.yaxis,
          crossGate: this.crossGate,
          polygonGate: this.polygonGate
        }
      })
    },
    postGateData: function () {
      let result = []
      if (this.type === 'linearlinear' && this.gateType === 'cross') {
        result = [this.crossGate[0] * 1000, this.crossGate[1] * 1000]
        this.crossGate = result
        return
      }
      if (this.type === 'linearlog' && this.gateType === 'polygon') {
        this.polygonGate.forEach((elem, index) => {
          var polygon = []
          elem.forEach((point, index) => {
            polygon.push([point[0] * 1000, point[1]])
          })
          result.push(polygon)
        })
        this.polygonGate = result
      }
    },
    point2Coord: function (position) {
      return this.myChart.convertFromPixel({ seriesIndex: 0 }, position)
    },
    createLinearLogOption: function () {
      this.points.forEach((elem, index) => {
        this.points[index][0] = this.points[index][0] / 1000
      })

      this.points = this.points.filter(function (item) {
        return item[0] > 0 && item[1] > 10
      })
      var option = {
        animation: false,
        toolbox: {
          show: false,
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            saveAsImage: {}
          }
        },
        tooltip: {
          show: false,
          trigger: 'item',
          axisPointer: {
            type: 'cross'
          }
        },
        xAxis: {
          id: this.xaxis,
          min: 0,
          max: 300,
          scale: true,
          name: this.xaxis,
          nameLocation: 'end'
        },
        yAxis: {
          id: this.yaxis,
          min: 10,
          max: 100000,
          scale: true,
          name: this.yaxis,
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
          data: this.points
        }]
      }
      return option
    },
    createLogLogOption: function () {
      this.points = this.points.filter(function (item) {
        return item[0] > 10 && item[1] > 10
      })
      var option = {
        animation: false,
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
          id: this.xaxis,
          min: 10,
          max: 100000,
          scale: true,
          name: this.xaxis,
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
          id: this.yaxis,
          min: 10,
          max: 100000,
          scale: true,
          name: this.yaxis,
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
          data: this.points
        }]
      }
      return option
    },
    createLinearLinearOption: function () {
      this.points.forEach((elem, index) => {
        this.points[index][0] = this.points[index][0] / 1000
        this.points[index][1] = this.points[index][1] / 1000
      })
      this.points = this.points.filter(function (item) {
        return item[0] > 0 && item[1] > 0
      })
      var option = {
        animation: false,
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
          id: this.xaxis,
          scale: true,
          name: this.xaxis,
          nameLocation: 'end'
        },
        yAxis: {
          id: this.yaxis,
          scale: true,
          name: this.yaxis,
          nameLocation: 'end'
        },
        series: [{
          type: 'scatter',
          symbolSize: 3,
          data: this.points
        }]
      }
      return option
    },
    createOption: function () {
      if (this.type === 'linearlinear') {
        return this.createLinearLinearOption()
      } else if (this.type === 'linearlog') {
        return this.createLinearLogOption()
      } else {
        return this.createLogLogOption()
      }
    }
  },
  mounted () {
    let option = this.createOption()
    this.myChart = this.$echarts.init(document.getElementById(this.viewid), 'shine')
    if (option && typeof option === 'object') {
      this.myChart.setOption(option, true)
    }
    this.initConf()
  },
  destroyed () {
    this.points = []
    this.$echarts.dispose(this.myChart)
    this.myChart = null
    this.gateViewGroup = null
    this.points = null
    this.polygonPoints = null
    this.traceEl = null
    this.drawing = false
  }
}
</script>

<style scoped>
</style>
