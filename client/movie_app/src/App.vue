<template>
  <div id="app"
    class="d-flex flex-row">
      <div>
        <Menu/>
      </div>
      <!-- <router-view/> -->
      
  </div>
</template>

<script>
import Menu from '@/views/Menu'
// import Home from '@/views/Home'
// import Login from '@/views/Login'


export default {
  name: 'App',

  components: {
    // Home,
    Menu,
    // Login,
  },

  data: () => ({
    //
  }),
};
</script>
