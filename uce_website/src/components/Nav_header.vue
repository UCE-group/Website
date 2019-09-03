<template>
<div id="nav_header">
  <el-menu
  :default-active="activeIndex2"
  class="el-menu-demo"
  mode="horizontal"
  @select="handleSelect"
  background-color="#545c64"
  text-color="#fff"
  active-text-color="#ffd04b">
  <el-menu-item index="1"><router-link tag="el-link" :underline="false" :to="{name: 'index'}">计算机爱好者联盟</router-link></el-menu-item>
  <el-menu-item index="2">社团简介</el-menu-item>
  <el-menu-item index="3">项目介绍</el-menu-item>
  <el-menu-item index="4">学习资源</el-menu-item>
  <el-menu-item index="5">近期活动</el-menu-item>
  <el-menu-item index="6">
    <el-row :gutter="20">
      <el-col :span="10"><el-avatar :size="40" :src="userAvatarURL"></el-avatar></el-col>
      <el-col :span="10"><span id="username">{{userName}}</span></el-col>
    </el-row>
  </el-menu-item>
  </el-menu>
</div>
</template>

<script>
  export default {
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        userAvatarURL: './logo.png',
        userName: 'Jaye瓶子'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>