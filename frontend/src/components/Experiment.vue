<template>
  <div style="width:500px;height:500px">
    <el-row :gutter="20">
      <el-col :span="4">
        <el-button @click="onClickGateUpload">门上传</el-button>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="8">
        <div :id="viewid" style="height:400px;width:400px;float:left;"></div>
      </el-col>
    </el-row>
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
    }
  },
  data () {
    return {
      viewid: this.item['key'],
      xaxis: this.item['xaxis'],
      yaxis: this.item['yaxis'],
      points: this.item['data'].splice(0, 1000),
      type: this.item['type'],
      // 绘图相关的对象
      myChart: null,
      gateViewGroup: null,
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
      var zr = this.myChart.getZr()
      if (this.gateViewGroup == null) {
        this.gateViewGroup = new zrender.Group()
        this.registerGateDraw(zr)
      }
      this.gateViewGroup.removeAll()
      this.gate = []
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
      // push gate to father
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
    registerGateDraw: function (zr) {
      var drawing
      var points
      var traceEl
      var _this = this
      zr.on('mousedown', function (e) {
        // 如果是十字门直接绘制
        if (_this.gateType === 'cross') {
          // 横线
          var xLine = new echarts.graphic.Line({
            shape: {
              x1: 50,
              y1: e.offsetY,
              x2: 300,
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
              y1: 100,
              x2: e.offsetX,
              y2: 350
            },
            style: {
              stroke: 'green',
              lineWidth: 2
            }
          })
          _this.gateViewGroup.add(xLine)
          _this.gateViewGroup.add(yLine)
          zr.add(_this.gateViewGroup)
          _this.crossGate = [e.offsetX, e.offsetY]
        } else {
          if (!drawing) {
            drawing = true
            _this.gate.push([])
            points = _this.gate[_this.gate.length - 1]
          }
        }
      })
      zr.on('mousemove', function (e) {
        if (_this.gateType === 'cross') {
          // nothing to do
        } else {
          if (drawing && points.length > 0) {
            traceEl.attr('shape', {
              x1: points[points.length - 1][0],
              y1: points[points.length - 1][1],
              x2: e.offsetX,
              y2: e.offsetY
            })
          }
        }
      })
      zr.on('mouseup', function (e) {
        if (_this.gateType === 'cross') {
          // nothing to do
        } else {
          points.push([e.offsetX, e.offsetY])
          traceEl = new echarts.graphic.Line({
            shape: {
              x1: 0, y1: 0, x2: 0, y2: 0
            },
            style: {
              stroke: 'green',
              lineWidth: 2
            }
          })
          _this.gateViewGroup.add(traceEl)
          zr.add(_this.gateViewGroup)
        }
      })
      zr.on('dblclick', function (e) {
        if (_this.gateType === 'cross') {
          // nothing to do
        } else {
          if (points.length < 4 || !drawing) {
            return
          }
          points.length -= 1
          drawing = false
          traceEl.attr('shape', {
            x1: points[points.length - 1][0],
            y1: points[points.length - 1][1],
            x2: points[0][0],
            y2: points[0][1]
          })
        }
        points.push(points[0])
        _this.polygonGate.push(points)
      })
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
          id: xaxis,
          min: 0,
          max: 300,
          scale: true,
          name: xaxis,
          nameLocation: 'end'
        },
        yAxis: {
          id: yaxis,
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
          id: xaxis,
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
          id: yaxis,
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
          id: xaxis,
          scale: true,
          name: xaxis,
          nameLocation: 'end'
        },
        yAxis: {
          id: yaxis,
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
        return createLinearLinearOption(xaxis, yaxis, points)
      } else if (type === 'linearlog') {
        return createLinearLogOption(xaxis, yaxis, points)
      } else {
        return createLogLogOption(xaxis, yaxis, points)
      }
    }

    let option = createOption(this.type, this.xaxis, this.yaxis, this.points)
    this.myChart = this.$echarts.init(document.getElementById(this.viewid), 'shine')
    if (option && typeof option === 'object') {
      this.myChart.setOption(option, true)
    }
    this.initConf()
  }
}
</script>

<style scoped>
</style>
