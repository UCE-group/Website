<template>
  <div id="app">
    <el-container>
      <el-header><navheader></navheader></el-header>
      <el-main><router-view></router-view></el-main>
    </el-container>
  </div>
</template>

<script>
import Nav_header from './components/Nav_header'

export default {
  name: 'app',
  components: {
    'navheader': Nav_header
  }
}
</script>
