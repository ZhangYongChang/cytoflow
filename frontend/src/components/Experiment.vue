<template>
  <div>
    <div :id="viewid"
         style="height:400px;width:400px;float:left;"></div>
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
      points: this.item['data']
    }
  },
  mounted () {
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
      color: ['#2f4554', '#61a0a8', '#d48265'],
      tooltip: {
        trigger: 'item',
        axisPointer: {
          type: 'cross'
        }
      },
      xAxis: {
        scale: true,
        name: this.xaxis,
        nameLocation: 'end',
        type: 'log',
        logBase: 10
      },
      yAxis: {
        scale: true,
        name: this.yaxis,
        nameLocation: 'end',
        type: 'log',
        logBase: 10
      },
      series: [{
        type: 'scatter',
        data: this.points
      }]
    }

    let myChart = this.$echarts.init(document.getElementById(this.viewid), 'shine')
    if (option && typeof option === 'object') {
      myChart.setOption(option, true)
    }
  }
}
</script>

<style scoped>
</style>
