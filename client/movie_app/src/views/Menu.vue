<template>
    <div id="app">
    <v-app id="inspire">
      <v-app-bar app clipped-left class="primary">
        <v-app-bar-nav-icon @click="drawerState = !drawerState"/>
      </v-app-bar>
      <v-navigation-drawer v-model="drawerState" app clipped color="grey lighten-4">
        <!-- content -->
      

        <v-list dense>
          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <router-link :to="item.url"> {{item.title}} </router-link>
            </v-list-item-content>
          </v-list-item>
          <br>

          <searching/>

        </v-list>
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
  </div>
</template>



<script>
import Searching from '@/components/Searching'

export default {
  name: 'Menu',
  components:{
  Searching,
  },
  data () {
      return {
        items: [
          { title: 'MyPage', icon: 'mdi-view-dashboard', url: '/mypage' },
          { title: 'Home', icon: 'mdi-view-dashboard', url: '/' },
          { title: 'Login', icon: 'mdi-forum', url: '/accounts/login' },
          { title: 'Signup', icon: 'mdi-forum', url: '/accounts/signup' },
          { title: 'Recommend', icon: 'mdi-forum', url: '/recommend' },

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

</style>
