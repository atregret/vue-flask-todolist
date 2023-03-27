<template>
  <div id = "line">
    <div id="linecanvas"></div>
  
  </div>
  
</template>

<script>
//import { Pie } from '@antv/g2plot';
import { Line } from '@antv/g2plot';
export default {
    name: 'LineChart',
    data() {
        return {
        msg: 'Welcome to Your Vue.js App',
        chart: null,
        data:[
          { year: '1991', value: 3 },
          { year: '1992', value: 4 },
          { year: '1993', value: 3.5 },
          { year: '1994', value: 5 },
          { year: '1995', value: 4.9 },
          { year: '1996', value: 6 },
          { year: '1997', value: 7 },
          { year: '1998', value: 9 },
          { year: '1999', value: 13 },
],
  
        }
    },
    mounted() {
            
      const linePlot = new Line('linecanvas', {
        title: {
          visible: true,
          text: '折线图',
        },
        description: {
          visible: true,
          text: '用平滑的曲线代替折线。',
        },
        data:this.data,
        xField: 'year',
        yField: 'value',
        width: 200,
        height: 200,
      });

      linePlot.render();
}
}
</script>

<style>

</style>


// const linePlot = new Line('canvas', {
//   title: {
//     visible: true,
//     text: '折线图',
//   },
//   description: {
//     visible: true,
//     text: '用平滑的曲线代替折线。',
//   },
//   data:this.data2,
//   xField: 'year',
//   yField: 'value',
//   width: 200,
//   height: 200,
// });

// linePlot.render();