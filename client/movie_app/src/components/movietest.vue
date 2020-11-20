<template>
  <div>
      <div v-for="(movie,idx) in movies" :key="idx">
        {{ movie.title }}
      </div>
  </div>
</template>
 
<script>
const BASE_URL = 'http://localhost:8000/api/v1/movie_community/movies/'

import axios from 'axios'
export default {
  name:'movietest',
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