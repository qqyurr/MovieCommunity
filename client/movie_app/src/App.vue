<template>
  <div id="app"
    class="d-flex flex-row appBack">
      <div>
        <Menu :login="login"/>
      </div>
      <!-- <router-view/> -->
      
  </div>
</template>

<script>
import Menu from '@/views/Menu'


export default {
  name: 'App',

  components: {
    Menu,
  },

  data: function() {
    return {
      login: false
    }
  },
  
  created: function() {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.login = true
    }
  },
};
</script>

<style scoped>
#app {
  font-family: 'Montserrat','Noto Sans Kr', sans-serif;
}
.appBack {
  margin: 0px !important;
  padding: 0px !important;
}

</style>