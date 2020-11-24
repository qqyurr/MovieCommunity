<template>
  <v-app id="inspire" v-if="isLoaded">
    <v-main class="grey lighten-2">
      <v-container>
        <v-row>
            <v-col
              class="mt-2"
              cols="12"
            >
            <strong>Comedy</strong>
            </v-col>

            <v-col
              v-for="(movie) in movies.comedy_movies.slice(0,6)"
              :key="movie.id"
              cols="6"
              md="2"
            >
              <v-sheet  height="150" >
                <v-img :max-height="250" :src="movie.poster_path" @click="goToDetail(movie)"></v-img>
              </v-sheet>
            </v-col>

            <v-col
              class="mt-2"
              cols="12"
            >
            <strong>Action</strong>
            </v-col>

            <v-col
              v-for="(movie) in movies.action_movies.slice(0,6)"
              :key="movie.id"
              cols="6"
              md="2"
            >
              <v-sheet height="150">
                <v-img :max-height="250" :src="movie.poster_path" @click="goToDetail(movie)"></v-img>
              </v-sheet>
            </v-col>

            <v-col
              class="mt-2"
              cols="12"
            >
            <strong>Horror</strong>
            </v-col>

            <v-col
              v-for="(movie) in movies.horror_movies.slice(0,6)"
              :key="movie.id"
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
const SERVER_URL = 'http://localhost:8000/api/v1/movie_community/movie_list_by_genre/'

import axios from 'axios'
export default {
  name:'MainMovieList',
  data() {
    return {
      movies: [],
      draweer: null,
      isLoaded: false,
    }
  },
  created() {
    this.getMovie()
  },
  methods: {
    getMovie() {
      const myToken = localStorage.getItem('jwt')
      axios.get(SERVER_URL, {headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
        console.log(res.data.movies_by_genre)
        console.log(res.data.movies_by_genre.action_movies)
        this.movies = res.data.movies_by_genre
        this.isLoaded = true
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


