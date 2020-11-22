<template>
  <v-container
    class="fill-height"
    fluid
    style="min-height: 300px"
  >
    <h1>코미디</h1>
    <v-card v-for="(movie,idx) in movies.comedy_movies" :key="idx">
      <v-card-title >
       {{ movie.title }}
      </v-card-title>
       <v-img 
        :src="movie.poster_path" 
        alt="poster img"
        height="300"
      >
      </v-img>
    </v-card>
    <h1>액션</h1>
    <v-card v-for="(movie,idx) in movies.action_movies" :key="idx">
      <v-card-title >
       {{ movie.title }}
      </v-card-title>
       <v-img 
        :src="movie.poster_path" 
        alt="poster img"
        height="300"
      >
      </v-img>
    </v-card>
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
    }
  },
}
</script>

<style>

</style>