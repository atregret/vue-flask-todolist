<template>
  <div id = "rt">
    <div id="canvas" style="z-index: 999;"></div>
  
  </div>
  
</template>

<script>
import { Rose } from '@antv/g2plot';
export default {
    name: 'LineChart',
    data() {
        return {
        msg: 'Welcome to Your Vue.js App',
        chart: null,
        data: [
            {
              type: '分类一',
              value: 27,
            },
            {
              type: '分类二',
              value: 25,
            },
            {
              type: '分类三',
              value: 18,
            },
  
],
        }
    },
    mounted() {
      const rosePlot = new Rose('canvas', {
        data:this.data,
        radiusField: 'value',
        categoryField: 'type',
        colorField: 'type',
        color:['blue','yellow','green'],
        label: {
          visible: true,
          type: 'outer',
      
        },
      });

      rosePlot.render();
    }
}
</script>

<style>

</style>