<template>
  <div id="inde">
    <el-carousel height="300px">
      <el-carousel-item v-for="item in 4" :key="item">
        <h3 class="small">{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>
    <article>
      <section>
        <h1>关于我们</h1>
        <p>计算机爱好者联盟(UCE)是一群热爱计算机的同好者在北化的聚焦地，无论是编程或者美工，无论网站开发还是最基本的玩机技巧，在UCE总会遇见你的知己。我们一起学习自己所喜爱的计算机技术，不断超越自己，看到更大的世界。</p>
      </section>
      <section>
        <h1>WHAT WE DO?</h1>
        <div id="whatwedo">
          <el-row v-for="i in 2" :key="i">
            <el-col :span="8" v-for="j in 3" :key="j">
              <el-image
              class="whatwedoIcon"
              :src="url"
              fit="fill"></el-image>
            </el-col>
          </el-row>
        </div>
      </section>
      <section>
        <button><h1>加入我们</h1></button>
      </section>
    </article>
  </div>
</template>

<script>
export default {
  name: 'index',
  data() {
    return {
      msg: "This is Index",
      url: "./logo.png"
    }
  }
}
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }

  .whatwedoIcon {
    width: 100px;
    height: 100px;
  }
</style>