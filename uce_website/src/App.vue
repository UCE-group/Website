<template>
  <div id="app">
    <navheader></navheader>
    <router-view></router-view>
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
