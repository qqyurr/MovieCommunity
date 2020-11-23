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
const BASE_URL = 'http://localhost:8000/api/v1/movie_community/movies/'

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
      axios.get(BASE_URL)
      .then(res=>{
        console.log(res)
        this.movies = res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
    goToDetail(movie) {
      console.log(movie)
      this.$router.push('moviedetail')
    }
  },
}
</script>

<style>

</style>


