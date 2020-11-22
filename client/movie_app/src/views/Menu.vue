<template>
<div class='d-flex'>
  <v-navigation-drawer
  class='menubar'>
    this is menu bar
    userprofile사진, 필요
    로그인 안했을 때는 - 로그인 버튼, 회원가입 버튼 나오게
    로그인 했을 때는 - 마이페이지, 로그아웃, 검색창 나오게
    <searching/>
  </v-navigation-drawer>
</div>
</template>

<script>
import Searching from '../components/Searching.vue'
export default {
  components: { Searching },
  name:'Menu',
}
</script>

<style>

</style>