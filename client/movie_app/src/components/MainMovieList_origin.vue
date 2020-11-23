<template>
  <v-container
    class="fill-height"
    fluid
    style="min-height: 300px"
  >
  <v-app id="app">
    <v-content>

      <!-- MainContentContainer starts -->


      <!-- <v-container style="margin-top: -4rem; width: 1600px;">
        <v-card outlined style="width: 1600px;" class="mx-auto" >
          <v-card-title>Comedy</v-card-title>
          <v-card-text style="width: 1600px;">
            <v-row no-gutters>
              <v-col v-for="(movie,idx) in movies.comedy_movies.slice(0,6)" :key="idx" cols="12" sm="6" md="2" class="pa-1">
                <v-card outlined>
                  <v-img :max-height="250" :src="movie.poster_path"></v-img>
                  <v-card-title class="subtitle-1">{{movie.title}}</v-card-title>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-container> -->

      <v-container style="margin-top: -4rem; width: 1600px;">
        <v-card outlined style="width: 1600px;" class="mx-auto" >
          <v-card-title>Comedy</v-card-title>
          <v-card-text style="width: 1600px;">
            <v-row no-gutters>
              <v-col v-for="(movie,idx) in movies.comedy_movies.slice(0,6)" :key="idx" cols="12" sm="6" md="2" class="pa-1">
                <v-card @click='goToDetail(movie)' outlined>
                  <v-img :max-height="250" :src="movie.poster_path"></v-img>
                  <v-card-title class="subtitle-1">{{movie.title}}</v-card-title>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-container>
      <!-- MainContentContainer ends -->

      </v-content>
    </v-app>
  </v-container>
</template>
 
<script>
const SERVER_URL = 'http://localhost:8000/api/v1/movie_community/movies/'

import axios from 'axios'
export default {
  name:'MainMovieList',
  data() {
    return {
      movies: [],
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
        console.log(res)
        this.movies = res.data
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


