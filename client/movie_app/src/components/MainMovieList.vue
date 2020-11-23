<template>
  <v-app id="inspire">
    <!-- <v-system-bar app>
      <v-spacer></v-spacer>

      <v-icon>mdi-square</v-icon>

      <v-icon>mdi-circle</v-icon>

      <v-icon>mdi-triangle</v-icon>
    </v-system-bar>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Application</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      fixed
      temporary
    >
    </v-navigation-drawer> -->

    <v-main class="grey lighten-2">
      <v-container>
        <v-row>

                       <!-- <v-col v-for="(movie,idx) in movies.comedy_movies.slice(0,6)" :key="idx" cols="12" sm="6" md="2" class="pa-1">
                <v-card @click='goToDetail(movie)' outlined>
                  <v-img :max-height="250" :src="movie.poster_path"></v-img>
                  <v-card-title class="subtitle-1">{{movie.title}}</v-card-title>
                </v-card>
              </v-col> -->



          <!-- <template v-for="n in 4"> -->
            <v-col
              :key="n"
              class="mt-2"
              cols="12"
            >
            <strong>Comedy</strong>
            </v-col>

            <v-col
              v-for="(movie,idx) in movies.comedy_movies.slice(0,6)"
              :key="`${n}${idx}`"
              cols="6"
              md="2"
            >
              <v-sheet  height="150" >
                <v-img :max-height="250" :src="movie.poster_path" @click="goToDetail(movie)"></v-img>
              </v-sheet>
            </v-col>

            <v-col
              :key="n"
              class="mt-2"
              cols="12"
            >
            <strong>Action</strong>
            </v-col>

            <v-col
              v-for="(movie,idx) in movies.action_movies.slice(0,6)"
              :key="`${n}${idx}`"
              cols="6"
              md="2"
            >
              <v-sheet height="150">
                <v-img :max-height="250" :src="movie.poster_path" @click="goToDetail(movie)"></v-img>
              </v-sheet>
            </v-col>

            <v-col
              :key="n"
              class="mt-2"
              cols="12"
            >
            <strong>Horror</strong>
            </v-col>

            <v-col
              v-for="(movie,idx) in movies.horror_movies.slice(0,6)"
              :key="`${n}${idx}`"
              cols="6"
              md="2"
            >
              <v-sheet height="150">
                <v-img :max-height="250" :src="movie.poster_path" @click="goToDetail(movie)"></v-img>
              </v-sheet>
            </v-col>
          <!-- </template> -->
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>
 
<script>
const SERVER_URL = 'http://localhost:8000/api/v1/movie_community/movies/'

import axios from 'axios'
export default {
  name:'MainMovieList',
  data() {
    return {
      movies: [],
      draweer: null,
    }
  },
  created() {
    this.getMovie()
  },
  methods: {
    getMovie() {
      const myToken = localStorage.getItem('jwt')

      axios.get(SERVER_URL, {params:{}, headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
        console.log(res.data.movies_by_genre)
        console.log(res.data.movies_by_genre.action_movies)
        this.movies = res.data.movies_by_genre
      })
      .catch(err=>{
        console.log(err)
      })
    },
    goToDetail(movie) {
      console.log('goToDetail clicked! ')
      this.$store.state.selectedMovie = movie.id
      console.log(this.$store.state.selectedMovie)
      this.$router.push('/movies/' + movie.id + '/reviews/')
    }
  },
}
</script>

<style>

</style>


