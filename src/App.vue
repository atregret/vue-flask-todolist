<template>
  <div id="app">

    <mu-flex class="flex-body" justify-content="start" >
      <mu-flex class="flex-body-left" justify-content="" >
        <div style="width: 200px;height: 100%;background-color: blue;">
        </div>
      </mu-flex>
      <mu-flex class="flex-body-right" direction="column" align-items="center" fill style="background-color: gainsboro;">
        <mu-flex class="flex-test" justify-content="center" >
            <LineChart></LineChart>
            <PieChart></PieChart>
        </mu-flex>
        <mu-flex class="flex-test" justify-content="center" >
          <mu-container class="cinput">
          <mu-row gutter>
            <mu-col span="12" lg="4" sm="6">
              <mu-auto-complete :data="fruits" label="提示输入内容" v-model="value1"></mu-auto-complete>
            </mu-col>
            <mu-col span="12" lg="4" sm="6">
              <mu-auto-complete :data="fruits" label="激活及显示输入提示" :max-search-results="5"  v-model="value3" open-on-focus></mu-auto-complete>
            </mu-col>

        
            <mu-col span="12" lg="4" sm="6">
              <mu-button color="info">Info</mu-button>
              </mu-col>
          </mu-row>
          
        </mu-container>

        </mu-flex>
        <mu-flex class="flex-test" justify-content="center" >
       
        </mu-flex>
   
      </mu-flex>
    </mu-flex>
 


    
  </div>
</template>

<script>
import LineChart from './components/LineChart.vue'
import PieChart from './components/PieChart.vue'
// import TodoPage from './page/TodoPage.vue'
// import NavMenu from './components/NavMenu.vue'
export default {
  name: 'App',
  components: {
    LineChart,
    PieChart,
    // TodoPage,
    // NavMenu
  }
  ,
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      fruits: ['Apple', 'Banana', 'Orange', 'Watermelon', 'Pear', 'Grape', 'Pineapple', 'Strawberry', 'Cherry', 'Mango'],
      value1:''
    }
  }
}
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
}
.cinput{
  position: relative;
  left:150px;
  top:170px;
}
.button{
  cursor: pointer;
}
.default-transition{
  transition: all 0.4s;
}
.flex-body {
    height: 100%;
    width: 100%;
    margin-top: 8px;
  }
.flex-body-left {
  width: 200px;
  height:100%;
  
}
.flex-body-right {
  height:100%;
}
.flex-test{
  width: 100%;
  height: 100%;
  border: 2px solid black;

}
</style>
