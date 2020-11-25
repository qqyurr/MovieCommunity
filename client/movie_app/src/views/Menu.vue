<template>
    
    <v-app id="app">
      <v-app-bar 
        app 
        flat 
        clipped-left 
        class="navbar d-flex justify-space-between white"
      >
        <v-app-bar-nav-icon @click="drawerState = !drawerState" class='logo'/>
        <router-link :to="'/'" class='logo' > 
                  
        <h1 class='font-italic logo'>
          Oh, young me
        </h1>
        </router-link>
      </v-app-bar>
      <v-navigation-drawer v-model="drawerState" app flat clipped color="white" >
        <!-- content -->
      

        <v-list dense class='menu'>
          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <router-link :to="item.url" class='link'> 
                  {{item.title}} 
                </router-link>
            </v-list-item-content>
          </v-list-item>
          <br>

          <searching class='searching'/>

        </v-list>

            <v-list-item-content>
            <router-link @click.native="logout" to="#"> Logout </router-link>
          </v-list-item-content>

      </v-navigation-drawer>
      <v-content>
        <v-container>
          <v-row justify="center" align="center" class="mt-10">
            <v-col cols="auto">
              <!--출력되는곳 -->
              <router-view/>
            </v-col>
          </v-row>
        </v-container>
      </v-content>
    </v-app>

</template>



<script>
import Searching from '@/components/Searching'

export default {
  name: 'Menu',
  components:{
  Searching,
  },
  
  methods: {
    logout: function() {
      localStorage.removeItem('jwt')
      this.$router.push({name: 'Login'})
    },
  },

  data () {
      return {
        items: [
          { title: 'MyPage', icon: 'mdi-home', url: '/mypage' },
          { title: 'Home', icon: 'mdi-account', url: '/' },
          { title: 'Login', icon: 'mdi-login', url: '/accounts/login' },
          { title: 'Signup', icon: 'mdi-account-plus-outline', url: '/accounts/signup' },
          { title: 'Recommend', icon: 'mdi-compass-outline', url: '/recommend' },

        ],
      }
    },
  computed: {
    drawerState: {
      get () { return this.$store.getters.drawerState },
      set (v) { return this.$store.commit('toggleDrawerState', v) }
    }
  }


}
</script>

<style>
.logo {
  font-weight: 600;
  text-decoration: none !important;
  color: grey;
}
.link{
  color: grey !important;
  font-weight: 600;
  text-decoration: none !important;
}
.searching{
  margin: 10 10 10 10;
}
.navbar {
  opacity: 50%;
}
.menu {
  opacity: 70%;
  border-color:none !important;
}
</style>
