<template>
  <v-app class="home">
       <v-btn
      class="mx-2"
      fab
      dark
      color="teal"
    >
    <v-icon dark>
      mdi-format-list-bulleted-square
    </v-icon>
    </v-btn>
    <no-login />
    <!-- <규연이가 아이패드로 그린 우리의 로고...손그림 그것이 매력포인트여 -->
    <main-movie-list />

  </v-app>
</template>

<script>
// @ is an alias to /src
import MainMovieList from '../components/MainMovieList.vue'
import NoLogin from '../components/NoLogin.vue'

export default {
  name: 'Home',
  components: {
    MainMovieList,
    NoLogin,
  }
}
</script>
